# @markdown Minimum lot size function
import math

class LotSize:
    def round_lot_size(x: float, min_size: float =1):
        """
        Function use to perform ceiling quantity to minimum unit in lot

        Args:
            x: Number of demand (unit)
            min_size: Minimum lot size (unit)

        Return:
            Quantity you need to order due to specific minimum lot size
        """
        return min_size * math.ceil(x/min_size);

    def minimum_order_quantity(x: float, min_quantity: float=0):
        if x > min_quantity:
            return x
        else:
            return min_quantity;

assert LotSize.round_lot_size(x=400.65, min_size=5) == 405
assert LotSize.round_lot_size(228, 22.5) == 247.5
assert LotSize.minimum_order_quantity(13.68, 30.5) == 30.5
assert LotSize.minimum_order_quantity(LotSize.round_lot_size(225, 50), 300) == 300
assert LotSize.minimum_order_quantity(LotSize.round_lot_size(225, 50), 200) == 250