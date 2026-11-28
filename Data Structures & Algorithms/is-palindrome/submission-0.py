class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        print(s)
        for i in range(len(s) // 2):
            left_char = s[i]
            right_char = s[-i - 1]  # Or s[~i]
            print(f"{left_char} <-> {right_char}")
            if left_char != right_char:
                return False
        return True