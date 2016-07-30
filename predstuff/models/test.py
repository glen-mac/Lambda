import pickle
import numpy as np

p = open('reg_baseline2.p', 'rb')
d = pickle.load(p)

d.predict(np.random.sample(35,))