import pandas as pd
from additional.config import CSV_DATA_LOC

def expand_contractions(text):
    # Dictionary of common contractions
    contractions = {
        "we're": "we are",
        "you're": "you are",
        "they're": "they are",
        "I'm": "I am",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "can't": "cannot",
        "won't": "will not",
        "don't": "do not",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "hasn't": "has not",
        "haven't": "have not",
        "hadn't": "had not",
        "wouldn't": "would not",
        "shouldn't": "should not",
        "couldn't": "could not",
        "let's": "let us",
        "that's": "that is",
        "who's": "who is",
        "what's": "what is",
        "where's": "where is",
        "why's": "why is",
        "when's": "when is"
    }
    # Replace contractions in the text
    for contraction, expanded in contractions.items():
        text = text.replace(contraction, expanded)
    
    return text

def read_data():
    df = pd.read_csv(CSV_DATA_LOC)
    df['time_diff']  = df['end_time'] - df['start_time']
    df['sentence_length'] = df['transcript'].apply(lambda x: len(x.split()))
    df['t_uncontraction'] = df['transcript'].apply(lambda sentence: " ".join([expand_contractions(word) for word in sentence.lower().split()]))

    return df