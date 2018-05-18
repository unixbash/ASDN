import pandas
import pickle
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.datasets import make_blobs
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

class Model:
    file=""
    names=""
    dataset=""
    array = ""
    X = []
    Y = []
    size = 0
    seed = 0
    modelFile=""

    def __init__(self):
        # Load dataset
        self.file = "ml/dataset.csv"
        self.names = ["cpu", "memory", "interfaces", "reachable-roots", "reachable-vlans", "wan-pps", "load", "wan-latency",
                 "class"]
        self.dataset = pandas.read_csv(self.file, names=self.names)
        self.array = self.dataset.values
        self.X = self.array[:, 0:8]
        self.Y = self.array[:, 8]
        self.size = 0.20
        self.seed = 7
        self.modelSave()

    #Get dataset averages
    def dataAvg(self):
        print(self.dataset.describe())

    #Box Plot Graph
    def boxPlot(self):
        self.dataset.plot(kind='box', subplots=True, layout=(2,4), sharex=False, sharey=False)
        plt.show()

    #Class Distribution
    def classDist(self):
        print(self.dataset.groupby('class').size())

    #Validate the Dataset
    def algoValidation(self):
        scoring = 'accuracy'
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=self.size, random_state=self.seed)

        #Check the following Algorithms
        models = []
        models.append(('LR', LogisticRegression()))
        models.append(('LDA', LinearDiscriminantAnalysis()))
        models.append(('KNN', KNeighborsClassifier()))
        models.append(('CART', DecisionTreeClassifier()))
        models.append(('NB', GaussianNB()))
        models.append(('SVM', SVC()))

        #Evaluate the above algoritms
        results = []
        names = []
        for name, model in models:
            kfold = model_selection.KFold(n_splits=10, random_state=self.seed)
            cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)
            msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(msg)

        # Compare Algorithms
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.boxplot(results)
        ax.set_xticklabels(names)
        plt.show()

    #Make predictions using the CART Algorithm
    def modelValidate(self):
        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=self.size,
                                                                                        random_state=self.seed)
        cart = DecisionTreeClassifier()
        cart.fit(X_train, Y_train)
        predictions = cart.predict(X_validation)
        print(accuracy_score(Y_validation, predictions))
        print(confusion_matrix(Y_validation, predictions))
        print(classification_report(Y_validation, predictions))

    #Saving the final model locally
    def modelSave(self):
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(self.X, self.Y, test_size=self.size,
                                                                            random_state=self.seed)
        model = DecisionTreeClassifier()
        model.fit(X_train, Y_train)
        # save the model to disk
        self.modelFile = 'model.sav'
        pickle.dump(model, open(self.modelFile, 'wb'))

    #Main predition function
    def predict(self, networkAttr):
        model = pickle.load(open(self.modelFile, 'rb'))
        result = model.predict(networkAttr)
        return result[0]


model = Model()
print(model.predict([["0.27","-0.8","0","1","0","17","0.21","11"]]))