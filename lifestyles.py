from financialObjects import Asset, Cost
import config

living_alone = {
    "bank": Asset(roi=config.yearly_to_weekly_ir(config.bank_roi),
                  frequency='daily',
                  starting_capital=10000),
    "shares": Asset(roi=config.yearly_to_weekly_ir(config.shares_roi),
                    frequency='daily',
                    starting_capital=70000),
    "rent": Cost(amount=220,
                 frequency='weekly'),
    "electricity": Cost(amount=90,
                        frequency='monthly'),
    "grocery": Cost(amount=100,
                    frequency="weekly"),
    "transportation": Cost(amount=30,
                           frequency="weekly")
}

living_with_mum = {
    "bank": Asset(roi=config.yearly_to_weekly_ir(config.bank_roi),
                  frequency='daily',
                  starting_capital=10000),
    "shares": Asset(roi=config.yearly_to_weekly_ir(config.shares_roi),
                    frequency='daily',
                    starting_capital=70000),
    "rent": Cost(amount=0,
                 frequency='weekly'),
    "electricity": Cost(amount=0,
                        frequency='monthly'),
    "grocery": Cost(amount=20,
                    frequency="weekly"),
    "transportation": Cost(amount=50,
                           frequency="weekly")
}