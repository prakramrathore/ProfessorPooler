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

def assign_topic_probabilities(docs, topics):
    # Create a vocabulary from the topics
    vocab = sorted(set(word for topic in topics.values() for word in topic))
    vocab_index = {word: i for i, word in enumerate(vocab)}
    
    # Create the topic-word matrix
    topic_word_mat = np.zeros((len(topics), len(vocab)), dtype=int)
    for topic, words in topics.items():
        # print(f"topic: {topic}, words: {words}")
        for word in words:
            topic_word_mat[topic, vocab_index[word]] = 1
    
    # Normalize the rows of the topic-word matrix
    topic_word_mat = topic_word_mat / topic_word_mat.sum(axis=1)[:, np.newaxis]
    
    # Create the document-term matrix
    dtm = np.zeros((len(docs), len(vocab)), dtype=int)
    for i, doc in enumerate(docs):
        for word in tokenize(doc):
            if word in vocab_index:
                dtm[i, vocab_index[word]] += 1
    
    # Compute the document-topic probabilities
    doc_topic_prob = dtm @ topic_word_mat.T
    doc_topic_prob = doc_topic_prob / doc_topic_prob.sum(axis=1)[:, np.newaxis]
    
    return doc_topic_prob

# def assign_topic_probabilities(docs, topics, max_iter=100):
#     # Create a vocabulary from the topics
#     vocab = sorted(set(word for topic in topics.values() for word in topic))
#     vocab_index = {word: i for i, word in enumerate(vocab)}
    
#     # Create the topic-word matrix
#     # topic_word_mat = np.zeros((len(topics), len(vocab)), dtype=int)
#     topic_word_mat = np.random.rand(len(topics), len(vocab))
#     for topic, words in topics.items():
#         for word in words:
#             topic_word_mat[topic, vocab_index[word]] = 1
    
#     # Normalize the rows of the topic-word matrix
#     topic_word_mat = topic_word_mat / topic_word_mat.sum(axis=1)[:, np.newaxis]
    
#     # Create the document-term matrix
#     # dtm = np.zeros((len(docs), len(vocab)), dtype=int)
#     dtm = np.random.rand(len(docs), len(vocab))
#     for i, doc in enumerate(docs):
#         for word in tokenize(doc):
#             if word in vocab_index:
#                 dtm[i, vocab_index[word]] += 1
#     for _ in range(max_iter):
#         # Compute the document-topic probabilities
#         doc_topic_prob = dtm @ topic_word_mat.T
#         doc_topic_prob = doc_topic_prob / doc_topic_prob.sum(axis=1)[:, np.newaxis]
    
#     return doc_topic_prob

# Example usage:
topics = {
    0: ['language', 'text', 'nlp', 'processing'],
    1: ['vision', 'image', 'object', 'recognition'],
    2: ['algorithm', 'optimization', 'learning', 'model'],
    3: ['neural', 'network', 'deep', 'learning'],
    4: ['data', 'big', 'analytics', 'mining'],
    5: ['robotics', 'control', 'autonomous', 'system'],
    6: ['database', 'query', 'sql', 'transaction'],
    7: ['security', 'privacy', 'encryption', 'authentication'],
    8: ['software', 'engineering', 'testing'],
    9: ['web', 'cloud', 'distributed'],
}
# docs = ["Natural language processing is a subfield of linguistics", "Computer vision is an interdisciplinary field"]
# doc_topic_prob = assign_topic_probabilities(docs, topics)
# print(doc_topic_prob)