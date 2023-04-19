def checker(function):
    def checker(*args,**kwargs):
        try:
            result = function( *args,**kwargs)
        except Exception as exc:
            print(f"We have problem {exc}")
        else:
            print(f"No problem {result}")
    return checker

@checker
def calc(exp):
    return eval(exp)


calc("2+2")







# def fun(funk):
#
#     def initer(*args):
#         print("h1")
#         funk(*args)
#         print('h1')
#     return initer
# def pink(funk):
#
#     def initer(*args):
#         print("bul")
#         funk(*args)
#         print('bul')
#     return initer
#
# @fun
# @pink
# def puk(name,surname):
#     print('Roma ',name,surname)
#
#
# # puk = pink(fun(puk))
# puk("er","Todfsfp")