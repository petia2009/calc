def check(numb1, numb2):
    try:
        numb1 = int(numb1)
        numb2 = int(numb2)
    except:
        main()

def plus(numb1, numb2):
    print(int(numb1) + int(numb2))

def Xplus(numb1, numb2):
    print(int(numb1) - int(numb2))

def doublee(numb1, numb2):
    print(int(numb1) * int(numb2))

def Xdouble(numb1, numb2):
    print(int(numb1) / int(numb2))

def main():
    played = True
    while played:
        num1 = input("num 1: ")
        num2 = input("num 2: ")
        check(num1, num2)
        print("Дейсвия: ")
        print("""1. сложение
2. вычитание
3. умножение
4. деление""")
        todo = int(input("todo:  "))
        if todo not in "1 2 3 4".split():
            played = False

        if todo == 1:
            plus(num1, num2)

        if todo == 2:
            Xplus(num1, num2)

        if todo == 3:
            doublee(num1, num2)

        if todo == 4:
            Xdouble(num1, num2)

    else:
        print("Again?(y or yes)")
        again = input()
        if again != "y" or again != "yes":
            played = False
        if again == "yes" or again == "y":
            main()

main()