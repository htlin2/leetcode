class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []  # We can think of this stack as a way to keep track of unmatched '('.
        inserts = 0  # Counts the number of insertions needed.
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                stack.append('(')  # Push the open parenthesis onto the stack
            elif s[i] == ')':
                # We need to check if we have a pair of ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    # If the next character is also ')', it's a valid double closing for a '('
                    if stack:
                        stack.pop()  # We can balance with a previous '('
                    else:
                        # If there's no '(' to balance, we need an extra '('
                        inserts += 1
                    i += 1  # Skip the next ')', as we've handled it here.
                else:
                    # Otherwise, it's a single ')', which means it's incomplete
                    if stack:
                        stack.pop()  # Balance one '(' with this ')', but we need one more ')'
                        inserts += 1  # Need to add another ')'
                    else:
                        # No '(' to balance, so we need to add both '(' and ')'
                        inserts += 2
            
            i += 1

        # If there are any unmatched '(' left in the stack, we need two ')' for each
        inserts += 2 * len(stack)

        return inserts
