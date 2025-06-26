
# 📘 Python Data Types & Memory Concepts

##  Mutable vs Immutable in Python

### ✅ Mutable
Mutable objects can be **changed after creation**. The memory reference remains the same.

**Examples:**
- `List` → `[1, 2, 3]`
- `Dictionary` → `{'name': 'Alice'}`
- `Set` → `{1, 2, 3}`

### ❌ Immutable
Immutable objects **cannot be changed** once created. Any modification creates a **new object** in memory.

**Examples:**
- `Integer` → `10`
- `Float` → `3.14`
- `String` → `"hello"`
- `Tuple` → `(1, 2)`
- `Boolean` → `True`, `False`

---

## 🧠 Python Data Types Overview

| Category      | Examples |
|---------------|----------|
| **Numbers**   | `1234`, `3.234`, `3+4j`, `0b11`, `Decimal(12.34)`, `Fraction(1, 3)` |
| **Strings**   | `"hello"`, `'hello'`, `b'a\\x01c'` |
| **List**      | `[1, 2, 3]`, `list(range(10))`, `[1, [2, 'three', 4.5]]` |
| **Tuple**     | `(1, 'spam', 4, 'U')`, `tuple('spam')` |
| **Dictionary**| `{'food': 'Spam', 'quantity': 4}`, `dict(name='Bob', age=40)` |
| **Set**       | `{1, 2, 3}`, `set(range(5))` |
| **File**      | `open('file.txt', 'r')`, `'w'`, `'a'` |
| **Boolean**   | `True`, `False` |
| **NoneType**  | `None` |

---

## 💡 Key Concept: Python Variables & Memory

- Python variables are **references** to objects in memory.
- Python is **dynamically typed** — you do **not** declare types explicitly.

```python
x = 10       # int
x = "Hello"  # x now refers to a str object
```

- Python uses an internal **Garbage Collector (GC)** to manage memory:
  - Automatically frees up memory for variables that are no longer referenced.

---

## 📺 Further Learning

Watch this great explanation on Python memory and data types:  
👉 [YouTube Video Link](https://www.youtube.com/watch?v=brp5aiuWfso&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=7)

---
