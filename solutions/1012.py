from fractions import Fraction

class Solution:
    def isRationalEqual(self, s, t):
        def to_fraction(s):
            if '(' not in s:
                return Fraction(s)
            
            base, repeat = s.split('(')
            repeat = repeat.rstrip(')')
            
            if '.' in base:
                int_part, frac_part = base.split('.')
            else:
                int_part, frac_part = base, ''
            
            # Build base value: integer + non-repeating decimal part
            base_frac = Fraction(int_part)
            if frac_part:
                base_frac += Fraction(int(frac_part), 10 ** len(frac_part))
            
            # Add repeating part as infinite geometric series
            repeat_denominator = (10 ** len(frac_part)) * (10 ** len(repeat) - 1)
            repeat_numerator = int(repeat)
            repeat_frac = Fraction(repeat_numerator, repeat_denominator)

            return base_frac + repeat_frac

        return to_fraction(s) == to_fraction(t)
