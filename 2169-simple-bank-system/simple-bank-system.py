class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def _is_valid_account(self, account) -> bool:
        if account - 1 < len(self.balance):
            return True
        return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1):
            return False
        if not self._is_valid_account(account2):
            return False
        if not self.withdraw(account1, money):
            return False
        self.deposit(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account - 1):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account - 1):
            return False
        if self.balance[account - 1] - money < 0:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)