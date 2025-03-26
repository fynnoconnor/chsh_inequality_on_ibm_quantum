import numpy as np
import scipy
from scipy.optimize import basinhopping, differential_evolution

# Sum we want to maximise
def theoretical_chsh_sum(theta1, theta2, theta1prime, theta2prime):
    return -np.cos(theta1-theta2) - np.cos(theta1-theta2prime) - np.cos(theta1prime-theta2) + np.cos(theta1prime-theta2prime)

def fun_to_opt(x):
    # so we can "maximize" the CHSH sum
    return -theoretical_chsh_sum(x[0], x[1], x[2], x[3])

if __name__ == "__main__":
        
    # Option A simple SciPy minimize
    bounds = [(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi),(-np.pi, np.pi)]
    first_guess = [np.pi,np.pi,0,0]

    result = scipy.optimize.minimize(fun_to_opt, first_guess, bounds=bounds)
    print("-------SciPy Optimise result----------")
    print(result)
    print("--------------------------------------")

    # Option A: basinhopping

    x0 = [np.pi, np.pi, 0, 0]
    minimizer_kwargs = {"bounds": bounds, "method": "L-BFGS-B"}
    result_basin = basinhopping(fun_to_opt, x0, minimizer_kwargs=minimizer_kwargs)
    print("-------SciPy basinhopping result----------")
    print(result_basin)
    print("------------------------------------------")

    # Option B: differential_evolution
    # (directly on fun_neg, no need for an initial guess)
    result_de = differential_evolution(fun_to_opt, bounds)
    print("-------SciPy Differential evolution result----------")
    print(result_de)
    print("----------------------------------------------------")
