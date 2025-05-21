class Solution:
    def complexNumberMultiply(self, num1, num2):
        def parse(num):
            real, imag = num.split('+')
            return int(real), int(imag[:-1])

        a, b = parse(num1)
        c, d = parse(num2)

        real_part = a * c - b * d
        imag_part = a * d + b * c

        return "{}+{}i".format(real_part, imag_part)
