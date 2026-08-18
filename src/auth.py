import bcrypt

from database import get_connection
from account import create_account

def create_user(name, email, password):

	if not name.strip():
		return "Name cannot be empty."

	if "@" not in email or "." not in email:
		return "Invalid email."

	if len(password) < 8:
		return "Password must have at least 8 characters."

	connection = get_connection()
	cursor = connection.cursor()

	query = """
		SELECT id
		FROM users
		WHERE email = %s
	"""

	cursor.execute(query, (email,))

	existing_user = cursor.fetchone()

	if existing_user:
		cursor.close()
		connection.close()
		return "Email already registered."

	password_hash = bcrypt.hashpw(
		password.encode("utf-8"),
		bcrypt.gensalt()
	)

	query = """
		INSERT INTO users (name, email, password_hash)
		VALUES (%s, %s, %s)
	"""

	cursor.execute(
		query,
		(name, email, password_hash)
	)

	user_id = cursor.lastrowid

	connection.commit()

	cursor.close()
	connection.close()

	create_account(user_id)

	return "User created successfully."

def login(email, password):

	connection = get_connection()
	cursor = connection.cursor(dictionary=True)

	query = """
		SELECT id, name, email, password_hash
		FROM users
		WHERE email = %s
	"""

	cursor.execute(query, (email,))

	user = cursor.fetchone()

	cursor.close()
	connection.close()

	if not user:
		return None

	password_hash = user["password_hash"]

	if bcrypt.checkpw(
		password.encode("utf-8"),
		password_hash.encode("utf-8")
	):
		return user

	return None
