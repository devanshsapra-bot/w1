def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

print(group([2,35,2,23,4,4,325,6,5,2,34,3,424],3))