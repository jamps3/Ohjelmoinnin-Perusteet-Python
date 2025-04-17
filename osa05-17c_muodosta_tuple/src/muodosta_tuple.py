def tee_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    largest = max(x, y, z)
    total = x + y + z
    return (smallest, largest, total)