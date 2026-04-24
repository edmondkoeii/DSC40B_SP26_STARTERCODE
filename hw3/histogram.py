def histogram(points, bins):
    """Efficiently computes a histogram.

    Assumes that both `points` and `bins` are sorted in ascending order to
    avoid looping through all bins for each point.

    """
    n = len(points)
    densities = []
    
    point_idx = 0  # single pointer, never resets between bins
    
    for (a, b) in bins:
        count = 0
        width = b - a
        
        # count points in [a, b) by advancing the pointer
        while point_idx < n and points[point_idx] < b:
            count += 1
            point_idx += 1
        
        densities.append(count / (n * width))
    
    return densities
