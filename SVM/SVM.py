import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')

print(dataset)

X = dataset.iloc[:, 2:-1]
y = dataset.iloc[:, -1]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)

classifier.fit(X_train, y_train)

y_predict = classifier.predict(X_test)

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
print(accuracy_score(y_test, y_predict))
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))