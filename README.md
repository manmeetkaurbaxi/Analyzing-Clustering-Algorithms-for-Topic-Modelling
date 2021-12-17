# Analyzing Clustering Algorithms for Topic Modelling
I evaluate several techniques for document embeddings and clustering on the AG News dataset. Four different feature representations including Term Frequency-Inverse Document Frequency (TF-IDF), doc2vec, Bag of Words (BoW) and Sentence BERT are combined with four clustering techniques, i.e., k-means, Latent Dirichlet Allocation (LDA), Latent Semantic Indexing (LSI), and BERTopic to benchmark the dataset. Three different evaluation measures have been used to measure the performance of the topic clustering algorithms on news description, and the most appropriate extrinsic measure has been suggested for evaluation.

The results show that corpus based embedding: Bag of Words (BoW) outperforms the others, however, comparable results have been portrayed by transformer based embeddings: Sentence BERT, taking a fraction of time as compared to the top performer, Bag of Words (BoW).

## Dataset 
[AG News](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html)

## Analysis Pipeline
![](flowchart.png)

## Optimal number of epochs for document embeddings
![](optimal_epochs.png)

## Performance evaluation
![](performance_evaluation.png)
