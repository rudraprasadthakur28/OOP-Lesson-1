# Python OOP Lesson 1

This repository contains my practice for OOP Lesson 1 in Python.

The lesson focuses on the basic building blocks of Object-Oriented Programming, including classes, objects, attributes, constructors, methods, `self`, return values, and basic calculations.

## Topics Covered

- Classes
- Objects
- Attributes
- `__init__()` Constructor
- `self`
- Methods
- Return Values
- Basic Calculations

## Classes and Objects

A class is a blueprint for creating objects.

An object is an instance of a class.

Example:

```python
class Student:
    pass

student1 = Student()
```

## Attributes

Attributes are variables that belong to an object or class.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## `__init__()` and `self`

The `__init__()` method is a constructor that runs automatically when an object is created.

The `self` parameter refers to the current object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

## Methods Practice

Methods are functions defined inside a class.

They can be used to perform actions related to an object.

## Return and Calculation Practice

This lesson also includes practice with methods that return values and perform basic calculations.

Example:

```python
class Calculator:
    def add(self, a, b):
        return a + b
```

## Practice Sections

- Class and Object Practice
- Attributes Practice
- `__init__()` and `self` Practice
- Methods Practice
- Return Value Practice
- Calculation Practice

## Learning Goal

The goal of this lesson is to build a strong foundation in Python Object-Oriented Programming before moving to more advanced OOP concepts.

## Status

Completed as part of my Python OOP learning journey.