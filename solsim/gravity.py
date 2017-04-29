import numpy as np
from astropy import constants as c

def universal_gravity(m1, m2, r, G=c.G.value):
    """
    Calculate the force between two objects of mass m1, m2, separated 
    by r. 
    
    Newton's universal law of gravity.
    
    Parameters
    ----------
    m1 : float or numpy array
        mass of object 1 
    m2 : float or numpy array
        mass of object 1
    r  : float or numpy array
        
    Returns
    -------
    float or numpy array
        The force between two objects.
    """
    return G * (m1 * m2) / r**2