import json
import nltk
import sys
import spacy
import re
from dateutil import parser

# Make sure the nltk data is downloaded
nltk.data.path.append('./punkt')
nltk.data.path.append('./averaged_perceptron_tagger')

def process_text(text):
    processed_text = text.lower()
    tokens = nltk.word_tokenize(processed_text)
    tagged_tokens = nltk.pos_tag(tokens)
    return json.dumps(tagged_tokens)  # Return the processed data as JSON

def extract_deadlines(deadlines_text):
    deadlines = {}
    pattern = re.compile(r'(.+?) by (\d{4}-\d{2}-\d{2})', re.IGNORECASE)
    matches = pattern.findall(deadlines_text)
    for match in matches:
        task, date = match
        deadlines[task.strip().lower()] = date
    return deadlines

def extract_features(text, deadlines):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())  # Parse the text using spaCy
    print(f"doc => {doc}")
    
    urgent_words = ["urgent", "urgently", "asap", "immediately"]
    features = []

    for sentence in doc.sents:  # Iterate through sentences
        sentence_text = sentence.text
        is_urgent = any(word in sentence_text for word in urgent_words)
        
        for token in sentence:
            if token.pos_ == "VERB":  # Focus on verbs for potential tasks
                task_words = [token.text]
                deadline_words = []
                
                # Process children for task words and deadlines
                for child in token.children:
                    task_words.append(child.text)
                    if child.dep_ in ["npadvmod", "prep", "pobj", "advmod"]:
                        deadline_words.append(child.text)
                    # Include grandchildren for better deadline extraction
                    for grandchild in child.children:
                        if grandchild.dep_ in ["pobj", "npadvmod", "advmod"]:
                            deadline_words.append(grandchild.text)
                
                print(f"Token: {token.text}")
                print(f"Children: {[child.text for child in token.children]}")
                print(f"Task Words: {task_words}")
                print(f"Deadline Words: {deadline_words}")
                
                if task_words:
                    task = " ".join(task_words)
                    # Check if any user-provided deadline matches the current task
                    deadline = None
                    for user_task, user_deadline in deadlines.items():
                        if user_task in task:
                            deadline = user_deadline
                            break
                    features.append({
                        "task": task,
                        "is_urgent": is_urgent,
                        "deadline": deadline
                    })

                # Add a debug print for the whole feature set at this step
                print(f"Features: {features}")
    
    return json.dumps(features, indent=2)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        text = sys.argv[1]  # Access the text argument passed from the backend
        deadlines_text = sys.argv[2]  # Access the deadlines argument passed from the backend
        deadlines = extract_deadlines(deadlines_text)  # Extract deadlines from the text
        result = extract_features(text, deadlines)
        print(result)  # For debugging purposes
    else:
        print("Error: No text or deadlines provided")