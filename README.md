# AirBnB_clone

![hbnb project](image.png)

## Background Context
Welcome to the AirBnB clone project! - The console

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. 
This first step is very important because you will use what you build during this project 
with all other following projects: HTML/CSS templating, database storage, API, front-end integration e.t.c

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, 
serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: 
Instance <-> Dictionary <-> JSON string <-> file

create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## description of the command interpreter:

Execution: Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

