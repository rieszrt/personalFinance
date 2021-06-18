# Personal Finance

A personal finance model where various financial products are base classes derived from the INVESTMENT parent class with 
emphasis on Liskov substitution principle from software design.

## The Investment Object:
The investment object is instantiated with these attributes:

1. calc_Rate: the rate at which interest is calculated 
2. pay_Rate: the rate at which interest is paid to account (in the case of banks this is not the same as calc_Rate)
3. roi: the return on investment per calc_Rate Period.

and contains these methods:

1. deposit: makes a deposit into the capital of the account
2. external_Tick: updates capital after arbitrary number of days. 

## Investment children:
Below are investment options that instantiate from the Investment Object:

1. Shares
2. Super
3. Bank
4. Housing?




