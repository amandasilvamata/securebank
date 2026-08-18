# SecureBank

SecureBank is a simple banking system developed in Python with MySQL, focused on authentication, account management, financial transactions, and basic security practices.

## Features

- User registration
- User login
- Password hashing with bcrypt
- Bank account creation
- Balance checking
- Deposits
- Withdrawals
- Balance validation
- Transfers between accounts
- Transaction history
- Input validation
- Automated tests with pytest

## Technologies

- Python
- MySQL
- mysql-connector-python
- bcrypt
- python-dotenv
- pytest

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
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Security

SecureBank implements basic security practices, including:

- Password hashing with bcrypt
- Database credentials stored in environment variables
- `.env` excluded from version control through `.gitignore`
- Input validation
- Balance validation before withdrawals and transfers
- Prevention of transfers to the same account
- Transaction rollback when a transfer fails

Passwords are never stored as plain text. Instead, they are hashed using bcrypt before being stored in the database.

## Database

SecureBank uses MySQL to store:

- Users
- Bank accounts
- Account balances
- Transactions

The database schema is available in:

```text
sql/schema.sql
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/amandasilvamata/securebank.git
cd securebank
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=securebank
```

Replace `your_password` with your MySQL password.

> Never commit your `.env` file to GitHub.

### 5. Create the database

Run the SQL schema:

```bash
mysql -u root -p < sql/schema.sql
```

## Running the Application

From the project root:

```bash
PYTHONPATH=src python src/main.py
```

The application provides a terminal-based menu with options to:

1. Create an account
2. Log in
3. Exit

After logging in, users can access their banking operations.

## Testing

SecureBank uses pytest for automated testing.

Run the test suite with:

```bash
PYTHONPATH=src pytest
```

The tests cover account-related validation and transaction rules.

## Learning Goals

This project was developed to practice:

- Python programming
- SQL and relational databases
- Python and MySQL integration
- User authentication
- Password hashing
- Environment variables
- CRUD operations
- Financial transactions
- Error handling
- Automated testing
- Basic secure coding practices

## Future Improvements

Possible future improvements include:

- Password reset functionality
- More comprehensive automated tests
- Improved user interface
- Transaction filtering
- Account deletion
- Stronger input validation
- Role-based access control
- Audit logging

## Author

**Amanda Silva da Mata**

Software Engineering Student | Python | SQL | Linux | Cybersecurity
