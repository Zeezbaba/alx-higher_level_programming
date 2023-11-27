#!/usr/bin/python3

"""Function that multiplies two matrices using Numpy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the resulting matrix of the multiplication.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
