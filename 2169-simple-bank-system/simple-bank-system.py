class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {}
        for i, b in enumerate(balance):
            self.balance[i] = b

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        a1 = self.balance.get(account1 - 1, None)
        a2 = self.balance.get(account2 - 1, None)
        if a1 == None or a2 == None:
            return False
        if a1 - money < 0:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        a = self.balance.get(account - 1, None)
        if a == None:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        a = self.balance.get(account - 1, None)
        if a == None:
            return False
        if a - money < 0:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)