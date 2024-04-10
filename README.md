# Database Setup and Program Execution Guide

Welcome to our project! Below are the instructions to set up the database and run the program.

## 📁 Database Setup

1. Navigate to the main directory of the project.
2. Ensure you have the following files in the main directory:
   - `project.sql`
   - `data.sql`
   - `GenderOptions.txt`

### Modifying the Database

- Feel free to make changes to the tables' values in `project.sql`.
- Make sure to keep `GenderOptions.txt` in the main directory.

### Setting Up the Database

1. Open your PostgreSQL command line interface.
2. Log in as user `postgres`.
3. Execute the following commands:
   ```sql
   -- Paste all the code from project.sql into the command line
   \i project.sql
   
   -- After executing project.sql, paste all the code from data.sql
   \i data.sql
   
# 🚀 Running the Program

To run the program, follow these steps:

1. Open your command line interface.
2. Navigate to the main folder where you can see all the project files, just before the `edu.ucalgary.oop` package.

## Compiling Tests and Classes

Compile the tests and classes using the following commands:

```bash
javac -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" edu\ucalgary\oop\*.java
java -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" org.junit.runner.JUnitCore edu.ucalgary.oop.TestName
```

## Running the Interface

To run the interface, continue to run your command line in the same directory and execute the following commands:

### Central Relief Worker Interface

If you want to start as a Central Relief Worker:

```bash
javac -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" edu\ucalgary\oop\CentralReliefWorkerInterface.java
java -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" edu.ucalgary.oop.CentralReliefWorkerInterface
```

### Location Relief Worker Interface

If you want to start as a Location Relief Worker:

```bash
javac -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" edu\ucalgary\oop\LocationReliefWorkerInterface.java
java -cp ".;path\to\hamcrestcore;path\to\junit;path\to\postgresql" edu.ucalgary.oop.LocationReliefWorkerInterface
```
Now you're all set to run the program and explore its features! 🎉
