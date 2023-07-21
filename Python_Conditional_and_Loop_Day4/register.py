def reg():
    print("<<<<<Register>>>>>")
    admin = input("enter your username")
    password = input("enter your password")
    age = input("enter age")
    gender = input("enter your gender")
    locality = input("enter your locality")

    print("<<<<<login Panel>>>>>")
    user = input("enter your username")
    passw = input("enter your password")
    if user==admin and passw==password:
        print("login success")
    else:
        print("fail")
reg()
