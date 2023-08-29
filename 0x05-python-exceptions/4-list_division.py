#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            result = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list


if __name__ == "__main__":
    list1 = [10, 20, 30, 40]  # Replace
    list2 = [2, 0, 5, "a"]     # Replace
    length = 4                 # Replace
    result_list = list_division(list1, list2, length)
    print(result_list)
