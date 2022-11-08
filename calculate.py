import math                     # math functions
from functools import reduce    # to apply a particular function to all elements of the list to return a single value
import re                       # to use regular expressions (to analyze input)


def main() -> None:

    # key of operations that can be performed
    OPERATIONS = {
        "a": "ADDITION",
        "s": "SUBTRACTION",
        "m": "MULTIPLICATION",
        "d": "DIVISON",
        "p": "TO THE POWER OF",
        "v": "ABSOLUTE VALUE",
        "ru": "ROUND UP TO THE NEAREST INTEGER",
        "rd": "ROUND DOWN TO THE NEAREST INTEGER",
        "n": "NATURAL LOGARITHM",
        "2": "BASE-2 LOGARITHM",
        "10": "BASE-10 LOGARITHM",
        "l": "LEAST COMMON MULTIPLE",
        "g": "GREATEST COMMON DIVISOR",
        "q": "QUIT"
    }

    while True:

        # print heading, key of operations
        line("ARITHMETIC OPERATIONS CALCUATOR")
        for key, name in OPERATIONS.items(): print(f"{key} - {name}")
        line()

        while True:

            # user input operator to be used
            try:
                op = input("Enter operation: ")
                if op not in OPERATIONS.keys(): raise Exception
                break
            except: line("INVALID OPERATOR INCLUDED")

        # to end infinte loop, to end calculator program
        if op == "q":
            line("END OF CALCULATOR")
            break
        
        # print the operation to be performed
        line(OPERATIONS[op])

        # user input the number of operands
        while True:
            try:
                n = int(input("Number of inputs: "))
                if n < 1: raise Exception
                break
            except: line("NATURAL NUMBER REQUIRED")
        print()

        # user input a list of operands to be operated on
        nums = []
        for i in range(1, n + 1):
            while True:
                try:
                    num = float(input(f"Enter number {i}: "))
                    break
                except: line("NUMBER REQUIRED")
            nums.append(num)
        print()

        # if the result is a single number
        if op in ["a", "s", "m", "d", "p", "l", "g"]:

            res = (math.fsum(nums) if op == "a"
                else reduce(lambda a, b: a - b, nums) if op == "s"
                else reduce(lambda a, b: a * b, nums) if op == "m"
                else reduce(lambda a, b: a / b, nums) if op == "d"
                else reduce(math.pow, nums) if op == "p"
                else math.lcm(nums) if op == "l"
                else math.gcd(nums)) # If op == "g"

            # ask user if absolute (non-negative) value is required (single result)
            if res < 0 and ques("absolute value"): res = math.fabs(res)

            # ask user if integer value is required (single result)
            res = math.floor(res) if ques("integral value") else float(res)

            # print single result
            print("\nResult:", res)

        # if the result is more than a single number (list of values)
        if op in ["v", "ru", "rd", "n", "2", "10"]:
            res = []
            for num in nums:
                num = (math.fabs(num) if op == "v"
                    else math.ceil(num) if op == "ru"
                    else math.floor(num) if op == "rd"
                    else math.log(num) if op == "n"
                    else math.log2(num) if op == "2"
                    else math.log10(num)) # op == "10"
                res.append(num)

            # ask user if absolute (non-negative) values are required (multiple results)
            if any(num < 0 for num in res) and ques("absolute values"): res = map(math.fabs, res)

            # ask user if integer values are required (multiple results)
            res = map(math.floor, res) if ques("integral values") else map(float, res)
            
            # print multiple results as comma separated values
            print("\nResult:", ", ".join(map(str, res)))


# ask a yes/no question and return a true or false value based on user input
def ques(ques) -> bool:
    while True:
        ques = input(f"{ques.capitalize()}? ")
        return True if re.search("y(es)?$", ques, re.IGNORECASE) else False if re.search("n(o)?$", ques, re.IGNORECASE) else None


# print a divider/header depending on parameter 'args'
def line(*args, num = 100) -> None:
    print()
    if not args: print("*" * num)
    else:
        word = " " + args[0] + " "
        print(word.center(num,"*"))
    print()


if __name__ == "__main__":
    main()
