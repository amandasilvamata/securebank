# SecureBank

SecureBank is a command-line banking simulation built with Python and MySQL. It was created as a learning project to practice database integration, authentication, transaction handling, and automated testing.

Users can create an account, log in, check their balance, make deposits and withdrawals, transfer funds, and view their transaction history.

## Features

- User registration and login
- Password hashing with bcrypt
- Hidden password input in the terminal
- Automatic bank account creation during registration
- Account ID displayed after login
- Balance checking
- Deposits and withdrawals
- Transfers between accounts
- Prevention of transfers to the same account
- Transaction history showing the sender or receiver of transfers
- Validation of transaction amounts
- Decimal arithmetic for monetary values
- Automated tests with pytest

## Technologies

- **Python**
- **MySQL**
- **mysql-connector-python** — connects Python to MySQL
- **bcrypt** — hashes and verifies passwords
- **python-dotenv** — loads environment variables
- **pytest** — runs automated tests

## Project Structure

```text
securebank/
├── sql/
│   └── schema.sql
├── src/
│   ├── account.py
│   ├── auth.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_account.py
├── .gitignore
├── requirements.txt
└── README.md
```

The `.env` file is created locally during setup and should not be committed to GitHub.

## Requirements

Before getting started, make sure you have:

- Python 3
- MySQL Server
- Git
- A MySQL user with permission to access the `securebank` database

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amandasilvamata/securebank.git
cd securebank
```

### 2. Create and activate a virtual environment

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activation is different:

```bash
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database and tables

Run the SQL schema from the project root:

```bash
mysql -u root -p < sql/schema.sql
```

Enter your MySQL root password when prompted.

On some Ubuntu installations, you can use:

```bash
sudo mysql < sql/schema.sql
```

This step is intended for the first setup. If the tables already exist, MySQL may report that they already exist.

### 5. Configure environment variables

Create a file named `.env` in the project root:

```env
DB_HOST=localhost
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=securebank
```

Replace `your_mysql_user` and `your_mysql_password` with the credentials of a MySQL user that has permission to access the `securebank` database.

> Keep your `.env` file private. Do not commit it to GitHub.

## Running the Application

From the project root, with the virtual environment activated, run:

```bash
python src/main.py
```

The main menu offers three options:

1. Create an account
2. Log in
3. Exit

After logging in, your account ID is displayed. You can share this ID with another user so they can transfer funds to your account.

From the account menu, you can check your balance, deposit, withdraw, transfer funds, and view your statement.

Enter monetary values using a period as the decimal separator, for example:

```text
10.50
```

## Running the Tests

From the project root, with the virtual environment activated, run:

```bash
PYTHONPATH=src pytest
```

The tests check rules such as rejecting invalid withdrawal and transfer amounts and preventing a transfer to the same account.

## Security Practices

This learning project includes some basic security practices:

- Passwords are hashed with bcrypt before being stored.
- Password input is hidden in the terminal.
- Database credentials are loaded from environment variables.
- SQL queries use parameters for user-provided values.
- The application checks balances before withdrawals and transfers.
- A transfer is rolled back if an error occurs during its database operations.

## Learning Goals

This project was developed to practice:

- Python programming
- SQL and relational databases
- Python and MySQL integration
- User authentication and password hashing
- Environment variables
- Database transactions and rollback
- Input validation
- Automated testing with pytest

## Future Improvements

- Add more automated tests, including database error scenarios
- Improve database error messages
- Test the setup process on a fresh database
- Improve handling of simultaneous transactions
- Add transaction filtering
- Add password reset functionality

## Author

**Amanda Silva da Mata**

Software Engineering Student | Python | SQL | Linux | Cybersecurity