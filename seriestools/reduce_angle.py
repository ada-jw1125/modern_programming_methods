import math

def reduce_angle(angle):
    """
    Reduce x to a smaller equivalent angle r in [-pi/2, pi/2].

    Parameters
    ----------      
    angle : float
        Angle in radians.

    Returns
    -------
    q : int
        Quadrant index (integer multiple of pi/2).
    r : float
        Reduced angle in radians.  

    Notes
    -----
    Chosen interval: [-pi/2, pi/2] was selected because it ensures fast and stable convergence.      
    For very large |x|, no special correction is applied.
    """
    half_pi = math.pi / 2
    q = round(angle / half_pi)
    r = angle - q * half_pi
    
    # Avoid minor rounding errors.
    if r > half_pi:
        r = half_pi
    elif r < -half_pi:
        r = -half_pi    
    
    return q, r

# print(reduce_angle(0))  
# print(reduce_angle(math.pi))  
# print(reduce_angle(3 * math.pi / 2))
# print(reduce_angle(-3 * math.pi / 2))   
# print(reduce_angle(3 * math.pi / 4))