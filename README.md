## Aims
This repo is used to compare the correlation function of two qubits prepared in an entangled state.

Additionally it measures the CHSH sum and thus invalidates the CHSH inequality. Proving the hidden variable theories cannot explain the quantum phenomena observed.

## Method

Here we use the IMB quantum computer and Qiskit to prepare an entangled state.


# Background

The CHSH inequality is essentially states the following:

https://latex.codecogs.com/svg.image?%5Csum=C(%5Ctheta%20_A,%5Ctheta%20_B)&plus;C(%5Ctheta'_A,%5Ctheta%20_B)&plus;C(%5Ctheta%20_A,%5Ctheta'_B)-C(%5Ctheta'_A,%5Ctheta'_B)

## Finding the optimal angles to maximise the CHSH sum
Uses the differential evolution (Storn & Price) to maximise the CHSH sum.

## Next steps
Other sources of uncertainty need to be quantified other than shot noise.

## Instructions to run this code yourself:
1. Clone the repo.
2. cd into the folder.
3. create a virtual environment: `python3 -m venv env` (may vary depending on your python installation)
4. Activate it: `source env/bin/activate`
5. Install dependancies `pip install -r requirements.txt`
You should then be able to run the IBM_Quantum.ipynb notebook. (Make sure you select the virtual environment created above as the kernel)

