"""
Let's do one OOP problem focusing on optimization:
Problem: Design a Parking Lot System
Requirements:

Multiple levels (floors)
Different spot sizes: Compact, Regular, Large
Different vehicle types: Motorcycle, Car, Bus

Motorcycle: fits in any spot
Car: fits in Regular or Large
Bus: needs 5 consecutive Large spots


Methods:

parkVehicle(vehicle) - returns spot assignment or null if full
removeVehicle(vehicle) - frees up the spot
getAvailableSpots() - returns count by type



Focus on:

Class design (what classes do you need?)
Optimization (how do you make parkVehicle fast? O(1) lookup?)
Edge cases (what if bus needs spots across levels? what if spots are full?)
"""

# ============================================================================
# SOLUTION
# ============================================================================

from enum import Enum
from typing import Optional, List

# Enums for type safety
class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    BUS = 3

class SpotSize(Enum):
    COMPACT = 1
    REGULAR = 2
    LARGE = 3

# Vehicle class
class Vehicle:
    def __init__(self, vehicle_id: str, vehicle_type: VehicleType):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
    
    def get_spots_needed(self) -> int:
        """Bus needs 5 spots, others need 1"""
        return 5 if self.vehicle_type == VehicleType.BUS else 1
    
    def can_fit_in_spot(self, spot_size: SpotSize) -> bool:
        """
        Motorcycle: fits in any spot
        Car: fits in Regular or Large
        Bus: needs Large only
        """
        if self.vehicle_type == VehicleType.MOTORCYCLE:
            return True
        if self.vehicle_type == VehicleType.CAR:
            return spot_size in [SpotSize.REGULAR, SpotSize.LARGE]
        if self.vehicle_type == VehicleType.BUS:
            return spot_size == SpotSize.LARGE
        return False

# Spot class
class ParkingSpot:
    def __init__(self, spot_id: str, level: int, spot_size: SpotSize, row: int, col: int):
        self.spot_id = spot_id
        self.level = level
        self.spot_size = spot_size
        self.row = row
        self.col = col
        self.vehicle: Optional[Vehicle] = None
    
    def is_available(self) -> bool:
        return self.vehicle is None
    
    def park(self, vehicle: Vehicle) -> bool:
        if not self.is_available():
            return False
        self.vehicle = vehicle
        return True
    
    def remove_vehicle(self) -> Optional[Vehicle]:
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

