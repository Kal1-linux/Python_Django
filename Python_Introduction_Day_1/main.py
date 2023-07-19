# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def client(User,Pass):
    # Use a breakpoint in the code line below to debug your script.
    print("client: "+User,Pass)  # Press Ctrl+F8 to toggle the breakpoint.

def admin(user,pas):
    print("admin: "+user,pas)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    User = input("enter username:")
    Pass = input("enter pass:")
    verify = 1
    if verify==1:
        admin(User,Pass)
    else:
        client(User,Pass)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
