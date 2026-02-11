🧮 Python Calculator Project
📌 Project Overview

In this project, I build a fully functional calculator in Python.
The project is designed step by step—starting from simple arithmetic functions and gradually evolving into a menu-driven, object-oriented calculator application.

Each task acts as a building block for the final system, helping you understand Python fundamentals such as functions, loops, error handling, user input validation, and object-oriented programming (OOP).

🎯 Project Objectives

Understand how to create and use Python functions

Handle user input safely using error handling

Implement a menu-driven program using loops

Apply Object-Oriented Programming concepts

Build a complete, reusable calculator system

🛠️ Project Requirements
1️⃣ Create Arithmetic Functions

Write four separate Python functions that perform basic arithmetic operations:

Addition: Adds two numbers

Subtraction: Subtracts one number from another

Multiplication: Multiplies two numbers

Division: Divides two numbers

Must safely handle division by zero

These functions serve as the foundation of the calculator.

2️⃣ User Input & Displaying Results

Ask the user to enter two numbers

Use the arithmetic functions to calculate:

Addition result

Subtraction result

Multiplication result

Division result

Display appropriate messages if division by zero occurs

3️⃣ Input Validation

Create a separate function that:

Takes user input

Uses try-except to check whether the input is a valid number

Repeats until the user enters valid numeric input

This ensures the program never crashes due to invalid input.

4️⃣ Menu-Based Calculator

Convert the calculator into a menu-driven application with the following options:

Add

Subtract

Multiply

Divide

Exit

Requirements:

Use a while loop to keep the program running

Allow unlimited operations until the user selects Exit

Display results in a formatted way, for example:

5 + 3 = 8

5️⃣ Object-Oriented Calculator

Transform the calculator into an Object-Oriented Program.

🔹 Create a Calculator Class

Include the following methods:

add()

subtract()

multiply()

divide()

Must return a custom message for division by zero

🔹 A. menu() Method

Displays all available calculator options to the user

🔹 B. run() Method

Acts as the controller of the calculator:

Displays the menu

Takes user choice

Accepts two numbers

Performs the selected operation

Keeps running until the user chooses Exit

🔹 C. Create Calculator Object

At the end of the program:

Create an instance of the Calculator class

Call the run() method to start the calculator automatically
