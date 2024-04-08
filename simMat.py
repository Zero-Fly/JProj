from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

hash = HashingVectorizer(lowercase=True, stop_words={'english'}, ngram_range=(1,1))
cv = CountVectorizer(stop_words='english', lowercase=True)
tfid = TfidfVectorizer()

#TF-IDF Vectorizer
vectorTfid = tfid.fit_transform(data['tags']).toarray()
similarityTfidfVect = cosine_similarity(vectorTfid)

#Count Vectorizer
vector = cv.fit_transform(data['tags']).toarray()
similarityCountVect = cosine_similarity(vector)

#Hashing Vectorizer
vectorHash = hash.fit_transform(data['tags']).toarray()
similarityHashingVect = cosine_similarity(vectorHash)