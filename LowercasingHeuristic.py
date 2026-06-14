import re

def lowercase_sentence_start(text: str) -> str:
    # Split text into sentences using basic punctuation markers (. ! ?)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    processed_sentences = []
    
    for sentence in sentences:
        if not sentence.strip():
            continue
        # Split sentence into the first word and the rest of the text
        words = sentence.split(maxsplit=1)
        if words:
            # Lowercase only the first word
            words[0] = words[0].lower()
            processed_sentences.append(" ".join(words))
            
    return " ".join(processed_sentences)

# --- Test the heuristic ---
sample_text = "The car stopped. Kebede visited General Motors yesterday. Associated Press reported it."
print("Original Text:")
print(sample_text)
print("\nProcessed Text (Only sentence-starts lowercased):")
print(lowercase_sentence_start(sample_text))