# Level class
class Level:
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.spots: List[ParkingSpot] = []
        self._init_spots(num_spots)
        
        # KEY OPTIMIZATION: Track available spots by size for O(1) lookup
        self.available_by_size = {
            SpotSize.COMPACT: [],
            SpotSize.REGULAR: [],
            SpotSize.LARGE: []
        }
    
    def _init_spots(self, num_spots: int):
        """Initialize spots in a grid layout"""
        spots_per_row = 10
        for i in range(num_spots):
            row = i // spots_per_row
            col = i % spots_per_row
            
            # Distribute spot sizes: 30% compact, 50% regular, 20% large
            if i % 10 < 3:
                size = SpotSize.COMPACT
            elif i % 10 < 8:
                size = SpotSize.REGULAR
            else:
                size = SpotSize.LARGE
            
            spot = ParkingSpot(f"L{self.floor}-{i}", self.floor, size, row, col)
            self.spots.append(spot)
            self.available_by_size[size].append(spot)
    
    def find_spot_for_vehicle(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        """O(1) lookup using available_by_size"""
        # Try to find a spot that matches vehicle requirements
        if vehicle.vehicle_type == VehicleType.MOTORCYCLE:
            # Try compact first (best fit), then regular, then large
            for size in [SpotSize.COMPACT, SpotSize.REGULAR, SpotSize.LARGE]:
                if self.available_by_size[size]:
                    return self.available_by_size[size][0]
        
        elif vehicle.vehicle_type == VehicleType.CAR:
            # Try regular first, then large
            for size in [SpotSize.REGULAR, SpotSize.LARGE]:
                if self.available_by_size[size]:
                    return self.available_by_size[size][0]
        
        elif vehicle.vehicle_type == VehicleType.BUS:
            # Need 5 consecutive large spots in same row
            return self._find_consecutive_spots(5, SpotSize.LARGE)
        
        return None
    
    def _find_consecutive_spots(self, count: int, size: SpotSize) -> Optional[List[ParkingSpot]]:
        """Find consecutive spots in same row"""
        # Group available spots by row
        spots_by_row = {}
        for spot in self.available_by_size[size]:
            if spot.row not in spots_by_row:
                spots_by_row[spot.row] = []
            spots_by_row[spot.row].append(spot)
        
        # Check each row for consecutive spots
        for row, spots in spots_by_row.items():
            spots.sort(key=lambda s: s.col)  # Sort by column
            
            consecutive = []
            for i, spot in enumerate(spots):
                if i == 0 or spot.col == spots[i-1].col + 1:
                    consecutive.append(spot)
                    if len(consecutive) == count:
                        return consecutive
                else:
                    consecutive = [spot]
        
        return None
    
    def park_vehicle(self, vehicle: Vehicle, spots: List[ParkingSpot]) -> bool:
        """Park vehicle and update available_by_size"""
        for spot in spots:
            spot.park(vehicle)
            self.available_by_size[spot.spot_size].remove(spot)
        return True
    
    def remove_vehicle(self, spots: List[ParkingSpot]) -> bool:
        """Remove vehicle and update available_by_size"""
        for spot in spots:
            spot.remove_vehicle()
            self.available_by_size[spot.spot_size].append(spot)
        return True

# Main ParkingLot class
class ParkingLot:
    def __init__(self, num_levels: int, spots_per_level: int):
        self.levels = [Level(i, spots_per_level) for i in range(num_levels)]
        
        # KEY OPTIMIZATION: Map vehicle to spots for O(1) removal
        self.vehicle_to_spots = {}  # vehicle_id -> List[ParkingSpot]
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        """
        Try to park vehicle on any level
        Time complexity: O(L) where L = number of levels
        """
        # Check if already parked
        if vehicle.vehicle_id in self.vehicle_to_spots:
            print(f"Vehicle {vehicle.vehicle_id} already parked")
            return False
        
        # Try each level
        for level in self.levels:
            if vehicle.vehicle_type == VehicleType.BUS:
                # Bus needs 5 consecutive spots
                spots = level._find_consecutive_spots(5, SpotSize.LARGE)
                if spots:
                    level.park_vehicle(vehicle, spots)
                    self.vehicle_to_spots[vehicle.vehicle_id] = spots
                    print(f"Parked bus {vehicle.vehicle_id} at level {level.floor}, spots {[s.spot_id for s in spots]}")
                    return True
            else:
                # Regular vehicle needs 1 spot
                spot = level.find_spot_for_vehicle(vehicle)
                if spot:
                    level.park_vehicle(vehicle, [spot])
                    self.vehicle_to_spots[vehicle.vehicle_id] = [spot]
                    print(f"Parked {vehicle.vehicle_type.name} {vehicle.vehicle_id} at {spot.spot_id}")
                    return True
        
        print(f"No available spots for {vehicle.vehicle_type.name} {vehicle.vehicle_id}")
        return False
    
    def remove_vehicle(self, vehicle_id: str) -> bool:
        """
        O(1) removal using vehicle_to_spots map
        """
        if vehicle_id not in self.vehicle_to_spots:
            print(f"Vehicle {vehicle_id} not found")
            return False
        
        spots = self.vehicle_to_spots[vehicle_id]
        level = self.levels[spots[0].level]
        level.remove_vehicle(spots)
        del self.vehicle_to_spots[vehicle_id]
        
        print(f"Removed vehicle {vehicle_id}")
        return True
    
    def get_available_spots(self) -> dict:
        """
        Returns count by type across all levels
        """
        counts = {
            SpotSize.COMPACT: 0,
            SpotSize.REGULAR: 0,
            SpotSize.LARGE: 0
        }
        
        for level in self.levels:
            for size in SpotSize:
                counts[size] += len(level.available_by_size[size])
        
        return {size.name: count for size, count in counts.items()}


# Test the system
if __name__ == "__main__":
    # Create parking lot: 3 levels, 30 spots per level
    lot = ParkingLot(num_levels=3, spots_per_level=30)
    
    # Park some vehicles
    motorcycle = Vehicle("M1", VehicleType.MOTORCYCLE)
    car1 = Vehicle("C1", VehicleType.CAR)
    car2 = Vehicle("C2", VehicleType.CAR)
    bus = Vehicle("B1", VehicleType.BUS)
    
    lot.park_vehicle(motorcycle)
    lot.park_vehicle(car1)
    lot.park_vehicle(car2)
    lot.park_vehicle(bus)
    
    # Check available spots
    print("\nAvailable spots:", lot.get_available_spots())
    
    # Remove a vehicle
    lot.remove_vehicle("C1")
    
    # Check available spots again
    print("Available spots after removal:", lot.get_available_spots())
