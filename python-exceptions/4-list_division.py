#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_lenght):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("Wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
            if i == list_lenght - 1:
                return new_list
