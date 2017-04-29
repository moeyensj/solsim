import pytest
import numpy as np
from astropy import constants as c

from ..gravity import universal_gravity

def test_universal_gravity():
    # Test unit mass and radius
    assert universal_gravity(1, 1, 1) == c.G.value
    # Test zero separation case
    with pytest.raises(ZeroDivisionError):
        universal_gravity(1, 1, 0)