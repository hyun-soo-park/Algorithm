class Solution:
    def isPalindrome(self, s: str) -> bool:
        nonreverse = []
        reverse = []
        for i in s:
            if i.isdecimal() == True:
                nonreverse.append(i)
            elif i.isalpha() == True:
                nonreverse.append(i.lower())

        for i in range(len(s) - 1, -1, -1):
            if s[i].isdecimal() == True:
                reverse.append(s[i])
            elif s[i].isalpha() == True:
                reverse.append(s[i].lower())

        if reverse == nonreverse:
            return True
        else:
            return False