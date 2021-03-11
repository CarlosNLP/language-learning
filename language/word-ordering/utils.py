import random

# Method to create a shuffled sentence
def generator(sentence_tokenized):
    """
    Input:
    sentence_tokenized: list of words representing a sentence

    Output:
    Tuple consisting of 2 elements: shuffled sentence (list of words) and original sentence (list of words)
    """
    original_sentence = sentence_tokenized.copy()
    random.shuffle(sentence_tokenized)
    
    return (sentence_tokenized, original_sentence)
