import numpy as np
from gensim.models import word2vec

def model(X:list):
    """creates a word2vec model

    Args:
        X (list): list of tweets to be vectorized

    Returns:
        Word2Vec: vectorized word2vec
    """    
    sentences = [sentence.split() for sentence in X]
    return word2vec.Word2Vec(sentences, vector_size=100 , window=5, min_count=5, workers=4)



def vectorize(sentence,w2v_model):
    """vectorizes the given sentence with the given word2vec model

    Args:
        sentence (str): sentence to vectorize
        w2v_model (Word2Vec): the word2vec model vectorizer

    Returns:
        ndarray: the array of the word2vec vectors for the given sentence
    """    
    words = sentence.split()
    words_vecs = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    if len(words_vecs) == 0:
        return np.zeros(100)
    words_vecs = np.array(words_vecs)
    return words_vecs.mean(axis=0)

def Word2Vec_vector(X):
    """vectorizes the given list of tweets with a given word2vec model

    Args:
        X (list): list of tweets to be vectorized

    Returns:
        ndarray: vectorized list of tweets with a given word2vec model
    """    
    w2v_model=model(X)
    return np.array([vectorize(sentence,w2v_model) for sentence in X])
