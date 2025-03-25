import numpy as np
import pandas as pd
import scipy.optimize
import tqdm
import scipy

def chsh_sum(theta1, theta2, theta1prime, theta2prime):
    return -np.cos(theta1-theta2) - np.cos(theta1-theta2prime) - np.cos(theta1prime-theta2) + np.cos(theta1prime-theta2prime)

# thetas = np.linspace(0, np.pi, 30)

# rows = []
# for theta1 in tqdm.tqdm(thetas):
#     for theta2 in thetas:
#         for theta1prime in thetas:
#             for theta2prime in thetas:
#                 rows.append(
#                     {
#                         "theta1": theta1,
#                         "theta2": theta2,
#                         "theta1prime": theta1prime,
#                         "theta2prime": theta2prime,
#                         "sum": chsh_sum(theta1, theta2, theta1prime, theta2prime),
#                     }
#                 )

# result=pd.DataFrame(rows)
# result = result.sort_values("sum")
# print(result.head())
# result.to_csv("thetas.csv", index=False)


bounds = [(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi)]
first_guess = [1.4398966328953218,2.22529479629277,3.00692959690218,0.6544984694978735]

def fun_to_opt(x):
    chsh_sum(x[0], x[1], x[2], x[3])

result = scipy.optimize.minimize(fun_to_opt, first_guess, bounds=bounds, method="BFGS")

print(result)