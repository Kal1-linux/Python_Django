uname = "admin"
password = "admin"

u = input("enter uname:")
p = input("enter pass:")

if u==uname and p==password:
    print("Login successsfully")
    age = int(input("enetr age:"))
    if age>18:
        print("eligible for voting")
        nationality = input("Enter nationality:")
        if nationality == "indian":
            print("valid")
            print("select party for Voting")
            print("Congress")
            print("AAP")
            print("Others")
            party=input("Enter Party Name:")
            if party=="BJP":
                print("vote done for:",party)
            elif party=="CONGRESS":
                print("vote done for:",party)
            elif party == "AAP":
                print("vote done for:", party)
            elif party=="OTHERS":
                print("vote done for:",party)
            else:
                print("Enter Correct party name:)")
        else:
            print("not valid")
    else:
        print("not eligible for voting")
else:
    print("Login failed")