from t4_functions.function_types import (
    function_1, function_2, function_3, function_4, function_5,
    function_6, function_7, function_8
)

if __name__ == '__main__':
    # function_4(3712989, name="Ali", sub1=23, sub2=23, father_name="Tariq")
    # function_5(12367, "ALi", "Tariq")
    # function_5(12367, "ALi", "Tariq", 1, 2, 3, 4)
    # function_6(90, 20, 30, 40, 90, name="Ikram", rollno=3618, fathername="AmirZada")
    # function_7("A", 289)
    # function_7("B", 239, "MPS")
    # function_7("C", 259)

    memory, value = function_8()
    if memory == id(value):
        print("SAME")
        print(id(value))
        print(memory)
    else:
        print(id(value))
        print(memory)
        print("Different")
