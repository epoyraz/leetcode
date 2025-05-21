class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            parsed.append((name, int(time), int(amount), city, t))

        n = len(parsed)
        invalid = [False] * n

        for i in range(n):
            name_i, time_i, amount_i, city_i, raw_i = parsed[i]
            
            if amount_i > 1000:
                invalid[i] = True
            
            for j in range(n):
                if i == j:
                    continue
                name_j, time_j, amount_j, city_j, raw_j = parsed[j]
                if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                    invalid[i] = True
                    break

        return [parsed[i][4] for i in range(n) if invalid[i]]
