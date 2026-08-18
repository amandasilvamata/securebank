from account import withdraw, transfer


def test_withdraw_rejects_negative_amount():

	result = withdraw(1, -50)

	assert result == "Withdrawal amount must be greater than zero."

def test_withdraw_rejects_zero_amount():

	result = withdraw(1, 0)

	assert result == "Withdrawal amount must be greater than zero."

def test_transfer_rejects_negative_amout():

	result = transfer(1, 2, -50)

	assert result == "Transfer amount must be greater than zero."

def test_transfer_rejects_zero_amount():

	result = transfer(1, 2, 0)

	assert result == "Transfer amount must be greater than zero." 

def test_transfer_rejects_self_transfer():

	result = transfer(1, 1, 50)

	assert result == "You cannot transfer money to yourself."
