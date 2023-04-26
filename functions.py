
import numpy as np
from collections import Counter

def tokenize(document):
    # Simple tokenizer that splits on spaces and removes punctuation
    return [token.strip('.,;:!?') for token in document.lower().split()]

def my_CountVectorizer(docs):
    # Create a vocabulary from the tokenized documents
    vocab = sorted(set(token for doc in docs for token in tokenize(doc)))
    vocab_index = {word: i for i, word in enumerate(vocab)}
    
    # Create the document-term matrix
    dtm = np.zeros((len(docs), len(vocab)), dtype=int)
    for i, doc in enumerate(docs):
        for word, count in Counter(tokenize(doc)).items():
            dtm[i, vocab_index[word]] = count
    return dtm


def my_LatentDirichletAllocation(dtm, n_topics=10, max_iter=10):
    n_docs, n_words = dtm.shape
    
    # Initialize the topic-word distribution randomly
    topic_word_dist = np.random.rand(n_topics, n_words)
    
    # Normalize the rows of the topic-word distribution
    topic_word_dist /= topic_word_dist.sum(axis=1)[:, np.newaxis]
    
    # Initialize the document-topic distribution randomly
    doc_topic_dist = np.random.rand(n_docs, n_topics)
    
    # Normalize the rows of the document-topic distribution
    doc_topic_dist /= doc_topic_dist.sum(axis=1)[:, np.newaxis]
    
    for _ in range(max_iter):
        # Update the document-topic distribution
        doc_topic_dist = (dtm[:, np.newaxis, :] * topic_word_dist[np.newaxis, :, :]).sum(axis=2)
        
        # Normalize the rows of the document-topic distribution
        doc_topic_dist /= doc_topic_dist.sum(axis=1)[:, np.newaxis]
        
        # Update the topic-word distribution
        topic_word_dist = (dtm[:, np.newaxis, :] * doc_topic_dist[:, :, np.newaxis]).sum(axis=0)
        
        # Normalize the rows of the topic-word distribution
        topic_word_dist /= topic_word_dist.sum(axis=1)[:, np.newaxis]
    
    return doc_topic_dist

# Example usage:
docs = ["I like apples", "I like bananas", "I like apples and bananas"]
dtm = my_CountVectorizer(docs)
# print(dtm)
doc_topic_dist = my_LatentDirichletAllocation(dtm)
print(doc_topic_dist)
