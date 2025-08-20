# 🚨 Exception Handling in Python

Exception handling allows you to gracefully manage errors in your program without breaking its execution.

---

## 🔎 Types of Errors

1. **Compile-Time Error (Syntax Error)**  
   - Occurs while writing code (invalid syntax).  
   - Example:  
     ```python
     print("Hello"  # Missing closing parenthesis
     ```

2. **Runtime Error (Exception)**  
   - Occurs during execution of the program.  
   - Example:  
     ```python
     print(5 / 0)  # ZeroDivisionError
     ```

3. **Logical Error**  
   - Program runs without crashing but produces incorrect output.  
   - Example:  
     ```python
     # Expected square but returns double
     def square(num):
         return num * 2
     ```

---

## 🐞 Bugs and Debugging

- **Bug** → An error in software.  
- **Debugging** → The process of detecting and fixing bugs.

---

## 🛡️ Handling Exceptions

Python provides a **try-except-finally** block.

### ✅ Syntax

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Handle the error
finally:
    # Always executed (cleanup code like closing DB connections)
```