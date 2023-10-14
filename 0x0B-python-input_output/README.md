# 0x0B-python-input/output


## New commands / functions used:
* ``import json``
* ``with open(<filename>, 'w' or 'a' or 'r' or 'b', encoding="utf-8") as file:`` -- 'w' for write, 'a' for append, 'r' for read, and 'b' for bytemode. It is good practice to use with open(): because it will be properly closed after reading, even if will raises an exception.
* ``file.read(size)`` -- Reads the whole file if <size> is ommitted. Otherwise reads <size> bytes from the file.
* ``file.readline()`` -- Reads a single line up to the new line
* ``file.readlines()`` -- Read all the lines including newline characters
* ``file.seek(offset, from_what)`` -- changes the position of the object
* ``file.tell()`` -- Returns an integer witht he offset
* ``file.close()`` -- closes a file descriptor
* ``json.dump()`` -- Puts a python object into a json structure.
* ``json.dumps()`` -- Serializes the object into a text file.
* ``json.load(file_descriptor)`` -- loads a json object if file_descriptor has been opened for reading.

## Helpful Links
* [7.2.Reading and Writing Files](https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7.Predefined Cleanup Actions](https://docs.python.org/3.4/tutorial/errors.html#predefined-clean-up-actions)
* [Files in python](http://www.diveintopython3.net/files.html)
* [json encoder and decoder](https://docs.python.org/3.4/library/json.html)
* [Learn To Program: Youtube](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring stuff with Python](https://automatetheboringstuff.com/)
* [The Proc Filesystem](https://www.kernel.org/doc/Documentation/filesystems/proc.txt)

# Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

# General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

# Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements
## Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 - -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be - verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
