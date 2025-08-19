# 🐍 Python Functions, Decorators, Generators & Lambda

This document provides a complete overview of **functions in Python**, including arguments, return values, decorators, generators, and lambda functions.

---

# 📖 Quick Summary Table

| Concept        | Description                                                                 | Example (Code Snippet) |
|----------------|-----------------------------------------------------------------------------|-------------------------|
| Function       | Block of reusable code                                                      | `def greet(): print("Hi")` |
| Arguments      | Values passed to a function (positional, keyword, default)                  | `greet("Manas", city="Mumbai")` |
| Return         | Used to send a result back from a function                                  | `return num1 + num2` |
| Decorator      | Adds extra features to a function without modifying it                      | `@my_decorator` |
| Generator      | Function that yields values one at a time (memory efficient)                | `yield num` |
| Lambda         | Anonymous one-liner function                                                | `lambda x: x+10` |

---

# 🛠️ Functions in Python

Functions are **blocks of code** designed to perform a specific task.  
They improve **reusability, modularity, and scoping** in programs.

---

## ✅ Why use Functions?
- Function naming should clearly state its purpose
- Should do only **one task effectively**
- Avoid global variables inside functions

---

## 📌 Function Syntax
```python
def function_name(parameters...):
    # statements
    return value

function_name(arguments...)
```