# 🐍 Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a **programming paradigm** that helps model real-world problems by using **objects** and **classes**.

---

## ⚠️ Problems Before OOP
Without OOP, developers faced:
1. **Code Duplication**  
2. **Difficult Maintenance**  
3. **Data Security Issues**  
4. **Poor Code Reusability**  
5. **No Real-World Representation**

---

## ✅ What is OOP?
- A paradigm that provides **security, maintainability, and reusability**  
- Best suited for **large projects**  
- Helps solve **real-world problems**

---

## 🏗️ Key Terminologies
### 📌 Class
- A **template** or **blueprint** for creating objects.  

### 📌 Object
- An **instance of a class** with:
  - **Properties (attributes)**
  - **Functions (behaviors)**

---

## 📖 Example: Class and Object
```python
class Character:
    def __init__(self, name, health):   # Constructor
        self.name = name
        self.health = health

warrior = Character("Shazam", 100)
print(warrior.name)   # Output: Shazam

```
