"""
Created by Ecem Balikci on 2/2/21. Contact: balikci8ecem@gmail.com
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm


ace_1 = np.array([])
ace_2 = np.array([])
result = np.array([])

with open("Grand-slams-men-2013.csv", encoding='Latin-1') as f:
    csv_list = list(csv.reader(f))
    for a in csv_list:
        if a != csv_list[0]:
            ace_1 = np.append(ace_1, int(a[10]))
            ace_2 = np.append(ace_2, int(a[28]))
            result = np.append(result, int(a[3]))

X = np.column_stack((ace_1, ace_2))
y = result
x_train = X[:100]
x_test = X[100:]
y_train = y[:100]
y_test = y[100:]
linear = svm.SVC(kernel='linear')
polynomial = svm.SVC(kernel='poly')
radial = svm.SVC(kernel='rbf', gamma='auto')

linear.fit(x_train, y_train)
l_prediction = linear.predict(x_test)
ind_0_l = list()
ind_1_l = list()

# for linear predictions
for i in range(len(l_prediction)):
    if l_prediction[i]==0:
        ind_0_l.append(i)

    if l_prediction[i]==1:
        ind_1_l.append(i)

m1 = x_test[ind_0_l]
m2 = x_test[ind_1_l]
print(m1)
polynomial.fit(x_train, y_train)
p_prediction = polynomial.predict(x_test)
ind_0_p = list()
ind_1_p = list()
# for polynomial predictions
for i in range(len(p_prediction)):
    if p_prediction[i]==0:
        ind_0_p.append(i)

    if p_prediction[i]==1:
        ind_1_p.append(i)
m3 = x_test[ind_0_p]
m4 = x_test[ind_1_p]

radial.fit(x_train, y_train)
r_prediction = radial.predict(x_test)
ind_0_r = list()
ind_1_r = list()

# for radial predictions
for i in range(len(r_prediction)):
    if r_prediction[i]==0:
        ind_0_r.append(i)

    if r_prediction[i]==1:
        ind_1_r.append(i)

m5 = x_test[ind_0_r]
m6 = x_test[ind_1_r]

plt.figure(1)
plt.scatter(m1[:, 0], m1[:, 1], c="slateblue")
plt.scatter(m2[:, 0], m2[:, 1], c="plum")
plt.title("SVC with linear kernel")
plt.xlabel("Number of aces by Player 1")
plt.ylabel("Number of aces by Player 2")
plt.legend(["Prediction: 1st player won", "Prediction: 2nd player won"])
plt.figure(2)
plt.scatter(m3[:, 0], m3[:, 1], c="mediumslateblue")
plt.scatter(m4[:, 0], m4[:, 1], c="mediumturquoise")
plt.title("SVC with polynomial kernel")
plt.xlabel("Number of aces by Player 1")
plt.ylabel("Number of aces by Player 2")
plt.legend(["Prediction: 1st player won", "Prediction: 2nd player won"])
plt.figure(3)
plt.scatter(m5[:, 0], m5[:, 1], c="salmon")
plt.scatter(m6[:, 0], m6[:, 1], c="grey")
plt.title("SVC with radial kernel")
plt.xlabel("Number of aces by Player 1")
plt.ylabel("Number of aces by Player 2")
plt.legend(["Prediction: 1st player won", "Prediction: 2nd player won"])
plt.show()