"""
PROBLEM:

PART 1:
Food delivery companies employ tens of thousands of delivery drivers who each submit hundreds of deliveries per week.
Delivery details are automatically sent to the system immediately after the delivery.
Delivery drivers are paid per delivery based on the time each delivery takes.
The exact rate paid per delivery varies per driver, based on their performance.
If a driver is paid $10.00 per hour, and a delivery takes 1 hour and 30 minutes, the driver is paid $15.00 for that delivery.
We are building a dashboard to show a single number - the total cost of all deliveries - on screens in the accounting department offices.
At first, we want the following functions:
* `add_driver(driver_id [integer], usd_hourly_rate_per_delivery [float])`
   - The given driver will not already be in the system
   - The hourly rate applies per delivery, so a driver can be paid multiples of this rate per hour for simultaneous deliveries
* `record_delivery(driver_id [integer], start_time, end_time)`
   - Discuss the time format you choose
   - Times require minimum one-second precision
   - The given driver will already be in the system
   - All deliveries will be recorded immediately after the delivery is completed
   - No delivery will exceed 3 hours
* `get_total_cost() -> string`
   - Return the total, aggregated cost of all drivers' deliveries recorded in the system, to 2 decimal places
   - For example, return "135.30" if one driver is in the system and has a total cost of 100.30 USD and another driver is in the system and has a total cost of 35.00 USD.
   - This will be used for a live dashboard
All inputs will be valid.
If you do anything differently in this interview than you would in production, share that.
Before you get started coding, and before we start using the AI assistant, let's discuss how you will store the time data and why.
We want to see good OOP practices.

PART 2:
The accounting department now wants to use the live dashboard you built to see how much money is owed in total to all drivers.
Add the following functions:
* `pay_up_to (pay_time)`
   - Pay all drivers for recorded deliveries which ended up to and including the given time
* `get_total_cost_unpaid() -> string`
   - Return the total, aggregated cost of all drivers' deliveries which have not been paid
The solution does not need to be thread-safe or handle concurrency.

Constraints:

Time/Space Complexity:

"""

# ============================================================================
# SOLUTION
# ============================================================================

from datetime import datetime
from typing import Dict


class Delivery:
    """Represents a single delivery"""
    def __init__(self, driver_id: int, start_time: datetime, end_time: datetime, cost: float):
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.cost = cost
        self.is_paid = False
    
    def duration_hours(self) -> float:
        """Calculate delivery duration in hours"""
        duration_seconds = (self.end_time - self.start_time).total_seconds()
        return duration_seconds / 3600

class Driver:
    """Represents a delivery driver"""
    def __init__(self, driver_id: int, hourly_rate: float):
        self.driver_id = driver_id
        self.hourly_rate = hourly_rate
        self.deliveries = []
    
    def calculate_delivery_cost(self, start_time: datetime, end_time: datetime) -> float:
        """Calculate cost for a single delivery"""
        duration_seconds = (end_time - start_time).total_seconds()
        duration_hours = duration_seconds / 3600
        return duration_hours * self.hourly_rate

class DeliverySystem:
    def __init__(self):
        self.drivers: Dict[int, Driver] = {}
        self.deliveries = []
        
        # KEY OPTIMIZATION 1: Cache running totals for O(1) reads
        self.total_cost = 0.0
        self.total_unpaid_cost = 0.0
    
    def add_driver(self, driver_id: int, usd_hourly_rate_per_delivery: float):
        """
        Add a new driver to the system
        Time: O(1)
        """
        if driver_id in self.drivers:
            raise ValueError(f"Driver {driver_id} already exists")
        
        self.drivers[driver_id] = Driver(driver_id, usd_hourly_rate_per_delivery)
    
    def record_delivery(self, driver_id: int, start_time: datetime, end_time: datetime):
        """
        Record a delivery and update running totals
        Time: O(1)
        """
        if driver_id not in self.drivers:
            raise ValueError(f"Driver {driver_id} not found")
        
        driver = self.drivers[driver_id]
        
        # Calculate cost immediately
        cost = driver.calculate_delivery_cost(start_time, end_time)
        
        # Create delivery object
        delivery = Delivery(driver_id, start_time, end_time, cost)
        
        # Update collections
        self.deliveries.append(delivery)
        driver.deliveries.append(delivery)
        
        # KEY OPTIMIZATION: Update running totals in O(1)
        self.total_cost += cost
        self.total_unpaid_cost += cost
    
    def get_total_cost(self) -> str:
        """
        Return total cost of all deliveries
        Time: O(1) - just return cached value
        """
        return f"{self.total_cost:.2f}"
    
    def pay_up_to(self, pay_time: datetime):
        """
        Mark deliveries as paid up to given time
        Time: O(n) where n = number of unpaid deliveries
        KEY OPTIMIZATION 2: Only iterate unpaid deliveries, update running total
        """
        amount_paid = 0.0
        
        for delivery in self.deliveries:
            # Only process unpaid deliveries
            if not delivery.is_paid and delivery.end_time <= pay_time:
                delivery.is_paid = True
                amount_paid += delivery.cost
                
                # Update running unpaid total
                self.total_unpaid_cost -= delivery.cost
        
        return amount_paid
    
    def get_total_cost_unpaid(self) -> str:
        """
        Return total unpaid cost
        Time: O(1) - just return cached value
        """
        return f"{self.total_unpaid_cost:.2f}"


