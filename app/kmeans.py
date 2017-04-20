import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_20newsgroups

def cluster(clusters):
    all_json = list()

    for offset in range(0, 10):
        r = requests.get('http://newsr.me/api/articles?offset=' + str(offset * 10))
        all_json += r.json()
        descriptions = list()

    for article in all_json:
        id = article['id']
        description = article['title']
        descriptions.append(description)

    newsgroups_train = fetch_20newsgroups(subset='train')

    train_sentences = list(newsgroups_train) + descriptions

    tfidfvectorizer = TfidfVectorizer()

    X_train = tfidfvectorizer.fit_transform(train_sentences)
    X_test = tfidfvectorizer.transform(descriptions)

    kmeans = KMeans(n_clusters=clusters, random_state=1234)
#    kmeans = KMeans(n_clusters=clusters)
    kmeans.fit(X_train)
    results = list(kmeans.predict(X_test))

    tuples = zip(results, descriptions)
    tuples = sorted(tuples, key=lambda x: x[0])

    return tuples
