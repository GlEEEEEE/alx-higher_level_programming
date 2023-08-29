#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False


if __name__ == "__main__":
    value = 12345  # Replace with any integer value
    result = safe_print_integer(value)
    if result:
        print("Integer printed successfully")
    else:
        print("Failed to print integer")
