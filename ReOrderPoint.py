import math
import scipy.stats as stats
import pandas as pd
from SafetyStock import SafetyStock

# @markdown ROP function
def ROP(Demand, Leadtime = 1, Safety_Stock: float = 0):
  """
  Function perform inventory Re-Order Point consider average demand, leadtime, and safety stock

  Args:
    Demand = Demand in the specifics period days or month (units)
          pd.Series: Demand in specific period
          int: Average Demand on specific period
    Leadtime: Leadtime (Period: days or months) default = 1
    Safety_Stock = Safety Stock (units) default = 0
        or cal function -> safety_stock_simple() , safety_stock_max(), safety_stock_normdist()

  Return:
    Re-Order point
  """

  if isinstance(Demand, (pd.Series)):
    D_bar = Demand.mean()
  elif isinstance(Demand, (int, float)):
    D_bar = Demand

  if isinstance(Leadtime, (pd.Series)):
    L_bar = Leadtime.mean()
  elif isinstance(Leadtime, (int, float)):
    L_bar = Leadtime

  rop = (L_bar * D_bar) + float(Safety_Stock)
  return rop

assert round(ROP(3, 5, 2),2) == 17
assert round(ROP(Leadtime=3, Demand=pd.Series([11,11,11,11,10]), Safety_Stock=2), 2) == 34.4
assert round(ROP(Demand = pd.Series([11,11,11,11,10]),
                 Leadtime= 4 ,
                 Safety_Stock = math.ceil(SafetyStock.normdist(pd.Series([11,11,11,11,10]), service_level=95))),2) == 44.2