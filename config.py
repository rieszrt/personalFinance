#functional configurations
import numpy as np

def after_tax(income):
    after_tax_income = 0
    if income >=0 and income < 18200:
        return income
    elif income>=18200 and income <37000:
        return 18200+(income-18200)*(1-0.19)
    elif income>=37000 and income <87000:
        return 18200+(37000-18200)*(1-0.19) + (income - 37000)*(1-0.325)
    else:
        return 18200+(37000-18200)*(1-0.19) + (87000 - 37000)*(1-0.325) +(income-87000)*(1-0.37)

def yearly_to_weekly_ir(ir=0.02):
    return np.exp(np.log(1 + ir) / 365)

#economics variables (annual)
cpi_increase = 0.02
bank_roi = 0.03
shares_roi = 0.08


#income
salary = 70000
after_tax_salary = after_tax(salary)

#spending
city_studio = {
    "rent_wk" :290,
    "food_wk" : 100,
    "electricity_mn" : 95,
    "transportation_mn":20
}

living_mom = {
    "rent_mn": 0,
    "food_mn": 0,
    "electricity_mn": 0,
    "transportation_mn": 40 #oppurtunity cost of travel daily? Should I count it in this way?
}