" Created by Ecem Balıkçı on 12/28/2020 at 8:30 PM (Contact: balikci8ecem@gmail.com) "
import numpy as np
import csv
import matplotlib.pyplot as plt

age_list = np.array([])
one_list = np.array([])
length_list = np.array([])

with open("Bluegill_dataset.csv") as f:  # extract and read the data from csv file
    bluegill_dataset = list(csv.reader(f))
    for a in bluegill_dataset:
        if a != bluegill_dataset[0]:
            age_list = np.append(age_list, int(a[0]))
            length_list = np.append(length_list, int(a[1]))
            one_list = np.append(one_list, 1)

x = age_list # our input value x is age data
y = length_list # our output value y is length data


def polynomial_regression(x, y, d):

    X = np.column_stack((one_list, age_list))
    for i in range(d-1):  # to skip first 2 columns
        arr = np.power(age_list, i+2)  # to skip 0, 1. start from ^2 then continue
        X = np.column_stack((X, arr))  # add every column to X

    reg_coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    y_hat = np.dot(X, reg_coefficients)
    return y_hat


poly_arr = list()
for i in range(1, 7):  # call 6 times, store the results
    poly_arr.append(polynomial_regression(x, y, i))


def calculate_r_square(a, b):
    avg_a = sum(a) / len(a)
    rss = 0
    tss = 0
    for c in range(len(a)):
        rss += np.square(a[c] - b[c])
        tss += np.square(a[c] - avg_a)

    r_square_score = 1 - (rss / tss)
    return r_square_score


for i in range(6):  # r^2 calculations for every degree
    call_r2 = calculate_r_square(y, poly_arr[i])
    if i == 0:
        print("The r^2 score for linear regression: ", format(call_r2, '.2f'))
    else:
        print("The r^2 score for", i, ". degree polynomial regression: ", format(call_r2, '.4f'))
    # format() allows us to set decimal numbers in our results. round() can be used too, but it ignores 0.
    # for ex: if your result is 0.8340234 format(result, '.4f') will make it 0.8340, round(result,4) will make it 0.834


sorted_loc = np.argsort(x)  # sorted locations of x(age)
matrix = np.column_stack((x, y, poly_arr[0], poly_arr[1], poly_arr[2], poly_arr[3], poly_arr[4], poly_arr[5]))
matrix = matrix[sorted_loc]  # sort matrix according to age's sorted locations
plt.scatter(x, y, c="k")
plt.plot(matrix[:, 0], matrix[:, 2], c="m")  # linear
plt.plot(matrix[:, 0], matrix[:, 5], c="r")  # 4th degree
plt.plot(matrix[:, 0], matrix[:, 6], c="c")  # 5th degree
plt.plot(matrix[:, 0], matrix[:, 7], c="b")  # 6th degree
plt.title("Polynomial Regression")
plt.xlabel("age of a bluegill fish")
plt.ylabel("length of a bluegill fish")
plt.legend(["linear", "4th degree", "5th degree", "6th degree"])
plt.show()
