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