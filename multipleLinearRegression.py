" Created by Ecem Balıkçı on 11/21/2020 at 1:56 PM (Contact: balikciecem@gmail.com) "

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

    for a in csv_list:
        if a != csv_list[0]:  # to avoid the first row (Player No, Country, Name...)

            exp_list = np.append(exp_list, int(a[6]))
            salary_list = np.append(salary_list, int(a[8]))
            age_list = np.append(age_list, int(a[4]))
            pow_list = np.append(pow_list, float(a[7]))
            one_list = np.append(one_list, 1)

X = np.column_stack((one_list, age_list, exp_list, pow_list))
xt = np.transpose(X)
xtx = np.dot(xt, X)
xty = np.dot(xt, salary_list)
xtx_inv = np.linalg.inv(xtx)
beta = np.dot(xtx_inv, xty)

# working alternative:
# coefficents = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)

y_est = X.dot(beta)  # 𝒚̂=𝑿𝜷̂
u = abs(salary_list-y_est)  # |𝒖̂|=|𝒚−𝒚̂|


def simlin_plot(x, y):
    plt.scatter(x, y, c="c")
    plt.xlabel("Estimated Salary Values(y_est)")
    plt.ylabel("Errors(u)")
    plt.title("Residual Error Plot")
    plt.show()


simlin_plot(y_est, u)


def calculateRsquare(a, b):  # a=salary_list b=estimated y values(y_est)

    avg_a = sum(a)/len(a)
    rss = 0
    tss = 0
    for i in range(len(salary_list)):
        rss += np.square(a[i]-b[i])
        tss += np.square(a[i]-avg_a)
    rsquarescore = 1 - (rss/tss)

    print("r^2 score: ", rsquarescore)

    return rsquarescore


print("Showing original results:")
r1 = calculateRsquare(salary_list, y_est)


random_list = np.random.randint(-1000, 1000, len(salary_list))
X = np.column_stack((X, random_list))

xt_2 = np.transpose(X)
xtx_2 = np.dot(xt_2, X)
xty_2 = np.dot(xt_2, salary_list)
xtx_inv_2 = np.linalg.inv(xtx_2)
beta_2 = np.dot(xtx_inv_2, xty_2)
y_est_2 = X.dot(beta_2)
u_2 = abs(salary_list-y_est_2)

print("Showing results with an added random column:")
r2 = calculateRsquare(salary_list, y_est_2)

