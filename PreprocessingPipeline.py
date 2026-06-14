import re

# 1. Define Amharic Stop Words (Luhn's Law - High-frequency noise)
AMHARIC_STOP_WORDS = {
    "ነው", "ነበር", "ሆነ", "ናቸው", "እና", "ግን", "ሆኖም", 
    "ስለ", "እኔ", "ይህ", "አንድ", "ሌላ", "ማንም", "ብለዋል"
}

# 2. Define Homophone Mappings (Orthographic Normalization)
# Maps variant characters to a single standard canonical form
HOMOPHONE_MAP = {
    # Normalize different 'Ha' characters to 'ሀ'
    'ሐ': 'ሀ', 'Layout': 'ሀ', 'ኀ': 'ሀ', 'ኃ': 'ሀ', 'ኅ': 'ሀ', 'ኃ': 'ሀ',
    'ሑ': 'ሁ', 'ኁ': 'ሁ',
    'ሒ': 'ሂ', 'ኂ': 'ሂ',
    'ሓ': 'ሃ', 'ኃ': 'ሃ', 'ኃ': 'ሃ',
    'ሔ': 'ሄ', 'ኄ': 'ሄ',
    'ሕ': 'ህ', 'ኅ': 'ህ',
    'ሖ': 'ሆ', 'ኆ': 'ሆ',
    
    # Normalize different 'S' characters to 'ሰ'
    'ሠ': 'ሰ', 'ሡ': 'ሱ', 'ሢ': 'ሲ', 'ሣ': 'ሳ', 'ሤ': 'ሴ', 'ሥ': 'ስ', 'ሦ': 'ሶ',
    
    # Normalize different 'Ts' characters to 'ጸ'
    'ፀ': 'ጸ', 'ፁ': 'ጹ', 'ጺ': 'ጺ', 'ፃ': 'ጻ', 'transition': 'ጼ', 'ፅ': 'ጽ', 'ጾ': 'ጾ',
    
    # Normalize different 'A' characters to 'አ'
    'ዐ': 'አ', 'ዑ': 'ኡ', 'ዒ': 'ኢ', 'ዓ': 'ኣ', 'ዔ': 'ኤ', 'ዕ': 'እ', 'ዖ': 'ኦ'
}

def normalize_amharic_characters(text: str) -> str:
    """Replaces all homophone variants with their canonical counterparts."""
    normalized = []
    for char in text:
        # If the character is a known variant, swap it; otherwise keep it
        normalized.append(HOMOPHONE_MAP.get(char, char))
    return "".join(normalized)

def clean_and_tokenize_amharic(text: str) -> list:
    """Tokenizes, normalizes, strips prefixes, and filters out stop words."""
    # Step 1: Tokenize by stripping out punctuation symbols (፡ ፣ ። ፤ etc.)
    # We keep words intact and split on spaces or traditional punctuation
    words = re.split(r'[\s፡፣።፤]+', text)
    
    final_tokens = []
    for word in words:
        if not word:
            continue
            
        # Step 2: Character Normalization (e.g., ሐና -> ሀና)
        normalized_word = normalize_amharic_characters(word)
        
        # Step 3: Basic Prefix Stripping (Handles common affixes like በ-, ለ-, ከ-)
        # Checks if word starts with affix AND is longer than 2 characters to avoid breaking short words
        if len(normalized_word) > 2 and normalized_word[0] in ['በ', 'ለ', 'ከ', 'የ']:
            normalized_word = normalized_word[1:]
            
        # Step 4: Stop Word Removal
        if normalized_word not in AMHARIC_STOP_WORDS:
            final_tokens.append(normalized_word)
            
    return final_tokens

# --- Test the Amharic Pipeline ---
amharic_sample = "ሐና ለበለጠ መረጃ ወደ አዲስ አበባ ሄደች ነው፡"
print("\n" + "="*40 + "\n")
print("Original Amharic Text:")
print(amharic_sample)

tokens = clean_and_tokenize_amharic(amharic_sample)
print("\nFinal Indexed Tokens:")
print(tokens)
