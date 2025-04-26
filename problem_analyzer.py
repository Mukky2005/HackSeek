import spacy
import random
from textblob import TextBlob

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # If model isn't available, use a simpler pipeline
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("sentencizer")

def analyze_problem(problem_statement):
    """
    Analyze the problem statement using NLP techniques.
    
    Args:
        problem_statement (str): The problem statement text
        
    Returns:
        dict: A dictionary containing analysis results
    """
    # Process the text with spaCy
    doc = nlp(problem_statement)
    
    # Convert doc.sents to a list so we can reuse it
    sentences = list(doc.sents)
    
    # Extract entities
    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char
        })
    
    # Extract key phrases using noun chunks
    try:
        key_phrases = [chunk.text for chunk in doc.noun_chunks]
    except ValueError:
    # Fallback when dependency parser isn't available
        key_phrases = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    
    # Identify potential objectives (using verb phrases)
    objectives = []
    for sent in sentences:
        for token in sent:
            if token.pos_ == "VERB" and token.dep_ in ["ROOT", "advcl", "xcomp"]:
                # Get the verb phrase
                verb_phrase = " ".join([t.text for t in token.subtree])
                if len(verb_phrase.split()) > 2:  # Only consider longer phrases
                    objectives.append(verb_phrase)
    
    # If no objectives found using verb phrases, use sentences
    if not objectives:
        objectives = [sent.text for sent in sentences][:3]
    
    # Identify constraints (sentences with negation or modal verbs)
    constraints = []
    constraint_keywords = ["must", "should", "cannot", "can't", "limited", "constraint", 
                           "restriction", "only", "maximum", "minimum", "at least", "at most"]
    
    for sent in sentences:
        sent_text = sent.text.lower()
        if any(keyword in sent_text for keyword in constraint_keywords):
            constraints.append(sent.text)
        elif any(token.dep_ == "neg" for token in sent):
            constraints.append(sent.text)
    
    # If no constraints found, make educated guess
    if not constraints:
        for sent in sentences:
            for token in sent:
                if token.is_stop and token.text.lower() in ["but", "however", "though"]:
                    constraints.append(sent.text)
                    break
    
    # Get sentiment using TextBlob (ranges from -1 to 1)
    blob = TextBlob(problem_statement)
    sentiment = blob.sentiment.polarity
    
    # Calculate complexity based on sentence structure and length
    complexity = min(1.0, (
        len(problem_statement) / 500 +  # Length factor
        len(sentences) / 10 +           # Number of sentences
        len(entities) / 10 +            # Number of entities
        sum(1 for token in doc if token.dep_ in ["advcl", "ccomp", "xcomp"]) / 5  # Complex clauses
    ) / 4)
    
    # Return the analysis results
    return {
        "objectives": objectives[:5],  # Limit to top 5
        "constraints": constraints[:5],  # Limit to top 5
        "entities": entities,
        "key_phrases": key_phrases,
        "sentiment": sentiment,
        "complexity": complexity,
        "doc": doc,  # Include the spaCy doc for further processing (not JSON serializable)
        "text": problem_statement  # Original text
    }
