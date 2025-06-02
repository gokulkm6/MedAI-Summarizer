from transformers import pipeline

summarizer = pipeline("summarization", model="models/bart-large-cnn", tokenizer="models/bart-large-cnn")

def generate_summary(text, max_length=300):
    if len(text) < 10:
        return "Text too short for summarization."
    
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    
    return summary[0]['summary_text']