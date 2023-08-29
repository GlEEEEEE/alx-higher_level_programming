#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count


if __name__ == "__main__":
    my_list = [1, 2, 3, "Hello", 4, "World", 5]  # Replace with your list
    x = 7  # Replace with the number of elements to access
    count = safe_print_list_integers(my_list, x)
    print("Total integers printed:", count)
