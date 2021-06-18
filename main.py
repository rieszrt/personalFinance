import datetime
import config
import numpy as np
from matplotlib import pyplot as plt
import lifestyles as LS
# from scipy.optimize import Bounds

portfolio = LS.living_with_mum

stock_purchase_frequency = 30
stock_purchase_amount = 4000
weekly_income = config.after_tax_salary / 52

for day in range(365*8):
    if day%7==0:
        portfolio['bank'].deposit(weekly_income)
    if day%365==0:
        weekly_income*=1.1
        stock_purchase_amount*=1.1
    if day%stock_purchase_frequency==0:
        portfolio['bank'].withdraw(stock_purchase_amount)
        portfolio['shares'].deposit(stock_purchase_amount-10)
    for key,value in portfolio.items():
        value.tick_day()

plt.plot(range(len(portfolio['bank'].pv_record)), portfolio['bank'].pv_record + portfolio['shares'].pv_record, label="total")
plt.plot(range(len(portfolio['bank'].pv_record)), portfolio['bank'].pv_record, label="bank")
plt.plot(range(len(portfolio['shares'].pv_record)), portfolio['shares'].pv_record, label="shares")
plt.title("Present Value of assets")
plt.legend(loc="upper left")
plt.savefig('test.png')
