import re
import string
import random

def preprocess_text(text):
    """
    Preprocess text for NLP analysis.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Preprocessed text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    
    # Remove mentions (@username)
    text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags as symbols but keep the text
    text = re.sub(r'#(\w+)', r'\1', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def extract_keywords(text, top_n=10):
    """
    Extract keywords from text using simple frequency analysis.
    
    Args:
        text (str): Input text
        top_n (int): Number of top keywords to return
        
    Returns:
        list: Top keywords with their frequencies
    """
    # Preprocess text
    processed_text = preprocess_text(text)
    
    # Split into words
    words = processed_text.split()
    
    # Count word frequencies
    word_freq = {}
    for word in words:
        if len(word) > 3:  # Only consider words longer than 3 characters
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Return top n keywords
    return sorted_words[:top_n]

def calculate_text_complexity(text):
    """
    Calculate text complexity based on length, sentence structure, and vocabulary.
    
    Args:
        text (str): Input text
        
    Returns:
        float: Complexity score between 0 and 1
    """
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # If no valid sentences, return 0
    if not sentences:
        return 0
    
    # Calculate average sentence length
    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
    
    # Calculate vocabulary richness (unique words / total words)
    words = [word.lower() for sentence in sentences for word in sentence.split()]
    vocab_richness = len(set(words)) / max(len(words), 1)
    
    # Calculate complexity (normalized)
    complexity = (
        min(avg_sentence_length / 20, 1) * 0.5 +  # Sentence length factor (cap at 20 words)
        vocab_richness * 0.5                     # Vocabulary richness factor
    )
    
    return complexity

def generate_random_id():
    """
    Generate a random ID.
    
    Returns:
        str: Random ID
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
