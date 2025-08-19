# 🐍 Python Operators Cheat Sheet

---

## 🔢 Arithmetic Operators

| Expression | Description        | Example (x=10, y=15) | Output |
|------------|--------------------|----------------------|--------|
| `x + y`    | Addition           | `10 + 15`            | `25`   |
| `x - y`    | Subtraction        | `10 - 15`            | `-5`   |
| `x * y`    | Multiplication     | `10 * 15`            | `150`  |
| `x / y`    | Division           | `10 / 15`            | `0.666...` |
| `x % y`    | Modulus (Remainder)| `10 % 15`            | `10`   |
| `x // y`   | Floor Division     | `10 // 15`           | `0`    |
| `x ** y`   | Exponentiation     | `10 ** 2`            | `100`  |

---

## ⚖️ Comparison Operators

| Expression | Meaning                         | Example |
|------------|---------------------------------|---------|
| `x > y`    | Greater than                   | `False` |
| `x < y`    | Less than                      | `True`  |
| `x == y`   | Equal to                       | `False` |
| `x != y`   | Not equal to                   | `True`  |
| `x <= y`   | Less than or equal to          | `True`  |
| `x >= y`   | Greater than or equal to       | `False` |

---

## 🧠 Logical Operators

| Operator       | Description                                         | Example           | Result  |
|----------------|-----------------------------------------------------|-------------------|---------|
| `and`          | True if **both** conditions are True               | `True and False`  | `False` |
| `or`           | True if **any one** condition is True              | `True or False`   | `True`  |
| `not`          | Inverts condition (True → False, False → True)     | `not True`        | `False` |

---

## ✍️ Assignment Operators

| Operator | Meaning                                  | Example      | Equivalent |
|----------|------------------------------------------|--------------|------------|
| `=`      | Assign value                             | `x = 1`      | —          |
| `+=`     | Add & assign                             | `x += 1`     | `x = x + 1`|
| `-=`     | Subtract & assign                        | `x -= 1`     | `x = x - 1`|
| `*=`     | Multiply & assign                        | `x *= 2`     | `x = x * 2`|
| `/=`     | Divide & assign                          | `x /= 2`     | `x = x / 2`|

---

## 🆔 Identity Operators

| Operator   | Meaning                                      | Example           | Result  |
|------------|----------------------------------------------|-------------------|---------|
| `is`       | True if both point to the **same object**    | `x is z`          | `True`  |
| `is not`   | True if they **don’t** point to same object  | `x is not y`      | `True`  |

---

## 📦 Membership Operators

| Operator  | Meaning                                     | Example                          | Result  |
|-----------|---------------------------------------------|----------------------------------|---------|
| `in`      | True if value exists in sequence            | `"name" in "My name is Manas"`   | `True`  |
| `not in`  | True if value does not exist in sequence    | `"my" not in "My name is Manas"` | `True`  |

---

✨ **Tip**: Use `print()` in Python to test each operator quickly.
