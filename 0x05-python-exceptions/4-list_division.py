#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            val1 = my_list_1[i] if i < len(my_list_1) else 0
            val2 = my_list_2[i] if i < len(my_list_2) else 1

            if not (isinstance(val1, (int, float)) and isinstance(val2, (int, float))):
                print("wrong type")
                result.append(0)
            elif val2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(val1 / val2)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

    return (result)
