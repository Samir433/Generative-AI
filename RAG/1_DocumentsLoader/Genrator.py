def id_generator():
    counter = 0
    while True:
        yield counter
        counter += 1
    
id_gen = id_generator()

for i in range(10):
    print(next(id_gen), end=" ")







