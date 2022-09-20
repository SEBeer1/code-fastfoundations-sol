import sys


def plain_while():
    i = 0
    while i < 10:
        print(f"{i = }")
        i += 1


def complex_while():
    from my_functions import calculate_geometric_series

    while True:  # loop forever!
        a = int(input("a: "))
        r = float(input("r: "))
        n = int(input("n: "))
        s_n = calculate_geometric_series(a, r, n)
        print(f"{s_n = }")
        quit_ = input("to quit enter 'q': ")  # why do we use 'quit_' instead of 'quit'
        if quit_ == 'q':
            break


def loop_over_file():
    with open("paradoxical.txt") as f:
        while line := f.readline():
            print(f"{line = }")


def reverse_while():
    i = 9
    while i > -1 :
        print(i)
        i -= 1

def int_sum_l1000():
    int_list = []
    i = -12
    while True:
        int_list.append(i)
        i += 1
        if sum(int_list) + (i+1) > 1000:
            print(int_list)
            print(len(int_list))
            print(sum(int_list))
            break


def main():
    # plain_while()
    # complex_while()
    # loop_over_file()
    # reverse_while()
    int_sum_l1000()
    return 0


if __name__ == '__main__':
    sys.exit(main())
