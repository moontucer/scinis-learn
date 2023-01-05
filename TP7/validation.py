import numpy as np
from random import randrange

def split(data, p = 0.2):
    training = list(data)
    validation = list()
    m = len(data)
    k = int(m * p)
    for i in range(k):
        ind = randrange(len(training))
        validation.append(training.pop(ind))
    return np.asarray(training), np.asarray(validation)