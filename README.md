# Arithmetic Operations Calculator
This is a simple command-line calculator that performs various arithmetic operations on one or more numbers entered by the user.

## Requirements
This program requires Python 3 to be installed on the system. No additional packages or libraries are required.

## Usage
The program is executed by running the main() function. To run the program, simply execute the following command in the terminal:

```
python calculator.py
```

Once the program is running, the user is presented with a list of available arithmetic operations, along with a corresponding key for each operation. The user can then input the desired operation by entering the corresponding key.

After selecting an operation, the calculator will ask the user to enter the number of inputs (operands) to be used in the calculation. Once the user has entered the number of operands, the calculator will ask the user to enter each input, one at a time.

If the selected operation returns a single result (i.e. addition, subtraction, multiplication, division, power, least common multiple, or greatest common divisor), the calculator will return the result as a single value. If the selected operation returns multiple results (i.e. absolute value, round up, round down, natural logarithm, base-2 logarithm, or base-10 logarithm), the calculator will return the results as a comma-separated list.

The user can also specify additional options, such as requesting positive or integral results.

## Key operations
The following arithmetic operations are available in the program, each corresponding to a key that the user must input:

* a - addition
* s - subtraction
* m - multiplication
* d - division
* p - raise to the power of
* v - absolute value (positive value)
* ru - round up to the nearest integer
* rd - round down to the nearest integer
* n - natural logarithm
* 2 - base-2 logarithm
* 10 - base-10 logarithm
* l - least common multiple
* g - greatest common divisor
* q - quit the calculator

## Sample Usage
```
********************************* ARITHMETIC OPERATIONS CALCUATOR **********************************

a - ADDITION
s - SUBTRACTION
m - MULTIPLICATION
d - DIVISON
p - TO THE POWER OF
v - ABSOLUTE VALUE
ru - ROUND UP TO THE NEAREST INTEGER
rd - ROUND DOWN TO THE NEAREST INTEGER
n - NATURAL LOGARITHM
2 - BASE-2 LOGARITHM
10 - BASE-10 LOGARITHM
l - LEAST COMMON MULTIPLE
g - GREATEST COMMON DIVISOR
q - QUIT

****************************************************************************************************

Enter operation: p

***************************************** TO THE POWER OF ******************************************

Number of inputs: 3

Enter number 1: 2
Enter number 2: 2
Enter number 3: 2

Integral value? n

Result: 16.0

********************************* ARITHMETIC OPERATIONS CALCUATOR **********************************

a - ADDITION
s - SUBTRACTION
m - MULTIPLICATION
d - DIVISON
p - TO THE POWER OF
v - ABSOLUTE VALUE
ru - ROUND UP TO THE NEAREST INTEGER
rd - ROUND DOWN TO THE NEAREST INTEGER
n - NATURAL LOGARITHM
2 - BASE-2 LOGARITHM
10 - BASE-10 LOGARITHM
l - LEAST COMMON MULTIPLE
g - GREATEST COMMON DIVISOR
q - QUIT

****************************************************************************************************

Enter operation: 2

***************************************** BASE-2 LOGARITHM *****************************************

Number of inputs: 4

Enter number 1: 10
Enter number 2: 4
Enter number 3: 6
Enter number 4: 7 

Integral values? n 

Result: 3.321928094887362, 2.0, 2.584962500721156, 2.807354922057604

********************************* ARITHMETIC OPERATIONS CALCUATOR **********************************

a - ADDITION
s - SUBTRACTION
m - MULTIPLICATION
d - DIVISON
p - TO THE POWER OF
v - ABSOLUTE VALUE
ru - ROUND UP TO THE NEAREST INTEGER
rd - ROUND DOWN TO THE NEAREST INTEGER
n - NATURAL LOGARITHM
2 - BASE-2 LOGARITHM
10 - BASE-10 LOGARITHM
l - LEAST COMMON MULTIPLE
g - GREATEST COMMON DIVISOR
q - QUIT

****************************************************************************************************

Enter operation: q

**************************************** END OF CALCULATOR *****************************************

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
