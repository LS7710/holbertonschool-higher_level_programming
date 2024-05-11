#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]  # Exclude the script name from the arguments list
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))

if __name__ == "__main__":
    main()
