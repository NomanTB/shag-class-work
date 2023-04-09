def helper(work):
    works = work

    def helper(work):
        return f"я помогу тебе {works}, и {work}"


    return helper


result = helper("homework")
# result = helper("homework")("clianing")

print(result("clianing"))
print(result("driving"))