def den(number,max_degree):
    for i in range(max_degree + 1):
        yield number ** i

res = den(2,10)

print(res)
for _ in res:
    print(_)



