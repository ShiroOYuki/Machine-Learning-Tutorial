from sklearn import datasets

iris = datasets.load_iris()

it = iris["target"][(iris["target"] == 0)|(iris["target"] == 1)]

print(it)