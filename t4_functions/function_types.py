
def function_1():
    """
    function      -> 1
    result/return -> void
    info/args     -> void
    NOTE          -> This is type 1 function with no return and no arguments
    """
    print("I am function one")


def function_2(name, roll_no):
    """
    function      -> 2
    result/return -> void
    info/args     -> yes
    NOTE          -> This is type 1 function with no return and with arguments
    """
    print("First 1| name:", name, "roll no:", roll_no)
    print("First 2| name: {} roll no: {}".format(name, roll_no))
    print(f"First 3| name: {name} roll no: {roll_no}")


def function_3():
    """
    function      -> 2
    result/return -> yes
    info/args     -> void
    NOTE          -> This is type 3 function with return and no arguments
    """
    return 2**4


def function_3():
    """
    function      -> 2
    result/return -> yes
    info/args     -> void
    NOTE          -> This is type 3 function with return and no arguments
    """
    return 2**4


def function_4(roll_no, name, father_name, sub1, sub2):
    """
    function      -> 2
    result/return -> yes
    info/args     -> void
    NOTE          -> This is type 3 function with return and no arguments
    """
    print(
        f"""
        RollNo       : {roll_no}
        Name         : {name}
        Father Name  : {father_name}
        Subject 1    : {sub1}
        Subject 2    : {sub2}
        Total        : {sub1+sub2}
        """
    )
    return sub2+sub1


def function_5(roll_no, name, father_name, *args):
    """
    function      -> Arbitrary Arguments
    NOTE          -> This is type 3 function with return and no arguments
    """
    total_marks = 100 * len(args)
    gained_marks = 0
    for x in args:
        gained_marks += x
    print("TOTAL  :", total_marks)
    print("GAINED :", gained_marks)


def function_6(*args, **kwargs):
    """
    function      -> Arbitrary Keyword Arguments
    NOTE          -> This is type 3 function with return and no arguments
    """
    total_marks = 100 * len(args)
    gained_marks = 0

    for x in args:
        gained_marks += x

    print("________INFO________")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print()
    print(
        f"""_________ MARKS__________
TOTAL SUBJECTS :{len(args)}
TOTAL MARKS    :{total_marks}
GAINED MARKS   :{gained_marks}
"""
    )


def function_7(name, roll_no, school="Garrison"):
    print(name)
    print(school)


def function_8():
    x = 10
    return id(x), x

