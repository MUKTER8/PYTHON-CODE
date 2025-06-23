# Problem 40: Generics in Python
def print_array(array):
    for item in array:
        print(item)


def main():
    n = int(input("How many integers? "))
    int_array = [int(input("Enter integer: ")) for _ in range(n)]

    n = int(input("How many strings? "))
    string_array = [input("Enter string: ").strip() for _ in range(n)]

    print("Integer Array:")
    print_array(int_array)
    print("String Array:")
    print_array(string_array)


if __name__ == "__main__":
    main()
