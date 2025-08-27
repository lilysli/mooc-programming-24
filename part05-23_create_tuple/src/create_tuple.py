def create_tuple(x: int, y:int, z: int):
    t_list = [x,y,z]
    smallest = min(t_list)
    greatest = max(t_list)
    total = sum(t_list)
    return (smallest, greatest, total)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
