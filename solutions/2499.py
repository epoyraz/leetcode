class Solution:
    def minimumMoney(self, transactions):
        loss_sum = 0
        loss_max_cashback = 0
        profit_max_cost = 0
        
        for cost, cash in transactions:
            if cash >= cost:
                # âProfitâ or neutral transaction
                profit_max_cost = max(profit_max_cost, cost)
            else:
                # Loss-making transaction
                loss_sum += (cost - cash)
                loss_max_cashback = max(loss_max_cashback, cash)
        
        # Worst case for a profit transaction i scheduled after all losses:
        #    requires M â¥ loss_sum + cost_i, so loss_sum + profit_max_cost
        # Worst case for a loss transaction j scheduled last among losses:
        #    requires M â¥ (loss_sum - (cost_j-cash_j)) + cost_j
        #             = loss_sum + cash_j, so loss_sum + loss_max_cashback
        return loss_sum + max(profit_max_cost, loss_max_cashback)
