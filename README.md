# 🐍 Python Inheritance and `super()`

A beginner-friendly Python lesson covering **class inheritance** and the use of the **`super()`** function.

This project demonstrates how a child class can inherit methods and functionality from a parent class and how `super()` can be used to call the parent's methods.

---

## 📌 Topics Covered

* Basic Inheritance
* Parent and Child Classes
* Method Inheritance
* The `super()` Function
* Calling a Parent Constructor
* Extending a Parent Class

---

# 1. Basic Inheritance

Inheritance allows one class to reuse functionality from another class.

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()
```

### 🧠 What Happens Here?

`Animal` is the **parent class**:

```python
class Animal:
```

`Dog` is the **child class**:

```python
class Dog(Animal):
```

Because `Dog` inherits from `Animal`, a `Dog` object can use methods defined inside `Animal`.

Therefore:

```python
dog.speak()
```

works even though `speak()` isn't defined inside `Dog`.

The child class can also have its own methods:

```python
dog.bark()
```

---

# 2. What is `super()`?

`super()` allows a child class to access functionality from its **parent class**.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)
```

Here:

```python
super().__init__(name)
```

calls the parent's constructor:

```python
Animal.__init__(name)
```

The parent class handles:

```python
self.name = name
```

while the child class adds its own attribute:

```python
self.breed = breed
```

---

## 🔄 How `super()` Works

```text
Dog()
  │
  ▼
Dog.__init__()
  │
  ├── super().__init__(name)
  │          │
  │          ▼
  │    Animal.__init__()
  │          │
  │          ▼
  │     self.name = name
  │
  └── self.breed = breed
```

This allows the child class to **reuse the parent's initialization** instead of rewriting it.

---

## 🧠 Key Concepts

### Parent Class

The class being inherited from.

```python
class Animal:
```

### Child Class

The class that inherits from another class.

```python
class Dog(Animal):
```

### Inherited Method

A method that the child can use from its parent.

```python
dog.speak()
```

### `super()`

Used to access the parent's methods, especially its constructor.

```python
super().__init__(name)
```

---

## 🎯 Learning Outcomes

After completing this lesson, you should understand:

* What inheritance means in Python.
* The difference between parent and child classes.
* How child classes reuse parent methods.
* How to create a child class using inheritance.
* Why `super()` is useful.
* How a child class can extend a parent's constructor.

---

## 🚀 Next Step

A natural next topic after inheritance and `super()` is **method overriding**, where a child class provides its own implementation of a method inherited from the parent.

---

## 👨‍💻 Author

**Yash**

⭐ If you found this lesson useful, consider giving the repository a star.
