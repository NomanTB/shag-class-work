def test(*args,**kwargs):
    for el in args:
        print(el)
    for el in kwargs:
        print(el)

test(12,34,23,"ffsd")
print()
test(l=2)