# PART 2 ALTERNATIVE: If pay_up_to() is called frequently, optimize further
class OptimizedDeliverySystem(DeliverySystem):
    """
    Further optimization: Keep separate lists of paid/unpaid deliveries
    Trade-off: More memory, but faster pay_up_to() if only a few deliveries paid each time
    """
    def __init__(self):
        super().__init__()
        self.unpaid_deliveries = []  # Only unpaid deliveries
    
    def record_delivery(self, driver_id: int, start_time: datetime, end_time: datetime):
        """Override to also add to unpaid list"""
        super().record_delivery(driver_id, start_time, end_time)
        self.unpaid_deliveries.append(self.deliveries[-1])
    
    def pay_up_to(self, pay_time: datetime):
        """
        Optimized: Only iterate unpaid deliveries
        Time: O(u) where u = unpaid deliveries (typically u << n)
        """
        amount_paid = 0.0
        still_unpaid = []
        
        for delivery in self.unpaid_deliveries:
            if delivery.end_time <= pay_time:
                delivery.is_paid = True
                amount_paid += delivery.cost
                self.total_unpaid_cost -= delivery.cost
            else:
                still_unpaid.append(delivery)
        
        # Update unpaid list
        self.unpaid_deliveries = still_unpaid
        return amount_paid


# TEST CODE
if __name__ == "__main__":
    system = DeliverySystem()
    
    # Add drivers
    system.add_driver(1, 10.0)  # $10/hour
    system.add_driver(2, 15.0)  # $15/hour
    
    # Record deliveries
    # Driver 1: 1.5 hour delivery = $15.00
    system.record_delivery(
        1, 
        datetime(2026, 1, 20, 10, 0, 0),
        datetime(2026, 1, 20, 11, 30, 0)
    )
    
    # Driver 2: 2 hour delivery = $30.00
    system.record_delivery(
        2,
        datetime(2026, 1, 20, 10, 0, 0),
        datetime(2026, 1, 20, 12, 0, 0)
    )
    
    # Driver 1: 45 min delivery = $7.50
    system.record_delivery(
        1,
        datetime(2026, 1, 20, 14, 0, 0),
        datetime(2026, 1, 20, 14, 45, 0)
    )
    
    print("Total cost:", system.get_total_cost())  # "52.50"
    print("Unpaid cost:", system.get_total_cost_unpaid())  # "52.50"
    
    # Pay deliveries up to 12pm
    system.pay_up_to(datetime(2026, 1, 20, 12, 0, 0))
    
    print("After paying:")
    print("Total cost:", system.get_total_cost())  # "52.50" (unchanged)
    print("Unpaid cost:", system.get_total_cost_unpaid())  # "7.50" (only 2pm delivery unpaid)

        

        

    


# ============================================================================
# TESTS
# ============================================================================

def test_solution():
    # Test 1
    delivery_system = DeliverySystem()
    delivery_system.add_driver(1, 10.00)
    # Convert Unix timestamps (seconds) to datetime objects
    delivery_system.record_delivery(1, datetime.fromtimestamp(3600), datetime.fromtimestamp(7200))
    result = delivery_system.get_total_cost()
    expected = "10.00"
    print(f"Test 1: {result} == {expected}")
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_solution()