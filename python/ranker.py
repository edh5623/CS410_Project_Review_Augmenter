import metapy
import pytoml
import os

dataset_path = "review_docs/review_docs.dat"

def load_ranker():
    """
    Use this function to return the Ranker object to evaluate,
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    # metapy.index.OkapiBM25(1.7, 0.82, 10.0)
    # return metapy.index.JelinekMercer(0.611) # 0.34848639568697437
    # return metapy.index.PivotedLength(0.34800000000000003) # 0.3510384000155416
    # return metapy.index.OkapiBM25(1.2, 0.998, 500.0) # 0.3543020148774101
    # return metapy.index.OkapiBM25(2.4, 0.88, 500.0) # 0.36121066700657345
    # return metapy.index.OkapiBM25(1.7, 0.71, 500.0) # last one left in MP 2.1
    return metapy.index.OkapiBM25()

def rank(query, docs):
    write_dataset(docs)

    query_doc = metapy.index.Document()
    query_doc.content(query)  # query from AP news

    cfg = "config.toml"
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker()

    scores = ranker.score(idx, query_doc, 10)
    ranked_docs = [docs[score[0]-1] for score in scores]

    # Fix not working on command line
    print(scores)
    # TODO: Comment out to work on command line
    print(ranked_docs)

    return ranked_docs

def write_dataset(docs):
    if os.path.exists(dataset_path):
        os.remove(dataset_path)

    with open(dataset_path, 'a') as dataset_file:
        for review in docs:
            dataset_file.write(review + "\n")