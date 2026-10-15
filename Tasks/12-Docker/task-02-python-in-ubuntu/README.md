# Task 02: Run Python Inside Ubuntu Docker

## Objective

Install Python 3 inside an Ubuntu container and execute a Python program.

## Commands Executed

```bash
apt-get update
apt-get install -y python3
python3 --version
```

## Python Program

File: `hello.py`

```python
print("Hello from Python inside Docker!")
print("Task 2 completed successfully.")
```

## Run the Program

```bash
python3 hello.py
```

## Output

```text
Hello from Python inside Docker!
Task 2 completed successfully.
```