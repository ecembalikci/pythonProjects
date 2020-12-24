"""
Created by Ecem Balikci on 12/20/20. Contact: balikciecem@gmail.com
"""
import numpy as np
import csv

exp_list = np.array([])
salary_list = np.array([])
age_list = np.array([])
one_list = np.array([])
pow_list = np.array([])

with open("team_big.csv", encoding='Latin-1') as f:
    csv_list = list(csv.reader(f))
    for a in csv_list:
        if a != csv_list[0]:
            exp_list = np.append(exp_list, int(a[6]))
            salary_list = np.append(salary_list, int(a[8]))
            age_list = np.append(age_list, int(a[4]))
            pow_list = np.append(pow_list, float(a[7]))
            one_list = np.append(one_list, 1)

random_list = np.random.randint(-1000, 1000, len(exp_list))
X = np.column_stack((one_list, age_list, exp_list, pow_list, random_list))
y = salary_list


def adjusted_r2(y, y_hat, d):
    n = len(y)
    avg_y = sum(y) / len(y)
    rss = 0  # rss, tss = 0, 0
    tss = 0
    for i in range(len(y)):
        rss += np.square(y[i] - y_hat[i])
        tss += np.square(y[i] - avg_y)

    adj_r2 = 1 - ((rss / (n - d - 1)) / (tss / (n - 1)))
    return adj_r2


def calculate_r_square(a, b):  # a=y b=y_hat
    avg_a = sum(a) / len(a)
    rss = 0
    tss = 0
    for c in range(len(a)):
        rss += np.square(a[c] - b[c])
        tss += np.square(a[c] - avg_a)

    r_square_score = 1 - (rss / tss)
    return r_square_score


r_square_Results = np.array([])
adj_Results = np.array([])
deleted_indices = np.array([])

reg_coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
y_hat = np.dot(X, reg_coefficients)
adj_Results = np.append(adj_Results, adjusted_r2(y, y_hat, 4))  # m4 is calculated
# since there are 4 columns to be calculated in X (age, experience, power, random), d=4
# np.size(X,1) column sayısı 0 row sayısı
r = 5  # should be stored and decremented
d = 4

for e in range(1, 5):  # we have to calculate 4 more models: m0,m1,m2,m3
# for e in range(np.size(X,1)-1):
    #r2_max = 0
    for i in range(1, r): # for i in range(np.size(X,1)-1):
        X_copy = X  # added a variable named X_copy to temporarily delete the columns then restore back to original
        X_copy = np.delete(X_copy, i, 1)

        reg_coefficients = np.linalg.inv(X_copy.T.dot(X_copy)).dot(X_copy.T).dot(y)
        # you can define a function and put the calculations in there
        y_hat = np.dot(X_copy, reg_coefficients)

        r_square_Results = np.append(r_square_Results, calculate_r_square(y, y_hat))
        #r2_temp =  calculate_r_square(y, y_hat)
        #(if r2_temp>r2_max:
            # r2_max = r2_temp
            # index=i)
    r -= 1

    max_value = r_square_Results[0]  # since r^2 results are stored in an array I performed this in outer loop
    index = 0
    for i in range(len(r_square_Results)):
        if r_square_Results[i] > max_value:
            max_value = r_square_Results[i]
            index = i

    index += 1
    empty = np.array([])
    r_square_Results = empty  # clear r_square_Results in each iteration to calculate the max values in each step

    X = np.delete(X, index, 1)
    deleted_indices = np.append(deleted_indices, index)

    reg_coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    y_hat = np.dot(X, reg_coefficients)

    d -= 1
    adj_Results = np.append(adj_Results, adjusted_r2(y, y_hat, d))

print("The adjusted r^2 values for M4,M3,M2,M1 and M0 are, respectively:")
print(adj_Results)
