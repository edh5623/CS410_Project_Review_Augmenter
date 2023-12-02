"""
NLP functions for pre-processing, ranking, and sentiment scoring of text.
"""

import rank_bm25 as bm
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()


def preprocess_doc(document):
    tokenized = word_tokenize(document)

    stop_words = set(stopwords.words("english"))
    stemmer = PorterStemmer()

    preprocessed = []

    for word in tokenized:
        if word not in stop_words:
            preprocessed.append(stemmer.stem(word))

    return preprocessed


def rank(query, docs):
    tokenized_corpus = [preprocess_doc(doc) for doc in docs]

    bm25 = bm.BM25Okapi(tokenized_corpus, k1=1.7, b=0.71)
    tokenized_query = query.split(" ")

    top = bm25.get_top_n(tokenized_query, docs, n=90)
    return top


def sentiment(doc):
    preprocessed = " ".join(preprocess_doc(doc))
    return sentiment_analyzer.polarity_scores(preprocessed)["compound"]


##########################################
# Metapy implementation below with bugs. Saved for future investigation.
##########################################
# import metapy
# import pytoml
# import os
#
# dataset_path = "review_docs/review_docs.dat"
#
# def load_ranker():
#     """
#     Use this function to return the Ranker object to evaluate,
#     The parameter to this function, cfg_file, is the path to a
#     configuration file used to load the index.
#     """
#     # metapy.index.OkapiBM25(1.7, 0.82, 10.0)
#     # return metapy.index.JelinekMercer(0.611) # 0.34848639568697437
#     # return metapy.index.PivotedLength(0.34800000000000003) # 0.3510384000155416
#     # return metapy.index.OkapiBM25(1.2, 0.998, 500.0) # 0.3543020148774101
#     # return metapy.index.OkapiBM25(2.4, 0.88, 500.0) # 0.36121066700657345
#     # return metapy.index.OkapiBM25(1.7, 0.71, 500.0) # last one left in MP 2.1
#     return metapy.index.OkapiBM25()
#
# def rank(query, docs):
#     write_dataset(docs)
#
#     query_doc = metapy.index.Document()
#     query_doc.content(query)  # query from AP news
#
#     cfg = "config.toml"
#     idx = metapy.index.make_inverted_index(cfg)
#     ranker = load_ranker()
#
#     scores = ranker.score(idx, query_doc, 10)
#     ranked_docs = [docs[score[0]-1] for score in scores]
#
#     # Fix not working on command line
#     print(scores)
#     print(ranked_docs)
#
#     return ranked_docs
#
# def write_dataset(docs):
#     if os.path.exists(dataset_path):
#         os.remove(dataset_path)
#
#     with open(dataset_path, 'a') as dataset_file:
#         for review in docs:
#             dataset_file.write(review + "\n")
