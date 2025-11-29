"""
1396. Design Underground System
Difficulty: Medium

An underground railway system is keeping track of customer travel times between different stations. 
They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

- void checkIn(int id, string stationName, int t)
  A customer with a card ID equal to id, checks in at the station stationName at time t.
  A customer can only be checked into one place at a time.

- void checkOut(int id, string stationName, int t)
  A customer with a card ID equal to id, checks out from the station stationName at time t.

- double getAverageTime(string startStation, string endStation)
  Returns the average time it takes to travel from startStation to endStation.
  The average time is computed from all the previous traveling times from startStation to endStation 
  that happened directly, meaning a check in at startStation followed by a check out from endStation.
  The time it takes to travel from startStation to endStation may be different from the time it takes 
  to travel from endStation to startStation.
  There will be at least one customer that has traveled from startStation to endStation before 
  getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in 
at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

Example 1:
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45: Leyton -> Waterloo in 12 minutes
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27: Leyton -> Waterloo in 10 minutes
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32: Paradise -> Cambridge in 14 minutes
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.0 (1 trip: 14 minutes)
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.0 (2 trips: 12 + 10 = 22 / 2 = 11)
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10: Leyton -> Waterloo in 14 minutes
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.0 (3 trips: 12 + 10 + 14 = 36 / 3 = 12)

Constraints:
- 1 <= id, t <= 10^6
- 1 <= stationName.length, startStation.length, endStation.length <= 10
- All strings consist of uppercase and lowercase English letters and digits.
- There will be at least one call to getAverageTime.
- At most 2 * 10^4 calls will be made to checkIn, checkOut, and getAverageTime.

Notes:
- Key insight: Use two hash maps - one for active trips, one for route statistics.
- Active trips: Map customer ID to (start_station, start_time)
- Route statistics: Map (start_station, end_station) to (total_time, trip_count)
- Time complexity: O(1) for all operations
- Space complexity: O(n + m) where n is number of active trips, m is number of unique routes
- Alternative approaches:
  - Two hash maps: O(1) time, O(n + m) space - current approach
  - List of trips: O(1) checkIn/checkOut, O(k) getAverageTime where k is trips for route
  - Separate total and count: O(1) time, O(n + m) space - store separately
- Edge cases: Single trip, multiple trips same route, same customer multiple trips, no trips for route
"""

from collections import defaultdict
from typing import Dict, Tuple


