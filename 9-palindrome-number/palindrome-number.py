class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x!= 0):
            return False

        sum = 0
        n = x

        while n > sum:
            last_digit = n%10
            sum = sum*10 + last_digit
            n //= 10

        if n == sum or n == sum // 10:
            return True
