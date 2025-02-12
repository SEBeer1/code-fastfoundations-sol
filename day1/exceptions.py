import sys

#Premise of handling exceptions
#   try:
#       <statement?
#   excelpt:
#       <handle exception>
#   else:
#       <handle no exception>

#not a number
#complex
#not empty

#map efficient way as it doens't put the data into memory


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)


def main():
    try:
        a = int(input("a: "))
    except ValueError:
        print(f"Invalid value for a; defaulting to a=1...", file=sys.stderr)
        a = 1
    r = float(input("r: "))
    try:
        assert isinstance(r, float)
        #assert typre(r) == float
    except AssertionError:
        raise ValueError("invalid input for r")
        return 1

    n = int(input("n: "))
    try:
        assert n >= 1
    except AssertionError:
        raise ValueError(f"Invalid value for n; default to n=10...")
    else:
        print(f"s_{n} = {calculate_geometric_series(a, r, n=n)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
