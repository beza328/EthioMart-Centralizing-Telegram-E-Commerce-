import sys
import os
import pandas as pd
import re

def label_tokens_with_price(tokens):
    labeled_tokens = []
    
    # Label the first token as B-Product
    if tokens:
        labeled_tokens.append(f"{tokens[0]} B-Product")
    
    # Label the next three tokens as I-Product (if they exist)
    for token in tokens[1:4]:
        labeled_tokens.append(f"{token} I-Product")
    
    # Label specific tokens for B-LOC and I-LOC
    for token in tokens[4:]:
        if token == "መገናኛ" or token == "ፒያሳ":
            labeled_tokens.append(f"{token} B-LOC")
        elif token in ["ራመት_ታቦር_ኦዳ_ህንፃ", "ጊዮርጊስ", "አደባባይ", "መሰረት", "ደፋር", "ሞል"]:
            labeled_tokens.append(f"{token} I-LOC")
        elif token == "ዋጋ":
            labeled_tokens.append(f"{token} B-PRICE")
        elif token == "ብር":
            labeled_tokens.append(f"{token} I-PRICE")  # Assuming "ብር" follows "ዋጋ"
        elif re.match(r'^\d{3,}$', token):  # Label 3-digit numbers and above as I-PRICE
            labeled_tokens.append(f"{token} I-PRICE")
        else:
            labeled_tokens.append(f"{token} O")
    
    return labeled_tokens

# Function to process and label a subset of 200 messages from the data
def process_and_label_200_messages_with_price(df, num_messages=200):
    labeled_data = []
    
    # Take the first 200 messages
    for i, message in enumerate(df['Message'][:num_messages]):
        tokens = re.findall(r'\w+', message)  # Tokenizing the message
        labeled_tokens = label_tokens_with_price(tokens)  # Labeling the tokens
        
        # Append each message's labeled tokens
        labeled_data.append("\n".join(labeled_tokens))
    
    # Join labeled messages with blank lines between them
    return "\n\n".join(labeled_data)