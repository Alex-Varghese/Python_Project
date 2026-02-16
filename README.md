# Python BankAccount & Student Grades Analyzer

A Python project implementing two core functionalities: a banking system with transaction management and a student grades analyzer from CSV files.

## 📋 Table of Contents
- [BankAccount Class](#1-Account-class)
- [Student Grades Analyzer](#2-student-grades-analyzer)

## 1. Account Class

A comprehensive bank account management system with transaction history and transfer capabilities.

### Features
- Initialize account with:
  - Account number
  - Holder name
  - Initial balance (default: 0)
- **Deposit** money with validation (positive amounts only)
- **Withdraw** money with balance verification
- **Check balance** anytime
- **Transfer** money between accounts
- **Transaction history** tracking with timestamps
- **String representation** for readable output

### Class Structure
```python
class account:
    def __init__(self, acc_number, name, initial_balance=0):
        # Initialize account with transaction history
        
    def deposit(self, amount):
        # Add money to account (amount must be positive)
        
    def withdraw(self, amount):
        # Remove money from account (check sufficient balance)
        
    def get_balance(self):
        # Return current balance
        
    def transfer(self, amount, target_account):
        # Transfer money to another account
        
    def __str__(self):
        # Readable account representation
```

## Student Grades Analyzer

A Python script that analyzes a CSV file containing student grades and generates a comprehensive report with statistics and insights.

### Features

- **Read CSV file** with error handling for missing files
- **Student class** to store individual student information
- **Calculate averages** for each student across all subjects
- **Generate comprehensive reports** showing:
  - Total number of students
  - Class average for each subject
  - Overall class average
  - Top 3 students by overall average
  - Students who scored above 90 in any subject
  - Subject-wise highest and lowest scores
- **Formatted output** written to a text file

```python
class Student:
    def __init__(self, student_id, name, grades):
        # Initialize student with ID, name, and subject grades
        
    def calculate_average(self):
        # Calculate student's average across all subjects
```
