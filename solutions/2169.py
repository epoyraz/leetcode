class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.n = len(balance)

    def _valid_account(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: long
        :rtype: bool
        """
        if not self._valid_account(account1) or not self._valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: long
        :rtype: bool
        """
        if not self._valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: long
        :rtype: bool
        """
        if not self._valid_account(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
