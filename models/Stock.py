

class Stock:
    ticker: str

    purchasePrice: float
    currentPrice: float

    dividendAmt: float
    dividendPerc: float

    def __init__(self, ticker, purchasePrice, currentPrice, dividendAmt, dividendPerc):
        self.ticker, self.purchasePrice, self.currentPrice, self.dividendAmt, self.dividendPerc = \
            ticker, purchasePrice, currentPrice, dividendAmt, dividendPerc

