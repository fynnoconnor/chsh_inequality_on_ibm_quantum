import numpy as np
import pandas as pd
# import scipy.optimize
import scipy

def chsh_sum(theta1, theta2, theta1prime, theta2prime):
    return -np.cos(theta1-theta2) - np.cos(theta1-theta2prime) - np.cos(theta1prime-theta2) + np.cos(theta1prime-theta2prime)




bounds = [(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi)]
# first_guess = [1.4398966328953218,2.22529479629277,3.00692959690218,0.6544984694978735]
first_guess = [np.pi,np.pi,0,0]

def fun_to_opt(x):
    return -chsh_sum(x[0], x[1], x[2], x[3])

result = scipy.optimize.minimize(fun_to_opt, first_guess, bounds=bounds)

print(result)

from scipy.optimize import basinhopping, differential_evolution

# Option A: basinhopping
def fun_neg(x):
    return -chsh_sum(x[0], x[1], x[2], x[3])  # so we can "maximize" the CHSH sum

x0 = [np.pi, np.pi, 0, 0]
minimizer_kwargs = {"bounds": bounds, "method": "L-BFGS-B"}
result_basin = basinhopping(fun_neg, x0, minimizer_kwargs=minimizer_kwargs)
print(result_basin)

# Option B: differential_evolution
# (directly on fun_neg, no need for an initial guess)
result_de = differential_evolution(fun_neg, bounds)
print(result_de)


# thetas = np.linspace(0, np.pi, 30)
# import tqdm

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