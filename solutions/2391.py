class Solution:
    def strongPasswordCheckerII(self, password):
        # 1) Length at least 8
        if len(password) < 8:
            return False
        
        # 2) Flags for required character types
        has_lower = has_upper = has_digit = has_special = False
        specials = set("!@#$%^&*()-+")
        
        # 3) Check adjacent duplicates
        prev = None
        
        for ch in password:
            if ch == prev:
                return False
            prev = ch
            
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in specials:
                has_special = True
            # other characters not possible by constraints
        
        # 4) All flags must be True
        return has_lower and has_upper and has_digit and has_special
