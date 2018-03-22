import sys

args = sys.argv[1:]


def greet_user(username_list):
    print(args[0:])
    print(args[1:])
    print(args[2:])
    print(args[3:])
greet_user(args)


