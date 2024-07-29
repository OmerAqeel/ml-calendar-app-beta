import json
import nltk 
from datetime import datetime
import sys

nltk.data.path.append('./punkt')
nltk.data.path.append('./averaged_perceptron_tagger')

def process_text(text):
    processed_text = text.lower()
    tokens = nltk.word_tokenize(processed_text)
    tagged_tokens = nltk.pos_tag(tokens)
    return json.dumps(tagged_tokens)  # Return the processed data as JSON

def extract_features(text):
   #identify words that indicate priority and urgency
   urgent_words = ['urgent', 'immediate', 'asap', 'quick', 'quickly']
   is_urgent = any(word in text for word in urgent_words)

   



if __name__ == "__main__":
  if len(sys.argv) > 1:
    text = sys.argv[1]  # Access the text argument passed from the backend
    result = process_text(text)
    print(result)  # For debugging purposes
  else:
    print("Error: No text provided")