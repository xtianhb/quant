
import math

class CouponBond:

    def __init__(self, principal, rate, maturity, interest_rate):
        self.principal = principal
        self.rate = rate / 100
        self.maturity = maturity
        self.interest_rate = interest_rate / 100

    def present_value(self, x, n):
        return x * math.exp(-self.interest_rate*n)

    def calculate_price(self):

        price = 0

        # discount the coupon payments
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal * self.rate, t)

        # discount principle amount
        price = price + self.present_value(self.principal, self.maturity)

        return price


if __name__ == '__main__':

    principal = 1000
    rate = 5 # coupon rate
    maturity = 12
    irate = 5 # market rate

    bond = CouponBond(principal, rate, maturity, irate)

    present_price = bond.calculate_price()

    print(f"Principal amount: {principal}")
    print(f"Rate: {rate}")
    print(f"Time to maturity: {maturity}")
    print(f"Market interes rate: {irate}")
    print(f"Bond present price: {present_price:.2f}" )
