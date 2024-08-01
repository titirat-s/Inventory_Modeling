import math

def TC(D: int, C: float, S: float, H: float, Q: int, decimal=2):
  """
  Function use to perform Total Cost to carry inventory

  Args:
    D: Demand in year or cycle
    C: Inventory cost per unit (product cost)
    S: Set up cost use to purchase inventory (set up cost)
    H: Holding cost use to carry inventory (holding cost)
    Q: Quantity order in once
    decimal: result decimal, default=2

  Return:
    TC: Total cost of inventory
  """
  total_cost = (D*C)+(H*Q/2)+(S*D/Q)
  return round( total_cost, decimal);

assert TC(D=10000, C=4, Q=1000, S=20, H=4*0.2) == 40600
assert TC(10000, 4.5, 20, 4.5*0.2, 666.67 ,2) == 45600