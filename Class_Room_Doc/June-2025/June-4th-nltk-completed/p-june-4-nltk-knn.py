import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load dataset
dataset = pd.read_csv(r"./Restaurant_Reviews.tsv", sep='\t')

# Preprocess text
corpus = []
ps = PorterStemmer()
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# TF-IDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

#Use case KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=2)
classifier.fit(X_train, y_train)

# Predict test set results
y_pred = classifier.predict(X_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy
ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

# Bias and Variance
bias = classifier.score(X_train, y_train)
variance = classifier.score(X_test, y_test)
print("Bias (Train Accuracy):", bias)
print("Variance (Test Accuracy):", variance)

# ROC and AUC
probs = classifier.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, probs)
print("AUC:", auc)

fpr, tpr, _ = roc_curve(y_test, probs)

# Plot ROC
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - KNN")
plt.legend()
plt.grid(True)
plt.show()
