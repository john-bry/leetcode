"""
Asteroid API - Retrieve and Sort Asteroid Data
Difficulty: Medium

Retrieve information from an asteroid database using HTTP GET requests. 
Query http://jsonmock.hackerrank.com/api/asteroids to find all records.

Problem Description:
Given an API endpoint that returns paginated asteroid data, implement a function that:
1. Retrieves all asteroids matching a specific orbit class and discovery year
2. Filters asteroids by orbit class (case-insensitive partial match)
3. Filters asteroids by discovery year
4. Sorts the results by period_yr (ascending), then by designation (ascending)
5. Returns a list of asteroid designations

API Structure:
- Base URL: http://jsonmock.hackerrank.com/api/asteroids
- Query parameters: ?parameter={orbitclass}&page={page}
- Response format:
  {
    "page": 1,
    "per_page": 10,
    "total": 202,
    "total_pages": 21,
    "data": [
      {
        "designation": "419880 (2011 AH37)",
        "discovery_date": "2011-01-07",
        "period_yr": "4.06",
        "orbit_class": "Apollo",
        ...
      }
    ]
  }

Example:
Input: year=2010, orbitclass="Apollo"
Output: ["419624 (2010 SO16)", "414772 (2010 OC103)", ...]
(sorted by period_yr, then designation)

Notes:
- Key insight: Paginate through all pages, filter by orbit class and year, then sort.
- Orbit class matching is case-insensitive and uses substring matching.
- Discovery year is extracted from discovery_date (format: "YYYY-MM-DD").
- Sorting: Primary by period_yr (as float), secondary by designation (string).
- Time complexity: O(p * m + n log n) where p=pages, m=asteroids per page, n=matching asteroids
- Space complexity: O(n) for storing filtered asteroids
- Edge cases: Empty results, invalid dates, missing fields, API errors, single page
"""

from typing import Any, Dict, List

import requests


class AsteroidAPI:
    """
    API client for retrieving and processing asteroid data.
    """
    
    def __init__(self, base_url: str = "http://jsonmock.hackerrank.com/api/asteroids"):
        """
        Initialize the AsteroidAPI client.
        
        Args:
            base_url: Base URL for the asteroid API
        """
        self.base_url = base_url

    def get_asteroids_by_orbitclass_and_page(self, orbitclass: str, page: int) -> Dict[str, Any]:
        """
        Retrieve asteroid data for a specific orbit class and page number.
        
        Args:
            orbitclass: Orbit class to filter by
            page: Page number to retrieve
            
        Returns:
            JSON response containing asteroid data
        """
        params = {"parameter": orbitclass, "page": page}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()

    def sort_asteroids(self, year: int, orbitclass: str) -> List[str]:
        """
        Retrieve all asteroids matching the given orbit class and discovery year,
        then sort by period_yr and designation.
        
        Args:
            year: Discovery year to filter by
            orbitclass: Orbit class to filter by (case-insensitive partial match)
            
        Returns:
            List of asteroid designations, sorted by period_yr then designation
        """
        asteroid_list = []
        page = 1

        while True:
            response = self.get_asteroids_by_orbitclass_and_page(orbitclass, page)
            asteroids = response.get("data", [])

            if not asteroids:
                break
            
            for asteroid in asteroids:
                orbit_class = asteroid.get("orbit_class", "")
                discovery_date = asteroid.get("discovery_date", "")
                designation = asteroid.get("designation", "")
                discovery_year = int(discovery_date[:4]) if discovery_date else 0

                # Case-insensitive partial match for orbit class
                if orbitclass.lower() not in orbit_class.lower():
                    continue

                # Only include asteroids with valid non-empty designation and matching year
                if discovery_year == year and designation and designation.strip():
                    asteroid_list.append(asteroid)

            if page >= response.get("total_pages", 1):
                break

            page += 1

        def sort_key(asteroid: Dict[str, Any]) -> tuple:
            """Sort key: (period_yr, designation)"""
            period = float(asteroid.get("period_yr", "1"))
            return (period, asteroid.get("designation", ""))

        asteroid_list.sort(key=sort_key)

        return [asteroid.get("designation", "") for asteroid in asteroid_list if asteroid.get("designation", "").strip()]


