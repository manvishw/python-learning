# 📌 Python List

A **List** is an ordered, dynamic array in Python.  
- ✅ Supports multiple data types  
- ✅ Mutable (can be changed after creation)  
- ✅ Indexing starts from `0`  
- ✅ Supports concatenation using `+`  
- ✅ Supports repetition using `*`  

---

## 📝 Ways to Create a List

### 1) Using `[]` Brackets
```python
my_list = [1, 2, 3, "Hello", True]
print(my_list)   # [1, 2, 3, 4, 'Hello', True]
```

## 🛠️ List Methods

| Method | Description | Example | Output |
|--------|-------------|---------|--------|
| `append(x)` | Add element at end | `l=[1,2]; l.append(3)` | `[1,2,3]` |
| `extend(list)` | Extend with another list | `[1,2].extend([3,4])` | `[1,2,3,4]` |
| `insert(i, x)` | Insert at index | `l=[1,2]; l.insert(1,"Hi")` | `[1,"Hi",2]` |
| `remove(x)` | Remove first occurrence | `[1,2,2,3].remove(2)` | `[1,2,3]` |
| `pop([i])` | Remove & return element | `l=[1,2,3]; l.pop()` | returns `3` |
| `clear()` | Remove all elements | `l=[1,2]; l.clear()` | `[]` |
| `index(x)` | Return index of value | `[1,2,3].index(2)` | `1` |
| `count(x)` | Count occurrences | `[1,1,2].count(1)` | `2` |
| `sort()` | Sort ascending | `l=[3,1,2]; l.sort()` | `[1,2,3]` |
| `reverse()` | Reverse order | `[1,2,3].reverse()` | `[3,2,1]` |
| `copy()` | Shallow copy | `new = old.copy()` | Independent copy |
| `min(list)` | Minimum value | `min([3,1,2])` | `1` |
| `max(list)` | Maximum value | `max([3,1,2])` | `3` |
