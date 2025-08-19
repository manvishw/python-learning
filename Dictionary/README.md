# 📘 Python Dictionary

A **Dictionary** in Python is a collection of **key-value pairs**.  
It is:

- ✅ **Ordered** (from Python 3.7+)  
- ✅ **Mutable** (can be updated)  
- ✅ **Dynamic** (can grow/shrink)  
- ✅ Stores **unique keys**  

---

## 🔑 Creating a Dictionary

```python
my_dict = {
  "name": "Manas Vishwakarma",
  "age": 23,
  "gender": "Male",
  "isGraduated": True,
  "cgpa": 8.03  
}

print(my_dict)
```

## 📌 Dictionary Methods

| Method | Description | Example | Output |
|--------|-------------|---------|--------|
| `dict.get(key, default)` | Returns value of key, else default | `my_dict.get("name")` | `"Manas Vishwakarma"` |
| `dict.keys()` | Returns all keys | `my_dict.keys()` | `dict_keys(['name','age','gender','isGraduated','cgpa'])` |
| `dict.values()` | Returns all values | `my_dict.values()` | `dict_values(['Manas Vishwakarma',23,'Male',True,8.03])` |
| `dict.items()` | Returns key-value pairs | `my_dict.items()` | `dict_items([('name','Manas Vishwakarma'),('age',23),...])` |
| `dict.pop(key, default)` | Removes key and returns value | `my_dict.pop("age")` | `23` |
| `dict.popitem()` | Removes last inserted item | `my_dict.popitem()` | `('cgpa', 8.03)` |
| `dict.clear()` | Removes all items | `my_dict.clear()` | `{}` |
