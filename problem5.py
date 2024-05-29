## Objective: The aim of this assignment is to grasp the concept of logical operations and understand how operator precedence can affect the outcome of an operation.

## Task 1: Validating Calculations - Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.

ex = 3 * 5 + 7 - 14
ex2 = 3 * (5 + 7) - 14
print(ex)
print(ex2)

if ex == ex2:
    print("It's a match!")
else:
    print("No good!")

## Task 2: Mix and Match Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.