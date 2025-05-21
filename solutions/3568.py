class Solution(object):
    def generateKey(self, num1, num2, num3):
        # Convert to 4-digit strings with leading zeros
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        # Take the minimum digit in each position
        key_digits = [min(s1[i], s2[i], s3[i]) for i in range(4)]

        # Join and convert to int to remove leading zeros
        return int(''.join(key_digits))
