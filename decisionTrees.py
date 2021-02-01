" Created by Ecem Balıkçı on 1/11/2021 at 7:16 AM (Contact: balikciecem@gmail.com) "
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeRegressor

exp_list = np.array([])
salary_list = np.array([])
age_list = np.array([])
pow_list = np.array([])
headers_arr = np.array([])
headers_array = np.array([])
with open("team_big.csv", encoding='Latin-1') as f:
    csv_list = list(csv.reader(f))
    for a in csv_list:
        if a == csv_list[0]:
            headers_arr = np.append(exp_list, csv_list[0])
            headers_array = np.append(headers_array, headers_arr[4])
            headers_array = np.append(headers_array, headers_arr[6])
            headers_array = np.append(headers_array, headers_arr[7])

        if a != csv_list[0]:
            exp_list = np.append(exp_list, int(a[6]))
            salary_list = np.append(salary_list, int(a[8]))
            age_list = np.append(age_list, int(a[4]))
            pow_list = np.append(pow_list, float(a[7]))

X = np.column_stack((age_list, exp_list, pow_list))
y = salary_list

x_train = X[:30]
y_train = y[:30]
x_test = X[30:]
y_test = y[30:]

reg_1 = DecisionTreeRegressor(random_state=0, max_depth=1)
reg_1.fit(x_train, y_train)
y_hat = reg_1.predict(x_test)
mse = np.mean(np.square(y_hat - y_test))
print("☘☘☘☘☘☘☘☘☘<<<<<<<<<<Results for Decision Tree 1>>>>>>>>>>☘☘☘☘☘☘☘☘")
print("MSE: ", mse)
print("The feature importances: ", reg_1.feature_importances_)
print()
titles = export_text(reg_1, feature_names=[headers_array[0], headers_array[1], headers_array[2]])
print(titles)

reg_2 = DecisionTreeRegressor(random_state=0, max_depth=3)
reg_2.fit(x_train, y_train)
y_hat_2 = reg_2.predict(x_test)
mse = np.mean(np.square(y_hat_2 - y_test))
print("☘☘☘☘☘☘☘☘☘<<<<<<<<<<Results for Decision Tree 2>>>>>>>>>>☘☘☘☘☘☘☘☘")
print("MSE: ", mse)
print("The feature importances: ", reg_2.feature_importances_)
print()
titles = export_text(reg_2, feature_names=[headers_array[0], headers_array[1], headers_array[2]])
print(titles)
# I don't know if its about the python/pycharm version but mine doesn't have feature_name.
# it has feature_names and doesn't accept headers_array directly, so I had to do it that way

reg_3 = DecisionTreeRegressor(random_state=0, max_depth=None)
reg_3.fit(x_train, y_train)
y_hat_3 = reg_3.predict(x_test)
mse = np.mean(np.square(y_hat_3 - y_test))
print("☘☘☘☘☘☘☘☘☘<<<<<<<<<<Results for Decision Tree 3>>>>>>>>>>☘☘☘☘☘☘☘☘")
print("MSE: ", mse)
print("The feature importances: ", reg_3.feature_importances_)
print()
titles = export_text(reg_3, feature_names=[headers_array[0], headers_array[1], headers_array[2]])
print(titles)


plt.plot([1, 15000, 25000], [1, 15000, 25000], c="lavender")
plt.scatter(y_test, y_hat, c="mediumpurple")
plt.scatter(y_test, y_hat_2, c="palevioletred")
plt.scatter(y_test, y_hat_3, c="mediumturquoise")
plt.title("Decision Trees: Predictions vs. Actual Values")
plt.xlabel("Actual Salary Values for Test Data")
plt.ylabel("Salary Predictions for Test Data")
plt.legend(["No-error line", "Decision Tree 1(Max depth: 1)",
            "Decision Tree 2(Max depth: 3)", "Decision Tree 3(Max depth: None)"])
plt.show()