import random
import sys


def double_number(n):
    return 2 * n



def dict_to_squared_dict(input_dict):
    result_dict = dict()
    for key, value in input_dict.items():
        result_dict[key] = value ** 2
    return result_dict



def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")


def main():
    #using_map()
    #using_map_and_lambda()
    #using_filter()
    my_dict = {"one": 1, "two": 2}
    sq_dict = dict_to_squared_dict(my_dict)
    print(f"{dict_to_squared_dict(my_dict) = }")
    filtered_dict = filter(lambda v: 70 < v < 100, sq_dict.values())

    return 0


if __name__ == '__main__':
    sys.exit(main())
