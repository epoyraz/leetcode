class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        rounded = int((purchaseAmount + 5) / 10) * 10
        return 100 - rounded