class UndergroundSystem:
    """
    Approach 1: Two Hash Maps (Current)
    Time Complexity: O(1) for all operations
    Space Complexity: O(n + m) where n=active trips, m=unique routes
    
    Use two hash maps:
    1. trips: customer_id -> (start_station, start_time)
    2. times: (start_station, end_station) -> (total_time, trip_count)
    """
    def __init__(self):
        # Maps customer id to (check-in station, check-in time)
        self.trips: Dict[int, Tuple[str, int]] = {}
        # Maps (start_station, end_station) to (total_time, trip_count)
        self.times: Dict[Tuple[str, str], Tuple[float, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """Store the check-in info for this customer"""
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """Calculate travel time and update route statistics"""
        start_station, start_time = self.trips[id]
        travel_time = t - start_time
        route = (start_station, stationName)

        if route in self.times:
            total_time, count = self.times[route]
            self.times[route] = (total_time + travel_time, count + 1)
        else:
            self.times[route] = (travel_time, 1)

        del self.trips[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        """Return average travel time for the route"""
        route = (startStation, endStation)
        total_time, count = self.times[route]
        return total_time / count


class UndergroundSystemSeparate:
    """
    Approach 2: Separate Total and Count Maps
    Time Complexity: O(1) for all operations
    Space Complexity: O(n + m)
    
    Store total time and count in separate maps for clarity.
    """
    def __init__(self):
        self.trips: Dict[int, Tuple[str, int]] = {}
        self.route_totals: Dict[Tuple[str, str], float] = {}
        self.route_counts: Dict[Tuple[str, str], int] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.trips[id]
        travel_time = t - start_time
        route = (start_station, stationName)

        self.route_totals[route] = self.route_totals.get(route, 0) + travel_time
        self.route_counts[route] = self.route_counts.get(route, 0) + 1

        del self.trips[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.route_totals[route] / self.route_counts[route]


class UndergroundSystemDefaultDict:
    """
    Approach 3: Using DefaultDict
    Time Complexity: O(1) for all operations
    Space Complexity: O(n + m)
    
    Use defaultdict to simplify initialization logic.
    """
    def __init__(self):
        self.trips: Dict[int, Tuple[str, int]] = {}
        self.times: Dict[Tuple[str, str], Tuple[float, int]] = defaultdict(lambda: (0.0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.trips[id]
        travel_time = t - start_time
        route = (start_station, stationName)

        total_time, count = self.times[route]
        self.times[route] = (total_time + travel_time, count + 1)

        del self.trips[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.times[route]
        return total_time / count


class UndergroundSystemListBased:
    """
    Approach 4: List-Based (Less Efficient)
    Time Complexity: O(1) checkIn/checkOut, O(k) getAverageTime where k=trips for route
    Space Complexity: O(n + m)
    
    Store all trips in a list. Less efficient for getAverageTime but simpler conceptually.
    """
    def __init__(self):
        self.trips: Dict[int, Tuple[str, int]] = {}
        self.completed_trips: list = []  # List of (start_station, end_station, travel_time)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.trips[id]
        travel_time = t - start_time
        self.completed_trips.append((start_station, stationName, travel_time))
        del self.trips[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_times = [
            travel_time for start, end, travel_time in self.completed_trips
            if start == startStation and end == endStation
        ]
        return sum(route_times) / len(route_times)


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    system1 = UndergroundSystem()
    system1.checkIn(45, "Leyton", 3)
    system1.checkIn(32, "Paradise", 8)
    system1.checkIn(27, "Leyton", 10)
    system1.checkOut(45, "Waterloo", 15)  # 12 minutes
    system1.checkOut(27, "Waterloo", 20)  # 10 minutes
    system1.checkOut(32, "Cambridge", 22)  # 14 minutes
    
    result1a = system1.getAverageTime("Paradise", "Cambridge")
    expected1a = 14.0
    assert abs(result1a - expected1a) < 0.0001, f"Test 1a failed: expected {expected1a}, got {result1a}"
    print(f"  Paradise->Cambridge: {result1a} ✓")
    
    result1b = system1.getAverageTime("Leyton", "Waterloo")
    expected1b = 11.0  # (12 + 10) / 2
    assert abs(result1b - expected1b) < 0.0001, f"Test 1b failed: expected {expected1b}, got {result1b}"
    print(f"  Leyton->Waterloo: {result1b} ✓")
    
    system1.checkIn(10, "Leyton", 24)
    result1c = system1.getAverageTime("Leyton", "Waterloo")
    assert abs(result1c - expected1b) < 0.0001, f"Test 1c failed: expected {expected1b}, got {result1c}"
    print(f"  Leyton->Waterloo (after checkIn): {result1c} ✓")
    
    system1.checkOut(10, "Waterloo", 38)  # 14 minutes
    result1d = system1.getAverageTime("Leyton", "Waterloo")
    expected1d = 12.0  # (12 + 10 + 14) / 3
    assert abs(result1d - expected1d) < 0.0001, f"Test 1d failed: expected {expected1d}, got {result1d}"
    print(f"  Leyton->Waterloo (after 3 trips): {result1d} ✓")
    
    # Test case 2: Single trip
    print("\nTest 2: Single trip")
    system2 = UndergroundSystem()
    system2.checkIn(1, "A", 10)
    system2.checkOut(1, "B", 20)
    result2 = system2.getAverageTime("A", "B")
    expected2 = 10.0
    assert abs(result2 - expected2) < 0.0001, f"Test 2 failed: expected {expected2}, got {result2}"
    print(f"  Result: {result2} ✓")
    
    # Test case 3: Multiple trips same route
    print("Test 3: Multiple trips same route")
    system3 = UndergroundSystem()
    system3.checkIn(1, "A", 0)
    system3.checkOut(1, "B", 10)  # 10 minutes
    system3.checkIn(2, "A", 20)
    system3.checkOut(2, "B", 25)  # 5 minutes
    system3.checkIn(3, "A", 30)
    system3.checkOut(3, "B", 45)  # 15 minutes
    result3 = system3.getAverageTime("A", "B")
    expected3 = (10 + 5 + 15) / 3  # 10.0
    assert abs(result3 - expected3) < 0.0001, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Same customer multiple trips
    print("Test 4: Same customer multiple trips")
    system4 = UndergroundSystem()
    system4.checkIn(1, "A", 0)
    system4.checkOut(1, "B", 10)
    system4.checkIn(1, "A", 20)
    system4.checkOut(1, "B", 25)
    result4 = system4.getAverageTime("A", "B")
    expected4 = (10 + 5) / 2  # 7.5
    assert abs(result4 - expected4) < 0.0001, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: Compare all approaches
    print("\nTest 5: Comparing all approaches")
    operations = [
        ("checkIn", 1, "A", 0),
        ("checkOut", 1, "B", 10),
        ("checkIn", 2, "A", 20),
        ("checkOut", 2, "B", 25),
        ("getAverageTime", "A", "B"),
    ]
    
    system_a = UndergroundSystem()
    system_b = UndergroundSystemSeparate()
    system_c = UndergroundSystemDefaultDict()
    
    for op, *args in operations:
        if op == "checkIn":
            id, station, t = args
            system_a.checkIn(id, station, t)
            system_b.checkIn(id, station, t)
            system_c.checkIn(id, station, t)
        elif op == "checkOut":
            id, station, t = args
            system_a.checkOut(id, station, t)
            system_b.checkOut(id, station, t)
            system_c.checkOut(id, station, t)
        elif op == "getAverageTime":
            start, end = args
            result_a = system_a.getAverageTime(start, end)
            result_b = system_b.getAverageTime(start, end)
            result_c = system_c.getAverageTime(start, end)
            assert abs(result_a - result_b) < 0.0001, f"Mismatch: {result_a} vs {result_b}"
            assert abs(result_a - result_c) < 0.0001, f"Mismatch: {result_a} vs {result_c}"
    
    print("  All approaches match! ✓")
    
    # Test case 6: Different routes
    print("\nTest 6: Different routes")
    system6 = UndergroundSystem()
    system6.checkIn(1, "A", 0)
    system6.checkOut(1, "B", 10)  # A->B: 10
    system6.checkIn(2, "B", 20)
    system6.checkOut(2, "A", 30)  # B->A: 10
    assert abs(system6.getAverageTime("A", "B") - 10.0) < 0.0001, "Test 6a failed"
    assert abs(system6.getAverageTime("B", "A") - 10.0) < 0.0001, "Test 6b failed"
    print("  Result: Different routes tracked separately ✓")
    
    # Test case 7: Zero travel time
    print("Test 7: Zero travel time")
    system7 = UndergroundSystem()
    system7.checkIn(1, "A", 10)
    system7.checkOut(1, "B", 10)
    result7 = system7.getAverageTime("A", "B")
    assert abs(result7 - 0.0) < 0.0001, f"Test 7 failed: expected 0.0, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Large travel time
    print("Test 8: Large travel time")
    system8 = UndergroundSystem()
    system8.checkIn(1, "A", 0)
    system8.checkOut(1, "B", 1000000)
    result8 = system8.getAverageTime("A", "B")
    assert abs(result8 - 1000000.0) < 0.0001, f"Test 8 failed: expected 1000000.0, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Many trips same route
    print("Test 9: Many trips same route")
    system9 = UndergroundSystem()
    for i in range(100):
        system9.checkIn(i, "A", i * 10)
        system9.checkOut(i, "B", i * 10 + 5)
    result9 = system9.getAverageTime("A", "B")
    assert abs(result9 - 5.0) < 0.0001, f"Test 9 failed: expected 5.0, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Multiple routes
    print("Test 10: Multiple routes")
    system10 = UndergroundSystem()
    system10.checkIn(1, "A", 0)
    system10.checkOut(1, "B", 10)
    system10.checkIn(2, "B", 20)
    system10.checkOut(2, "C", 30)
    system10.checkIn(3, "C", 40)
    system10.checkOut(3, "D", 50)
    
    assert abs(system10.getAverageTime("A", "B") - 10.0) < 0.0001, "Test 10a failed"
    assert abs(system10.getAverageTime("B", "C") - 10.0) < 0.0001, "Test 10b failed"
    assert abs(system10.getAverageTime("C", "D") - 10.0) < 0.0001, "Test 10c failed"
    print("  Result: Multiple routes tracked correctly ✓")
    
    # Test case 11: Same station check-in/out
    print("Test 11: Same station check-in/out")
    system11 = UndergroundSystem()
    system11.checkIn(1, "A", 0)
    system11.checkOut(1, "A", 5)
    result11 = system11.getAverageTime("A", "A")
    assert abs(result11 - 5.0) < 0.0001, f"Test 11 failed: expected 5.0, got {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Varying travel times
    print("Test 12: Varying travel times")
    system12 = UndergroundSystem()
    times = [10, 20, 30, 40, 50]
    for i, travel_time in enumerate(times):
        system12.checkIn(i, "A", i * 100)
        system12.checkOut(i, "B", i * 100 + travel_time)
    result12 = system12.getAverageTime("A", "B")
    expected12 = sum(times) / len(times)  # 30.0
    assert abs(result12 - expected12) < 0.0001, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Concurrent check-ins
    print("Test 13: Concurrent check-ins")
    system13 = UndergroundSystem()
    system13.checkIn(1, "A", 0)
    system13.checkIn(2, "B", 0)
    system13.checkIn(3, "C", 0)
    system13.checkOut(1, "D", 10)
    system13.checkOut(2, "E", 20)
    system13.checkOut(3, "F", 30)
    
    assert abs(system13.getAverageTime("A", "D") - 10.0) < 0.0001, "Test 13a failed"
    assert abs(system13.getAverageTime("B", "E") - 20.0) < 0.0001, "Test 13b failed"
    assert abs(system13.getAverageTime("C", "F") - 30.0) < 0.0001, "Test 13c failed"
    print("  Result: Concurrent check-ins handled correctly ✓")
    
    # Test case 14: Long sequence
    print("Test 14: Long sequence")
    system14 = UndergroundSystem()
    for i in range(50):
        system14.checkIn(i, "Start", i)
        system14.checkOut(i, "End", i + 5)
    result14 = system14.getAverageTime("Start", "End")
    assert abs(result14 - 5.0) < 0.0001, f"Test 14 failed: expected 5.0, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex scenario
    print("Test 15: Complex scenario")
    system15 = UndergroundSystem()
    # Multiple routes with varying frequencies
    system15.checkIn(1, "A", 0)
    system15.checkOut(1, "B", 10)
    system15.checkIn(2, "A", 20)
    system15.checkOut(2, "B", 25)
    system15.checkIn(3, "A", 30)
    system15.checkOut(3, "B", 45)
    system15.checkIn(4, "B", 50)
    system15.checkOut(4, "C", 60)
    system15.checkIn(5, "B", 70)
    system15.checkOut(5, "C", 75)
    
    result15a = system15.getAverageTime("A", "B")
    expected15a = (10 + 5 + 15) / 3  # 10.0
    assert abs(result15a - expected15a) < 0.0001, f"Test 15a failed"
    
    result15b = system15.getAverageTime("B", "C")
    expected15b = (10 + 5) / 2  # 7.5
    assert abs(result15b - expected15b) < 0.0001, f"Test 15b failed"
    
    print(f"  A->B: {result15a}, B->C: {result15b} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()