# Airbnb Clone - Command Line Interface (CLI)

This project is a simplified version of Airbnb's backend system, implemented as a command-line interface (CLI). It allows users to manage and interact with data related to hosts, users, places, and reviews.

## Command Interpreter

The command interpreter is a Python script that provides a command-line interface for interacting with the Airbnb clone's backend functionality. It offers various commands to manipulate and manage data within the system.

### How to Start It

To start the command interpreter, follow these steps:

1. Clone the repository from GitHub:

```bash
git clone https://github.com/your_username/Airbnb_clone.git
```

2. Navigate to the project directory:

```bash
cd Airbnb_clone
```

3. Run the command interpreter:

```bash
./console.py
```

### How to Use It

Once the command interpreter is running, you can enter commands and arguments to perform various actions. Here are some of the available commands:

- `create`: Create a new instance of a given class (e.g., `create User`).
- `show`: Display details of a specific instance (e.g., `show Place 1234-1234-1234`).
- `destroy`: Delete a specific instance (e.g., `destroy Review 5678-5678-5678`).
- `all`: Retrieve all instances of a given class or all instances across all classes (e.g., `all User` or `all`).
- `update`: Update attributes of a specific instance (e.g., `update Place 1234-1234-1234 name "New Place Name"`).

For a complete list of commands and their usage, you can use the `help` command within the interpreter.

### Examples

Here are some examples of using the command interpreter:

1. Create a new user:

```bash
(create) User email="example@example.com" password="password123"
```

2. Show details of a place:

```bash
(show) Place 1234-1234-1234
```

3. Update the name of a place:

```bash
(update) Place 1234-1234-1234 name "New Place Name"
```

4. Retrieve all instances of a class:

```bash
(all) User
```

5. Delete a review:

```bash
(destroy) Review 5678-5678-5678
```
