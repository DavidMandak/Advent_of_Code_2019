def f():
    for i in range(2):
        yield


print(len(f()))
