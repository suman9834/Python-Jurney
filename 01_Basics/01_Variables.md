# Python Variables

## 1. What is a Variable?

A variable is a name used to store a value in a Python program.

For example:

```python
name = "Suman"
age = 20
```

Here:

- `name` is a variable.
- `"Suman"` is the value stored in `name`.
- `age` is a variable.
- `20` is the value stored in `age`.

---

## 2. Creating a Variable

In Python, we create a variable using the assignment operator `=`.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Suman"
age = 20
```

---

## 3. Printing a Variable

We can use the `print()` function to display the value stored in a variable.

### Example

```python
name = "Suman"

print(name)
```

### Output

```text
Suman
```

---

## 4. Different Values in Variables

A variable can store different types of values.

```python
name = "Suman"
age = 20
height = 5.5
is_student = True
```

Here:

| Variable | Value | Type |
|---|---|---|
| `name` | `"Suman"` | String |
| `age` | `20` | Integer |
| `height` | `5.5` | Float |
| `is_student` | `True` | Boolean |

---

## 5. Changing a Variable's Value

A variable's value can be changed.

```python
age = 20

print(age)

age = 21

print(age)
```

### Output

```text
20
21
```

The latest assigned value is stored in the variable.

---

## 6. Multiple Variables

We can create multiple variables in a program.

```python
name = "Suman"
age = 20
city = "Vaishali"

print(name)
print(age)
print(city)
```

### Output

```text
Suman
20
Vaishali
```

---

## 7. Variable Naming Rules

Python has some rules for naming variables.

### Rule 1: A variable name can contain letters, numbers and underscores.

Valid:

```python
name = "Suman"
age2 = 20
student_name = "Suman"
```

### Rule 2: A variable name cannot start with a number.

Invalid:

```python
2name = "Suman"
```

Valid:

```python
name2 = "Suman"
```

### Rule 3: Spaces are not allowed in variable names.

Invalid:

```python
student name = "Suman"
```

Use an underscore instead:

```python
student_name = "Suman"
```

### Rule 4: Python is case-sensitive.

These are different variables:

```python
name = "Suman"
Name = "Rahul"
```

`name` and `Name` are not the same.

---

## 8. Checking the Type of a Variable

We can use the `type()` function to check the data type of a variable.

```python
age = 20

print(type(age))
```

### Output

```text
<class 'int'>
```

Another example:

```python
name = "Suman"

print(type(name))
```

### Output

```text
<class 'str'>
```

---

## 9. Dynamic Typing in Python

Python is dynamically typed.

This means we do not have to specify the data type while creating a variable.

For example:

```python
x = 10
```

Later, the same variable can store another type of value:

```python
x = "Hello"
```

Python automatically determines the type of value.

---

## 10. Common Mistakes

### Mistake 1: Starting a variable name with a number

```python
1name = "Suman"
```

This is invalid.

Correct:

```python
name1 = "Suman"
```

### Mistake 2: Using spaces

```python
student name = "Suman"
```

Correct:

```python
student_name = "Suman"
```

### Mistake 3: Forgetting quotation marks for text

Incorrect:

```python
name = Suman
```

Correct:

```python
name = "Suman"
```

---

## 11. Practice Questions

### Beginner

1. Create a variable called `name` and store your name.
2. Create a variable called `age` and store your age.
3. Print both variables.

### Intermediate

4. Create two number variables and print their sum.
5. Create a variable called `city` and store your city.
6. Create a variable called `college` and store your college name.
7. Change the value of an `age` variable and print it.

### Challenge

Create these four variables:

```text
name
age
city
is_student
```

Store appropriate values in them and print all four.

---

## 12. Quick Revision

- A variable is a name used to store a value.
- Python variables are created using `=`.
- A variable's value can be changed.
- `print()` displays a value.
- `type()` tells us the type of a value.
- Python is dynamically typed.
- Variable names cannot start with a number.
- Spaces are not allowed in variable names.
- Python is case-sensitive.

---

## 13. Mini Project

Create a simple student information program.

```python
name = "Suman"
age = 20
course = "B.Tech CSE"
year = 3

print(name)
print(age)
print(course)
print(year)
```

Try changing the values and run the program yourself.