def test_solution():
    """Test cases for the solution"""
    import unittest.mock as mock

    # Mock API responses for testing
    mock_response_1 = {
        "page": 1,
        "per_page": 10,
        "total": 15,
        "total_pages": 2,
        "data": [
            {
                "designation": "Asteroid1",
                "discovery_date": "2010-01-15",
                "period_yr": "2.5",
                "orbit_class": "Apollo"
            },
            {
                "designation": "Asteroid2",
                "discovery_date": "2010-06-20",
                "period_yr": "1.8",
                "orbit_class": "Apollo"
            },
            {
                "designation": "Asteroid3",
                "discovery_date": "2011-03-10",
                "period_yr": "3.2",
                "orbit_class": "Apollo"
            }
        ]
    }
    
    mock_response_2 = {
        "page": 2,
        "per_page": 10,
        "total": 15,
        "total_pages": 2,
        "data": [
            {
                "designation": "Asteroid4",
                "discovery_date": "2010-12-05",
                "period_yr": "1.5",
                "orbit_class": "Apollo"
            }
        ]
    }
    
    # Test case 1: Basic functionality
    print("Test 1: Basic functionality - year=2010, orbitclass='Apollo'")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj_1 = mock.Mock()
        mock_response_obj_1.json.return_value = mock_response_1
        mock_response_obj_1.raise_for_status = mock.Mock()
        
        mock_response_obj_2 = mock.Mock()
        mock_response_obj_2.json.return_value = mock_response_2
        mock_response_obj_2.raise_for_status = mock.Mock()
        
        mock_get.side_effect = [mock_response_obj_1, mock_response_obj_2]
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should return sorted by period_yr: 1.5, 1.8, 2.5
        expected = ["Asteroid4", "Asteroid2", "Asteroid1"]
        assert result == expected, f"Test 1 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 2: Empty results
    print("\nTest 2: Empty results - no matching asteroids")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {"page": 1, "total_pages": 1, "data": []}
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2020, "Aten")
        assert result == [], f"Test 2 failed: expected [], got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 3: Single page
    print("Test 3: Single page of results")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        # Create a single-page response
        single_page_response = {
            "page": 1,
            "per_page": 10,
            "total": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid3",
                    "discovery_date": "2011-03-10",
                    "period_yr": "3.2",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.json.return_value = single_page_response
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2011, "Apollo")
        expected = ["Asteroid3"]  # Only 2011 asteroid
        assert result == expected, f"Test 3 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 4: Case-insensitive orbit class matching
    print("Test 4: Case-insensitive orbit class matching")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [{
                "designation": "Asteroid1",
                "discovery_date": "2010-01-01",
                "period_yr": "2.0",
                "orbit_class": "APOLLO"  # Uppercase
            }]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "apollo")  # Lowercase
        expected = ["Asteroid1"]
        assert result == expected, f"Test 4 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 5: Sorting by period_yr then designation
    print("Test 5: Sorting by period_yr then designation")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "B",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "A",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",  # Same period
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "C",
                    "discovery_date": "2010-01-01",
                    "period_yr": "1.0",  # Smaller period
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should be sorted: C (1.0), then A (2.0), then B (2.0)
        expected = ["C", "A", "B"]
        assert result == expected, f"Test 5 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 6: Missing fields
    print("\nTest 6: Missing fields handling")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    # Missing discovery_date
                    "period_yr": "1.5",
                    "orbit_class": "Apollo"
                },
                {
                    # Missing designation
                    "discovery_date": "2010-01-01",
                    "period_yr": "3.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should only include Asteroid1 (has valid date and designation)
        expected = ["Asteroid1"]
        assert result == expected, f"Test 6 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 7: Invalid date format
    print("Test 7: Invalid date format handling")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "invalid-date",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    "discovery_date": "2010-01-01",
                    "period_yr": "1.5",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should only include Asteroid2 (valid date)
        expected = ["Asteroid2"]
        assert result == expected, f"Test 7 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 8: Different orbit classes
    print("Test 8: Different orbit classes")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    "discovery_date": "2010-01-01",
                    "period_yr": "1.5",
                    "orbit_class": "Aten"  # Different class
                },
                {
                    "designation": "Asteroid3",
                    "discovery_date": "2010-01-01",
                    "period_yr": "3.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should only include Apollo asteroids
        expected = ["Asteroid1", "Asteroid3"]
        assert result == expected, f"Test 8 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 9: Year filtering
    print("Test 9: Year filtering")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    "discovery_date": "2011-01-01",
                    "period_yr": "1.5",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid3",
                    "discovery_date": "2010-12-31",
                    "period_yr": "3.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should only include 2010 asteroids
        expected = ["Asteroid1", "Asteroid3"]
        assert result == expected, f"Test 9 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 10: Multiple pages with filtering
    print("Test 10: Multiple pages with filtering")
    with mock.patch('requests.get') as mock_get:
        page1_response = mock.Mock()
        page1_response.json.return_value = {
            "page": 1,
            "total_pages": 2,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    "period_yr": "3.0",
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    "discovery_date": "2011-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        page1_response.raise_for_status = mock.Mock()
        
        page2_response = mock.Mock()
        page2_response.json.return_value = {
            "page": 2,
            "total_pages": 2,
            "data": [
                {
                    "designation": "Asteroid3",
                    "discovery_date": "2010-06-15",
                    "period_yr": "1.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        page2_response.raise_for_status = mock.Mock()
        
        mock_get.side_effect = [page1_response, page2_response]
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Should include Asteroid3 (1.0) and Asteroid1 (3.0), sorted by period
        expected = ["Asteroid3", "Asteroid1"]
        assert result == expected, f"Test 10 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 11: Empty string orbit class
    print("Test 11: Empty string orbit class")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": ""  # Empty orbit class
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "")
        # Empty string should match empty orbit class
        expected = ["Asteroid1"]
        assert result == expected, f"Test 11 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    # Test case 12: Missing period_yr (defaults to "1")
    print("Test 12: Missing period_yr defaults to 1")
    with mock.patch('requests.get') as mock_get:
        mock_response_obj = mock.Mock()
        mock_response_obj.json.return_value = {
            "page": 1,
            "total_pages": 1,
            "data": [
                {
                    "designation": "Asteroid1",
                    "discovery_date": "2010-01-01",
                    # Missing period_yr
                    "orbit_class": "Apollo"
                },
                {
                    "designation": "Asteroid2",
                    "discovery_date": "2010-01-01",
                    "period_yr": "2.0",
                    "orbit_class": "Apollo"
                }
            ]
        }
        mock_response_obj.raise_for_status = mock.Mock()
        mock_get.return_value = mock_response_obj
        
        api = AsteroidAPI()
        result = api.sort_asteroids(2010, "Apollo")
        # Asteroid1 should come first (period defaults to 1.0 < 2.0)
        expected = ["Asteroid1", "Asteroid2"]
        assert result == expected, f"Test 12 failed: expected {expected}, got {result}"
        print(f"  Result: {result} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
