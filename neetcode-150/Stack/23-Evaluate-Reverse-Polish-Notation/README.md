# 23 - Evaluate Reverse Polish Notation

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/evaluate-reverse-polish-notation/question

## 1. Problem Description
```text
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
```

**Example 1:**
```text
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
```

**Constraints:**
```text
1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
```

## 2. My Approach
```text
You can easily brute force this problem by just iterating through
the array till you find an operator, then evaluating the expression
with that operator and the two operands to the left of it. Then,
you just have to modify the array so that the result of that
operation is in the spot that the operator once was, and repeat
the process till you get the final result. However, this is a
pretty slow solution, with a time complexity of O(n^2).

Instead, another way to do this is using a stack. With a stack,
you no longer need to run any complicated algorithm to "alter"
the array accordingly after you evaluate an operation. What
I mean by this, is that I can just rely on the way a stack functions
to ensure that the result of the operation is always just going to be
on the top of the stack, ready to be used in the next operation.

To do this problem, all I need to do is iterate through the array and 
push any numbers I see onto a stack. Then, if I ever encounter an operator,
the previous two numbers pushed onto the stack are guaranteed to be the 
operands for that operator, so I just pop them off the stack and evaluate
the operation. Keep in mind that the operand that's popped first is actually
the 2nd value in the operation, and the one popped 2nd is the 1st.
Then, I take that result and I push it onto the stack as the next operand.

Python implementation:
- make a list of operators
- stack = [] to initialize the stack
- loop through the array
- if I see a number (something that's not in the list of operators), I just
stack.append(number)
- if I see an operator, stack.pop() twice, storing the values in variables.
- evaluate the appropriate operation.
- stack.append(result)
- return the final value on the stack as final result of the entire expression.
```

