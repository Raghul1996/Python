def gen_n():
    yield 1
    yield 2
    yield 3

gen_1=gen_n()
print(next(gen_1))

