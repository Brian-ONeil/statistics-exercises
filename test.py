import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)


n_dice_per_experiment = ncols = 10
n_experiments = nrows = 100

data = np.random.randint(1, 7, (nrows, ncols))

data[:4]

