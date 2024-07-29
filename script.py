import json
import nltk 
from datetime import datetime
import sys

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def process_text(text):
    processed_text = text.lower()
    tokens = nltk.word_tokenize(processed_text)
    tagged_tokens = nltk.pos_tag(tokens)
    print(tagged_tokens)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    text = sys.argv[1]  # Access the text argument passed from the backend
    result = process_text(text)
    print(result)  # or use the result for further processing
  else:
    print("Error: No text provided")




