import json
import pandas as pd
import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def generate_course_topics_csv(input_json='datacamp_courses_completed.json', output_csv='courses_topics.csv'):
    try:
        with open(input_json, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {input_json} not found.")
        return

    all_text = []
    for course in data:
        all_text.append(course.get('h1', ''))
        all_text.extend(course.get('h3s', []))
        all_text.extend(course.get('divs', []))

    full_text = " ".join(all_text)
    doc = nlp(full_text)

    overrides = {"datum": "data"}
    
    generic_terms = {
        "introduction", "basics", "course", "part", "congratulations", 
        "challenge", "concept", "summary", "final", "thought", "wrap",
        "exercise", "turn", "video", "lesson", "everything"
    }

    extracted_topics = []

    for chunk in doc.noun_chunks:
        clean_chunk = " ".join([
            overrides.get(t.lemma_.lower(), t.lemma_.lower()) 
            for t in chunk 
            if not t.is_stop and not t.is_punct and len(t.text) > 1
        ]).strip()
        
        if clean_chunk and clean_chunk not in generic_terms:
            extracted_topics.append(clean_chunk)

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and not token.is_punct:
            word = overrides.get(token.lemma_.lower(), token.lemma_.lower())
            if word not in generic_terms and len(word) > 2:
                extracted_topics.append(word)

    topic_counts = Counter(extracted_topics)
    df_topics = pd.DataFrame(topic_counts.items(), columns=["Topic", "Count"])
    
    df_topics = df_topics[df_topics["Count"] > 1] 
    df_topics = df_topics.sort_values(by="Count", ascending=False)

    df_topics.to_csv(output_csv, index=False)
    print(f"Generated {output_csv} with {len(df_topics)} unique topics.")

if __name__ == "__main__":
    generate_course_topics_csv()