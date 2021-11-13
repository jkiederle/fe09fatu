import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
    if resize:
        X = np.resize(X, resize)
    return X