def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sucesion = [0, 1]
        while len(sucesion) < n:
            sucesion.append(sucesion[-1] + sucesion[-2])
        return sucesion
print(fibonacci(3))