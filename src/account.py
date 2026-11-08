from database import get_connection


def create_account(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO accounts (user_id, balance)
        VALUES (%s, %s)
    """

    cursor.execute(
        query,
        (user_id, 0.00)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return "Bank account created successfully."


def get_account_id(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id
        FROM accounts
        WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]

    return None


def get_balance(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT balance
        FROM accounts
        WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]

    return None


def deposit(user_id, amount):

    if amount <= 0:
        return "Deposit amount must be greater than zero."

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id
        FROM accounts
        WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))

    result = cursor.fetchone()

    if not result:
        cursor.close()
        connection.close()
        return "Account not found."

    account_id = result[0]

    query = """
        UPDATE accounts
        SET balance = balance + %s
        WHERE id = %s
    """

    cursor.execute(
        query,
        (amount, account_id)
    )

    query = """
        INSERT INTO transactions (account_id, type, amount)
        VALUES (%s, 'DEPOSIT', %s)
    """

    cursor.execute(
        query,
        (account_id, amount)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return "Deposit successfully."


def withdraw(user_id, amount):

    if amount <= 0:
        return "Withdrawal amount must be greater than zero."

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id, balance
        FROM accounts
        WHERE user_id = %s
    """

    cursor.execute(query, (user_id,))

    result = cursor.fetchone()

    if not result:
        cursor.close()
        connection.close()
        return "Account not found."

    account_id = result[0]
    balance = result[1]

    if amount > balance:
        cursor.close()
        connection.close()
        return "Insufficient balance."

    query = """
        UPDATE accounts
        SET balance = balance - %s
        WHERE id = %s
    """

    cursor.execute(
        query,
        (amount, account_id)
    )

    query = """
        INSERT INTO transactions (account_id, type, amount)
        VALUES (%s, 'WITHDRAW', %s)
    """

    cursor.execute(
        query,
        (account_id, amount)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return "Withdrawal successful."


def get_transactions(user_id):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            transactions.type,
            transactions.amount,
            transactions.created_at,
            sender.name,
            receiver.name,
            sender_account.user_id
        FROM transactions
        INNER JOIN accounts AS sender_account
            ON transactions.account_id = sender_account.id
        INNER JOIN users AS sender
            ON sender_account.user_id = sender.id
        LEFT JOIN accounts AS receiver_account
            ON transactions.receiver_account_id = receiver_account.id
        LEFT JOIN users AS receiver
            ON receiver_account.user_id = receiver.id
        WHERE sender_account.user_id = %s
            OR receiver_account.user_id = %s
        ORDER BY transactions.created_at DESC
    """

    cursor.execute(query, (user_id, user_id))

    transactions = cursor.fetchall()

    cursor.close()
    connection.close()

    return transactions


def transfer(from_user_id, to_account_id, amount):

    if amount <= 0:
        return "Transfer amount must be greater than zero."

    connection = get_connection()
    cursor = connection.cursor()

    try:

        query = """
            SELECT id, balance
            FROM accounts
            WHERE user_id = %s
        """

        cursor.execute(query, (from_user_id,))
        sender = cursor.fetchone()

        if not sender:
            return "Sender account not found."

        sender_account_id = sender[0]
        sender_balance = sender[1]

        query = """
            SELECT id, balance
            FROM accounts
            WHERE id = %s
        """

        cursor.execute(query, (to_account_id,))
        receiver = cursor.fetchone()

        if not receiver:
            return "Receiver account not found."

        receiver_account_id = receiver[0]

        if sender_account_id == receiver_account_id:
            return "You cannot transfer money to yourself."

        if amount > sender_balance:
            return "Insufficient balance."

        query = """
            UPDATE accounts
            SET balance = balance - %s
            WHERE id = %s
        """

        cursor.execute(
            query,
            (amount, sender_account_id)
        )

        query = """
            UPDATE accounts
            SET balance = balance + %s
            WHERE id = %s
        """

        cursor.execute(
            query,
            (amount, receiver_account_id)
        )

        query = """
            INSERT INTO transactions
            (account_id, receiver_account_id, type, amount)
            VALUES (%s, %s, 'TRANSFER', %s)
        """

        cursor.execute(
            query,
            (sender_account_id, receiver_account_id, amount)
        )

        connection.commit()

        return "Transfer successful."

    except Exception:
        connection.rollback()
        return "Transfer failed."

    finally:
        cursor.close()
        connection.close()