# 🔤 Python Strings

---

## 📌 Basics of Strings
- **Definition** → Sequence of characters
- **Immutable** → Cannot be changed after creation
- **Indexed & Iterable** → Works like lists (can access with index)
- **Concatenation** → Use `+`
- **Repetition** → Use `*`
- **String Types**:
  - Single-quoted → `'Hello'`
  - Double-quoted → `"Hello"`
  - Multi-line → `"""This is a long string..."""`

### Example:
```python
single_qoute = 'single'
double_qoute = "double"
multiline_str = """we can write 
multiple lines inside it"""

print(single_qoute, "\n", double_qoute, "\n", multiline_str)
```

## 🛠️ String Methods

| Method | Description | Example | Output |
|--------|-------------|---------|--------|
| `.lower()` | Convert to lowercase | `"HELLO".lower()` | `hello` |
| `.upper()` | Convert to uppercase | `"hello".upper()` | `HELLO` |
| `.capitalize()` | Capitalize first letter | `"python".capitalize()` | `Python` |
| `.title()` | Capitalize first letter of each word | `"hello world".title()` | `Hello World` |
| `.swapcase()` | Swap cases | `"PyThOn".swapcase()` | `pYtHoN` |
| `.find("val")` | Returns index of first occurrence | `"hello".find("l")` | `2` |
| `.replace(old, new)` | Replace substring | `"hi hi".replace("hi","hey")` | `hey hey` |
| `.split(" ")` | Split string into list | `"a b c".split(" ")` | `['a','b','c']` |
| `" ".join(list)` | Join list into string | `" ".join(['a','b'])` | `a b` |
| `.startswith("str")` | Check start | `"Python".startswith("Py")` | `True` |
| `.endswith("str")` | Check end | `"Python".endswith("on")` | `True` |
| `.isalpha()` | True if all letters | `"ABC".isalpha()` | `True` |
| `.isdigit()` | True if all digits | `"123".isdigit()` | `True` |
| `.isalnum()` | True if letters+digits | `"abc123".isalnum()` | `True` |
