import numpy as np
import scipy as sp

def find_stars(image):
    #
    # you wrote code previously to return x,y values for the stars in an image
    #
    # replace the following with your code:
    x,y = np.where(image>30)
    #
    return x,y
