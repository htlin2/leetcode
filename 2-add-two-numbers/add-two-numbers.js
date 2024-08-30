/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    const dummy = curr = new ListNode(-1, null)
    let carry = 0
    while (l1 || l2) {
        let total = carry
        if (l1) {
            total += l1.val
            l1 = l1.next
        }
        if (l2) {
            total += l2.val
            l2 = l2.next
        }
        carry = Math.floor(total / 10)
        curr.next = new ListNode(total % 10)
        curr = curr.next
    }
    if (carry) {
        curr.next = new ListNode(carry)
    }
    return dummy.next
};