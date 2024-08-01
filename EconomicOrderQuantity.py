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