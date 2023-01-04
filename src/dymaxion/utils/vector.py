def distance(v1, v2=ORIGIN):
    """
    return distance between two vectors
    """
    return np.linalg.norm(v1-v2)


def midpoint(v1, v2):
    """
    return midpoint between two vectors
    """
    v = (v1 + v2)
    mp = v/np.linalg.norm(v)
    return mp