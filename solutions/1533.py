class Solution(object):
    def displayTable(self, orders):
        from collections import defaultdict

        table_orders = defaultdict(lambda: defaultdict(int))
        food_items = set()

        # Collect orders
        for customer, table, food in orders:
            table_orders[int(table)][food] += 1
            food_items.add(food)

        # Sort food items alphabetically
        sorted_food = sorted(food_items)
        result = [["Table"] + sorted_food]

        # Sort table numbers numerically
        for table in sorted(table_orders):
            row = [str(table)]
            for food in sorted_food:
                row.append(str(table_orders[table][food]))
            result.append(row)

        return result
