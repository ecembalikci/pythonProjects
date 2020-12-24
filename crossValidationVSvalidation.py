" Created by Ecem Balıkçı on 12/6/2020 at 9:13 PM (Contact: balikci8ecem@gmail.com) "
import numpy as np
import csv
import matplotlib.pyplot as plt

exp_list = np.array([])
salary_list = np.array([])
age_list = np.array([])
one_list = np.array([])
pow_list = np.array([])

with open("team_big.csv") as f:
    csv_list = list(csv.reader(f))

    for e in csv_list:
        if e != csv_list[0]:  # to avoid the first row (Player No, Country, Name...)

            exp_list = np.append(exp_list, int(e[6]))
            salary_list = np.append(salary_list, int(e[8]))
            age_list = np.append(age_list, int(e[4]))
            pow_list = np.append(pow_list, float(e[7]))
            one_list = np.append(one_list, 1)

X = np.column_stack((one_list, age_list, exp_list, pow_list))
y = salary_list


def k_fold_cv(X, y, k):
    fold_size = round(len(y) / k)
    cv_hat = np.array([])
    idx = 0  # to see the i's last value
    for i in range(0, len(y) - fold_size, fold_size):
        X_test = X[i:i + fold_size]
        y_test = y[i:i + fold_size]

        X_train = np.delete(X, range(i, i + fold_size), 0)  # 0 row 1 column
        y_train = np.delete(y, range(i, i + fold_size), 0)

        reg_coefficents = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

        y_hat = np.dot(X_test, reg_coefficents)
        cv_hat = np.append(cv_hat, y_hat)

        idx += fold_size

    X_test = X[idx:len(X)]
    y_test = y[idx:len(X)]

    X_train = np.delete(X, range(idx, len(y)), 0)  # 0 row 1 column
    y_train = np.delete(y, range(idx, len(y)), 0)

    reg_coefficents = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

    y_hat = np.dot(X_test, reg_coefficents)
    cv_hat = np.append(cv_hat, y_hat)

    mse = np.mean(np.square(cv_hat - y))

    return mse


def validation(X, y):
    first20 = round(len(X) * 20 / 100)  # ratio and proportion shows the 20% of data is 7.8, had to round it.

    val_hat = np.array([])

    X_test = X[:first20]
    y_test = y[:first20]

    X_train = np.delete(X, range(0, first20), 0)  # 0 row 1 column
    y_train = np.delete(y, range(0, first20), 0)

    r_coefficents = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

    y_hat = np.dot(X_test, r_coefficents)  # the estimations are found

    val_hat = np.append(val_hat, y_hat)

    mse = np.mean(np.square(val_hat - y_test))  # y_test is used to test the accuracy of the estimations

    return mse


val_errors = np.array([])
cv_errors = np.array([])
for i in range(5):
    merged = np.column_stack((X, y))
    np.random.shuffle(merged)  # shuffled the data(ex:row 1 of 𝑋 is moved to row 5,element 1 of y moved to 5th position)
    # separate new X and y
    new_X = merged[:, 0:4]  # new_X = merged[:, 0:-1]
    new_y = merged[:, 4]  # new_y = merged[:, np.size(merged, 1)-1] or new_y = merged[:, -1]
    cv_errors = np.append(cv_errors, k_fold_cv(new_X, new_y, 5))  # added error calculations in functions to arrays
    val_errors = np.append(val_errors, validation(new_X, new_y))

arr = [0, 1, 2, 3, 4]
exact_x = [1, 2, 3, 4, 5]  # to have exact numbers on x-axis. if I don't use xticks()the x-axis would be 1,1.5,2,2.5..
plt.xticks(arr, exact_x)
plt.plot(arr, cv_errors, c='m')  # combination of colors looked nice, no other reason to set the color.
plt.plot(arr, val_errors, c='c')
plt.title("Cross-validation vs Validation")
plt.xlabel("Shuffle number")
plt.ylabel("Mean squared error")
plt.legend(["Cross-Validation", "Validation"])
plt.show()

# instead of using xticks that should be enough:
# plt.plot(np.linspace(1,5,5),cv_errors,"c", label='Cross validation'
# but in this case our numbers will be 1,1.5,2,2.5...
# simply add plt.xticks([1,2,3,4,5])
