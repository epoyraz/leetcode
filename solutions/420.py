class Solution:
    def strongPasswordChecker(self, password):
        n = len(password)
        
        has_lower = has_upper = has_digit = False
        for c in password:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True
        
        missing_types = 3 - (has_lower + has_upper + has_digit)
        
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                j = i
                while j < n and password[j] == password[i-1]:
                    j += 1
                repeats.append(j - (i-2))
                i = j
            else:
                i += 1
        
        if n < 6:
            return max(missing_types, 6 - n)
        
        replace = sum(length // 3 for length in repeats)
        
        if n <= 20:
            return max(missing_types, replace)
        
        # Need to delete (n-20) chars
        delete = n - 20
        
        for idx in range(len(repeats)):
            if delete == 0:
                break
            length = repeats[idx]
            if length < 3:
                continue
            if length % 3 == 0:
                reduce = min(delete, 1)
                repeats[idx] -= reduce
                delete -= reduce
        
        for idx in range(len(repeats)):
            if delete == 0:
                break
            length = repeats[idx]
            if length < 3:
                continue
            if length % 3 == 1:
                reduce = min(delete, 2)
                repeats[idx] -= reduce
                delete -= reduce
        
        for idx in range(len(repeats)):
            if delete == 0:
                break
            length = repeats[idx]
            if length < 3:
                continue
            reduce = min(delete, length - 2)
            repeats[idx] -= reduce
            delete -= reduce
        
        replace = sum(length // 3 for length in repeats if length >= 3)
        
        return (n - 20) + max(missing_types, replace)
