

class Account:
    buyingPower: float
    cash: float
    positions: [Stock]
    transactions: [Transaction]

    def __init__(self, buyingPower, cash, positions, transactions):
        self.buyingPower, self.cash, self.positions, self.transactions = \
        buyingPower, cash, positions, transactions



