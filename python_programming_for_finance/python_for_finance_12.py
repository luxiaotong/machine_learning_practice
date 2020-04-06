from python_for_finance_11 import extract_featuresets
from sklearn.model_selection import train_test_split
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from collections import Counter


def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25)
    # clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier(
        [('lsvc', svm.LinearSVC()), ('knn', neighbors.KNeighborsClassifier()), ('rfor', RandomForestClassifier())])
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print("Accuracy: ", confidence)
    prediction = clf.predict(X_test)
    print("Predicted spread: ", Counter(prediction))


do_ml('BAC')
