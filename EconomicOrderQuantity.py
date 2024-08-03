import math
import pandas as pd

def EOQ(D, S: int, H:int, Stock: int = 0):
  """
  Function use to perform EOQ or Q*

  Args:
    D: Demand in a year or cycle
    S: Set up cost once when order
    H: Holding cost to carry inventory

  Return:
    Q: Economic order quantity (Unit)
  """
  
  if isinstance(D, (pd.Series)):
    D = D.sum().max() - Stock
  elif isinstance(D, (int, float)):
    D = D - Stock
  
  Q = math.sqrt((2*D*S)/H)
  return Q ;

assert math.ceil(EOQ(D=2730, S=300, H=10)) == 405
assert math.ceil(EOQ(2730, 300, 10)) == 405
assert math.ceil(EOQ(10000, 20, 4.5*0.2)) == 667

def orders(D, Q):
  """Function return number of orders within demand cycle

  Args:
      D (int or pd.DataFrame): Cycle demand (units)
      Q (int): Orders quantity (Units)
      
  Returns:
      Number of orders in cycle
  """
  orders = D/Q
  return math.ceil(orders);

def time_between_cycle(Cycle, orders: int, decimal:int = 2):
  """Function return Time between order cycle

  Args:
      Cycle (int): Number of cycle in period (12 months, 365 days, etc.)
      orders (int): Number of orders in period cycle
      decimal (int, optional): Result decimal Defaults to 2.

  Returns:
      time_between_cycle: average days or month between orders time
  """

  time_between_cycle = Cycle/orders
  return round(time_between_cycle, decimal);

def coc(D, Q, S, decimal: int = 2):
  """Function return Cycle Ordering Cost

  Args:
      D (int): Demand
      Q (int): Order Quantity
      S (int): Set up cost
      decimal (int, optional): Result decimal. Defaults to 2.

  Returns:
      coc: Cycle Operation Cost
  """
  coc = D/Q * S
  return round(coc, decimal);


def chc(Q, H, decimal:int = 2):
  """Function return Cycle Holding Cost

  Args:
      Q (int): Order quantity
      H (int): Inventory Holding Cost
      decimal (int, optional): Result decimal. Defaults to 2.

  Returns:
      chc: Cycle Holding Cots 
  """
  chc = Q/2*H
  return round(chc, decimal)

def impact_ratio(Q, q, percent_chg: bool = False, decimal:int = 4):
    """Function return impact of changes between 2 numbers
    Args:
        Q (int:float): 1st Number
        q (int:float): 2nd Number
        percent_chg (bool, optional): Return only changes percent. Defaults to False.
        decimal (int, optional): Return result decimal. Defaults to 4.

    Returns:
        Changes ratio: float    
    """
    if percent_chg == True:
        c = 1.000
    else:
        c = 0.000
    chg = (math.sqrt(Q/q) + math.sqrt(q/Q))/2
    return round((chg - c)*100, decimal)

impact_ratio(239, 200, True, 5) == 0.39696
impact_ratio(29.12, 32, True) == 0.1112