import pandas as pd
import spacy
from collections import Counter
import matplotlib.pyplot as plt
import os

nlp = spacy.load("en_core_web_sm")

INPUT_FILE = 'clean_crawl_data.csv' 
STORAGE_FILE = 'processed_topics.csv'    

def clean_chunk(chunk):
    """
    Standardizes noun chunks: removes noise and fixes the 'datum' issue.
    """
    exclude_list = {'jc', 'chouinard', 'guide', 'beginner', 'example', 'learn', 'access', 'request'}
    words = []
    for token in chunk:
        if token.is_stop or token.is_punct or len(token.text) <= 1:
            continue
            
        word = token.text.lower() if token.text.lower() == 'data' else token.lemma_.lower()
        
        if word not in exclude_list:
            words.append(word)
    
    return " ".join(words).strip()

def run_clean_report():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Please run your initial filter script first.")
        return

    df = pd.read_csv(INPUT_FILE)
    print(f"Processing {len(df)} clean HTML pages...")

    text_cols = ["Title 1", "Meta Description 1"]
    text_cols = [c for c in text_cols if c in df.columns]

    all_phrases = []

    for _, row in df.iterrows():
        text = " ".join([str(row[col]) for col in text_cols if pd.notnull(row[col])])
        doc = nlp(text)
        
        for chunk in doc.noun_chunks:
            cleaned = clean_chunk(chunk)
            if cleaned:
                all_phrases.append(cleaned)
    
    counts = Counter(all_phrases)
    
    df_topics = pd.DataFrame(counts.most_common(100), columns=['Topic', 'Count'])
    df_topics.to_csv(STORAGE_FILE, index=False)

    top_concepts = counts.most_common(100)
    if top_concepts:
        labels, values = zip(*top_concepts)
        labels, values = list(labels)[::-1], list(values)[::-1]

        plt.figure(figsize=(10, 8))
        plt.barh(labels, values, color='#27ae60') 
        plt.xlabel('Frequency Count')
        plt.title('Topic Analysis from Clean Crawl Data')
        plt.grid(axis='x', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    run_clean_report()


