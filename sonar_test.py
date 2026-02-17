import os
import subprocess

def compute(values):
    total = 0
    for v in values:
        if v is None:
            continue
        total = total + v
    return total

def greet(name):
    # Security issue: command injection risk if name comes from user input
    subprocess.run("echo Hello " + name, shell=True)

def read_password():
    # Bad practice: hardcoded credential (example only)
    password = "123456"
    return password

def process(items):
    # Code smell: catches all exceptions and hides the error
    try:
        return [int(x) for x in items]
    except Exception:
        return []

def main():
    data = [1, 2, None, 3]
    print(compute(data))
    user = os.getenv("USER_INPUT", "world")
    greet(user)
    print(read_password())
    print(process(["1", "x", "2"]))

if __name__ == "__main__":
    main()
