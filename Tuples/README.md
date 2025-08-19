# 📌 Python Tuple Quick Reference

## 🔹 What is a Tuple?
- Immutable (cannot be changed after creation)  
- Can store **mixed data types**  
- Faster than lists (due to immutability)  

---

## 🛠️ Tuple Methods & Functions

| Method / Function | Description | Example | Output |
|--------------------|-------------|---------|--------|
| `len(tuple)` | Returns number of elements | `len((1,2,3))` | `3` |
| `min(tuple)` | Returns minimum element | `min((3,1,2))` | `1` |
| `max(tuple)` | Returns maximum element | `max((3,1,2))` | `3` |
| `count(x)` | Count occurrences of value | `(1,2,2,3).count(2)` | `2` |
| `index(x)` | Returns first index of value | `(1,2,3).index(2)` | `1` |
| `sorted(tuple)` | Returns sorted list (not tuple) | `sorted((3,1,2))` | `[1,2,3]` |

---

## 📝 Creating Tuples

### 1️⃣ Using `()` Brackets
```python
my_tuple = (1, 2, 3, "Hello")
print(my_tuple)
# Output: (1, 2, 3, "Hello")
```