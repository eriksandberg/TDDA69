class AccountError(Exception):
    def __init__(self, value):
        self.value = value
    def str(self):
        return repr(self.value)
 
def make_account(balance, interest):
    time = 0
    
    def withdraw(amount, t):
        nonlocal balance
        nonlocal time
        if time > t:
            raise AccountError("Time error")
        balance += (t - time) * interest * balance
        time = t
        if balance >= amount:
            balance = balance - amount
        else:
            raise AccountError("Account balance too low")
        
    def deposit(amount, t):
        nonlocal balance
        nonlocal time
        if time > t:
            raise AccountError("Time error")
        balance += ((t - time) * interest * balance) + amount
        time = t

    def get_value():
        return balance

    public_methods = {'withdraw' : withdraw, 'deposit' : deposit, 'get_value' : get_value}
    return public_methods
