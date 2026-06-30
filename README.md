# My First PR

A tiny project to practice opening a pull request.

## What it does

This project has a small Python script that prints a friendly greeting.
It supports multiple languages — English (`en`) and Chinese (`zh`).

## How to run

```
python greet.py
```

This prints both an English and a Chinese greeting:

```
Hello, world!
你好，世界！
```

## Usage

```python
from greet import greet

greet()                    # "Hello, world!"
greet(lang="zh")           # "你好，世界！"
greet("Alice")             # "Hello, Alice!"
greet("小明", lang="zh")    # "你好，小明！"
```

Unknown language codes fall back to English.

## Welcome

Thanks for checking out this project!
