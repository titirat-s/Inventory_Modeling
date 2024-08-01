import math
import scipy.stats as stats
import numpy as np
import pandas as pd

class SafetyStock:
    # @markdown Simple Safety stock method
    def simple(Demand, Safety_day):
        """
        Function return safety stock unit due to average demand unit and safety time to carry inventory

        Args:
            Demand: Average demand in a period (units)
                int: constance demand
                Series: dynamically demand
            Safety_day: The constant period to carry inventory if order delay
                int: constance period

        Returns:
            SS: simple safety stock
        """
        if isinstance(Demand, (pd.Series)):
            D_bar = Demand.mean()
        elif isinstance(Demand, (int)):
            D_bar = Demand
        else:
            raise TypeError("Demand should be in integer or pandas series(1 columns) format")

        ss = (D_bar*Safety_day).max()
        return math.ceil(ss) ;

    # @markdown Safety Stock Prudent method
    def max(Demand, Leadtime):
        """ Safety day
        Function return safety stock unit due to average and maximum
        of demand unit and leadtime to cover historical worst case

        Args:
            Demand: Average demand in a period (units)
                Series: dynamically demand
                int: Average demand
            Leadtime: The constant period to carry inventory if order delay
                Series dynamic of leadtime
                int: Average period

        Returns:
            SS: Prudent safety stock
        """
        if isinstance(Demand, (pd.Series)):
            D_bar = Demand.mean()
            D_max = Demand.max()
        elif isinstance(Demand, (int, float)):
            D_bar = Demand
            D_max = Demand
        else:
            raise TypeError("Demand should be in integer or pandas series(1 columns) format")

        if isinstance(Leadtime, (pd.Series)):
            L_max = Leadtime.max()
            L_bar = Leadtime.mean()
        elif isinstance(Leadtime, (int, float)):
            L_max = Leadtime
            L_bar = Leadtime
        else:
            raise TypeError("Leadtime should be in integer or pandas series(1 columns) format")

        ss = ((D_max * L_max) - (D_bar * L_bar)).max()
        return math.ceil(ss) ;

    # @markdown Safety Stock Normal Distribution mathod 
    def normdist(Demand, Leadtime = 1, service_level: float = 0.95):
        """ Function return safetystock unit due to dynamic of demand and leadtime and service level priority
        Using Normal Diatribution method with confidance factor

        Args:
            Demand: Average demand in a days (units)
                Series: dynamically demand
                int: constance demand
            Leadtime: Average Leadtime from ordering until recieved orders
                Series: dynamically Leadtime
                int: constance Leadtime
            service_level: confidance Interval to have available stock serve to customers
                Default = 0.95

        Returns:
            safety stock
        """
        if isinstance(Demand, (pd.Series)):
            D_bar = Demand.mean()
            D_std = Demand.std(ddof=0)
        elif isinstance(Demand, (int, float)):
            D_bar = Demand
            D_std = 0
        else:
            raise TypeError("Demand should be in integer or pandas series(1 columns) format")

        if isinstance(Leadtime, (pd.Series)):
            L_bar = Leadtime.mean()
            L_sd = Leadtime.std(ddof=0)
        elif isinstance(Leadtime, (int, float)):
            L_bar = Leadtime
            L_sd = 0
        else:
            raise TypeError("Demand should be in integer or pandas series(1 columns) format")

        if service_level < 1:
            pass
        elif service_level > 1 and service_level < 100:
            service_level = service_level/100
        else:
            raise ValueError("Service level should be in proportion of 100")

        z_score = stats.norm.ppf(service_level)
        ss = (z_score * math.sqrt((L_bar*(D_std**2)) + ((D_bar**2)*(L_sd**2)))).max()
        return ss ;

assert SafetyStock.simple(Demand=pd.Series([900,1000,800,1100,900,1200,900,1100,1100,1000,800,1200]), Safety_day=15) == 15000
assert SafetyStock.simple(Demand=pd.Series([32.8]), Safety_day=15) == 492

assert SafetyStock.max(Demand=pd.Series([30,33,26,36,30,39,30,36,36,33,26,39]), Leadtime=pd.Series([38,37,38,40,33,28,37,36,36,27])) == 411
assert SafetyStock.max(Demand=33, Leadtime=pd.Series([38,37,38,40,33,28,37,36,36,27])) == 165
assert SafetyStock.max(Demand=pd.Series([30,33,26,36,30,39,30,36,36,33,26,39]), Leadtime = 35) == 216

assert math.ceil(SafetyStock.normdist(pd.Series([11,11,11,11,10]), service_level=0.95)) == 1
assert math.ceil(SafetyStock.normdist(Demand=20, Leadtime=2)) == 0
assert math.ceil(SafetyStock.normdist(Demand=20, Leadtime=pd.Series([4, 8, 6]), service_level= 90)) == 42
assert math.ceil(SafetyStock.normdist(Demand=pd.Series([50, 35, 20]), Leadtime=pd.Series([2, 1, 3]), service_level=80)) == 29
print("done")