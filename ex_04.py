def make_payment(p):
    limit = 1000
    if p < 20 or p > limit:
        print("Повторите попытку")
    else:
        print("Успех")


p = int(input())
make_payment(p)