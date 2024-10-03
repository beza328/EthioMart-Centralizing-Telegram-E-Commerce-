import sys
import os
import pandas as pd
import re

def remove_emojis(text):
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251" 
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)



# Define the phrases to be removed
phrases_to_remove = [
    'በTelegram', 'ለማዘዝ', 'ይጠቀሙ', 
    'zemencallcenter', 'zemenexpressadmin', 
    'ለተጨማሪ', 'ማብራሪያ', 'የቴሌግራም', 
    'ገፃችን', 'https', 'telegram', 'me', 
    'zemenexpress'
]

# Create a regex pattern to match any of the phrases
pattern = '|'.join(re.escape(phrase) for phrase in phrases_to_remove)

# Function to clean the messages
def clean_message(message):
    # Check if the message is a list and convert it to a string
    if isinstance(message, list):
        message = ' '.join(message)  # Join list elements into a single string

    # Remove phone numbers
    message = re.sub(r'\+?\d[\d\s()-]{7,}\d', '', message)  # Matches common phone number patterns

    # Remove specified phrases
    message = re.sub(pattern, '', message)  # Remove phrases
    
    return message.strip()  # Strip leading/trailing whitespace




#Preprocesing Steps
### Step 1: Tokenization ###

# Tokenize by splitting on spaces and punctuations
def tokenize_amharic(text):
    # Using regex to split on spaces and punctuation
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

### Step 2: Normalization ###

# Normalize the Amharic text
def normalize_amharic(text):
    # Replace numbers with their Amharic counterparts if needed, or standardize them
    normalized_text = re.sub(r'[፣።፡፥፦]', ' ', text)  # Remove Amharic punctuation marks
    normalized_text = normalized_text.replace('።', '')  # Example of normalizing punctuation
    normalized_text = normalized_text.strip()  # Remove leading/trailing spaces
    return normalized_text

### Step 3: Handling Amharic-specific linguistic features ###

# Removing special characters, diacritics, and handling Amharic stopwords
def handle_amharic_linguistic_features(tokens):
    stopwords = ['እና', 'ነው', 'የ', 'በ', 'ማለት']  # Add common Amharic stopwords
    cleaned_tokens = [token for token in tokens if token not in stopwords]
    return cleaned_tokens

### Combine All Steps in Preprocessing Function ###

def preprocess_amharic_text(text):
    # Step 1: Tokenize the text
    tokens = tokenize_amharic(text)
    
    # Step 2: Normalize the text
    normalized_text = normalize_amharic(text)
    
    # Step 3: Handle Amharic-specific linguistic features
    cleaned_tokens = handle_amharic_linguistic_features(tokens)

    # Step 4: Join tokens back into a single string without quotes
    cleaned_text = ' '.join(cleaned_tokens)

    
    return cleaned_tokens


