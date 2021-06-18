import datetime
import config
import numpy as np


class Cost():
    '''
    Assuming costs increase at cpi
    '''
    def __init__(self, amount, frequency='weekly'):
        assert (frequency in ['daily','weekly','monthly','yearly']), "Invalid frequency"
        self.amount = amount
        self.frequency = frequency
        self.cpi_increase_daily = config.yearly_to_weekly_ir(config.cpi_increase)
        self.day = datetime.datetime.now()

    def tick_day(self):
        last_day = self.day
        self.day = self.day + datetime.timedelta(days=1)
        tick = False
        if self.frequency == 'daily':
            tick = True
        elif self.frequency == 'weekly':
            # check if weeks have changed
            if self.day.isocalendar()[1] != last_day.isocalendar()[1]:
                tick = True
        elif self.frequency == 'monthly':
            if self.day.month != last_day.month:
                tick = True
        elif self.frequency == 'yearly':
            if self.day.isocalendar()[0] != last_day.isocalendar()[0]:
                tick = True

        if tick:
            return self.amount
        else:
            return 0

        # Appreciation of costs
        self.amount *= self.cpi_increase_daily


class Asset():
    def __init__(self, roi, frequency="daily", starting_capital=0):
        '''
        Investment Object
        :param roi: interest at each frequency
        :param frequency: frequency (daily, weekly, monthly, yearly)
        :param starting_capital: $0
        '''
        assert (frequency in ['daily','weekly','monthly','yearly']), "Invalid frequency"
        self.frequency = frequency
        self.roi = roi
        self.capital = starting_capital
        self.day = datetime.datetime.now()
        # config
        self.cpi_increase_daily = config.yearly_to_weekly_ir(config.cpi_increase)
        # record
        self.pv_record = np.array([])

    def tick_day(self):
        last_day = self.day
        self.day = self.day + datetime.timedelta(days=1)
        tick = False
        if self.frequency == 'daily':
            tick = True
        elif self.frequency == 'weekly':
            # check if weeks have changed
            if self.day.isocalendar()[1] != last_day.isocalendar()[1]:
                tick = True
        elif self.frequency == 'monthly':
            if self.day.month != last_day.month:
                tick = True
        elif self.frequency == 'yearly':
            if self.day.isocalendar()[0] != last_day.isocalendar()[0]:
                tick = True

        if tick:
            self.capital *= self.roi
        self.pv_record = np.append(self.pv_record, self.present_value())
        # self.pv_record.append(self.present_value())

    def present_value(self, current_day=datetime.datetime.now()):
        delta = self.day - current_day
        pv = self.capital / (self.cpi_increase_daily ** delta.days)
        return pv

    def deposit(self, amount):
        assert amount > 0, "Negative Deposit not allowed"
        self.capital += amount

    def withdraw(self, amount):
        assert amount > 0, "Negative Withdrawal not allowed"
        assert amount < self.capital, "Withdrawal exceeds capital"
        self.capital -= amount
