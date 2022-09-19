import sys


# def calculate_geometric_series(a, r, n=10):
#     """Calculate the sum of a geometric series"""
#     if r == 1:
#         return a * (n + 1)
#     return a * (1 - r ** (n + 1)) / (1 - r)

def find_max(list):
    maximum = None
    first = False
    for value in list:
        if first == False:
            maximum = value
            first = True
        if value > maximum:
            maximum = value

    return maximum


def main():
    #a = int(input("a: "))
    #r = float(input("r: "))
    #n = int(input("n: "))
    #print(f"s_n = {calculate_geometric_series(a, r, n)}")
    my_list = [1, 7, 9, 42]
    my_max = find_max(my_list)
    print(my_max)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#Can use flowcharts to cleanly show functions purpose / workflow

