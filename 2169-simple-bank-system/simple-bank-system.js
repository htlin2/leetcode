/**
 * @param {number[]} balance
 */
var Bank = function(balance) {
    this.accounts = {}
    for (let i = 0; i < balance.length; i++) {
        this.accounts[i + 1] = balance[i]
    }
};

/** 
 * @param {number} account1 
 * @param {number} account2 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.transfer = function(account1, account2, money) {
    if (this.accounts[account1] === undefined) return false
    if (this.accounts[account2] === undefined) return false
    if (this.accounts[account1] < money) return false
    this.accounts[account1] -= money
    this.accounts[account2] += money
    return true
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.deposit = function(account, money) {
    if (this.accounts[account] === undefined) return false
    this.accounts[account] += money
    return true
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.withdraw = function(account, money) {
    if (this.accounts[account] === undefined) return false
    if (this.accounts[account] < money) return false
    this.accounts[account] -= money
    return true
};

/** 
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */