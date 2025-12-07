"""
355. Design Twitter
Difficulty: Medium

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
  Each call to this function will be made with a unique tweetId.
- List[int] getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
  Each item in the news feed must be posted by users who the user followed or by the user themself. 
  Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user 
  with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the 
  user with ID followeeId.

Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

Notes:
- Key insight: Use a min-heap to maintain top 10 most recent tweets, then sort in reverse.
- Store tweets with timestamps to track recency.
- Use defaultdict for efficient user/tweet storage.
- Time complexity: O(1) postTweet, O(n * log 10) getNewsFeed where n is total tweets, O(1) follow/unfollow
- Space complexity: O(n + m) where n is tweets, m is follow relationships
- Alternative approaches:
  - Min-heap with size limit: O(n * log 10) time - current approach (optimal)
  - Max-heap with negative timestamps: O(n * log 10) time - similar efficiency
  - Merge k sorted lists: O(n * log k) where k is users - more complex
  - Collect all then sort: O(n log n) time - less efficient for large n
- Edge cases: User follows themselves, unfollow non-existent, empty news feed, single user
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
    Approach 1: Min-Heap with Size Limit (Current)
    Time Complexity: O(1) postTweet, O(n * log 10) getNewsFeed, O(1) follow/unfollow
    Space Complexity: O(n + m) where n=tweets, m=follow relationships
    
    Use min-heap to maintain top 10 most recent tweets, then sort in reverse order.
    """
    
    def __init__(self):
        """
        Initialize your Twitter object.
        """
        self.subscriptions = defaultdict(set)  # followerId -> set of followeeIds
        self.tweets = defaultdict(list)  # userId -> list of (tweetId, timestamp)
        self.timestamp = 0  # Global timestamp counter

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        
        Args:
            userId: ID of the user posting the tweet
            tweetId: ID of the tweet
        """
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        Tweets must be ordered from most recent to least recent.
        
        Args:
            userId: ID of the user
            
        Returns:
            List of tweet IDs (most recent first, max 10)
        """
        min_heap = []  # Min-heap to keep top 10 most recent tweets
        users = set(self.subscriptions[userId])  # Users being followed
        users.add(userId)  # Include own tweets

        # Collect tweets from all relevant users
        for user in users:
            for tweetId, time in self.tweets[user]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (time, tweetId))
                else:
                    # Replace smallest (oldest) if current is more recent
                    heapq.heapreplace(min_heap, (time, tweetId))

        # Sort in reverse order (most recent first)
        min_heap.sort(reverse=True)

        return [tweetId for _, tweetId in min_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        
        Args:
            followerId: ID of the follower
            followeeId: ID of the user to follow
        """
        if followerId != followeeId:
            self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        
        Args:
            followerId: ID of the follower
            followeeId: ID of the user to unfollow
        """
        self.subscriptions[followerId].discard(followeeId)


class TwitterMaxHeap:
    """
    Approach 2: Alternative Min-Heap Implementation
    Time Complexity: O(1) postTweet, O(n * log 10) getNewsFeed, O(1) follow/unfollow
    Space Complexity: O(n + m)
    
    Same logic as Approach 1 but with slightly different structure.
    Uses min-heap to maintain top 10 most recent tweets.
    """
    
    def __init__(self):
        self.subscriptions = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []  # Min-heap to keep top 10 most recent (same as approach 1)
        users = set(self.subscriptions[userId])
        users.add(userId)

        for user in users:
            for tweetId, time in self.tweets[user]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (time, tweetId))
                else:
                    # Replace if current tweet is more recent than oldest in heap
                    if time > min_heap[0][0]:
                        heapq.heapreplace(min_heap, (time, tweetId))

        # Sort by timestamp (descending) and extract tweetIds
        min_heap.sort(reverse=True)
        return [tweetId for _, tweetId in min_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].discard(followeeId)


class TwitterCollectSort:
    """
    Approach 3: Collect All Then Sort (Less Efficient)
    Time Complexity: O(1) postTweet, O(n log n) getNewsFeed, O(1) follow/unfollow
    Space Complexity: O(n + m)
    
    Collect all tweets, sort, then take top 10. Simpler but less efficient for large n.
    """
    
    def __init__(self):
        self.subscriptions = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        users = set(self.subscriptions[userId])
        users.add(userId)

        for user in users:
            all_tweets.extend(self.tweets[user])

        # Sort by timestamp (descending) and take top 10
        all_tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweetId for tweetId, _ in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].discard(followeeId)


def test_solution():
    """Test cases for the solution"""
    
    # Test case 1: Basic example from problem
    print("Test 1: Basic example from problem")
    twitter1 = Twitter()
    twitter1.postTweet(1, 5)
    result1a = twitter1.getNewsFeed(1)
    expected1a = [5]
    assert result1a == expected1a, f"Test 1a failed: expected {expected1a}, got {result1a}"
    print(f"  After postTweet(1, 5): {result1a} ✓")
    
    twitter1.follow(1, 2)
    twitter1.postTweet(2, 6)
    result1b = twitter1.getNewsFeed(1)
    expected1b = [6, 5]
    assert result1b == expected1b, f"Test 1b failed: expected {expected1b}, got {result1b}"
    print(f"  After follow and postTweet(2, 6): {result1b} ✓")
    
    twitter1.unfollow(1, 2)
    result1c = twitter1.getNewsFeed(1)
    expected1c = [5]
    assert result1c == expected1c, f"Test 1c failed: expected {expected1c}, got {result1c}"
    print(f"  After unfollow: {result1c} ✓")
    
    # Test case 2: Compare all approaches
    print("\nTest 2: Comparing all approaches")
    test_operations = [
        ("postTweet", 1, 5),
        ("postTweet", 2, 6),
        ("follow", 1, 2),
        ("postTweet", 2, 7),
    ]
    
    twitter_a = Twitter()
    twitter_b = TwitterMaxHeap()
    twitter_c = TwitterCollectSort()
    
    for op, *args in test_operations:
        if op == "postTweet":
            userId, tweetId = args
            twitter_a.postTweet(userId, tweetId)
            twitter_b.postTweet(userId, tweetId)
            twitter_c.postTweet(userId, tweetId)
        elif op == "follow":
            followerId, followeeId = args
            twitter_a.follow(followerId, followeeId)
            twitter_b.follow(followerId, followeeId)
            twitter_c.follow(followerId, followeeId)
        elif op == "unfollow":
            followerId, followeeId = args
            twitter_a.unfollow(followerId, followeeId)
            twitter_b.unfollow(followerId, followeeId)
            twitter_c.unfollow(followerId, followeeId)
    
    result_a = twitter_a.getNewsFeed(1)
    result_b = twitter_b.getNewsFeed(1)
    result_c = twitter_c.getNewsFeed(1)
    
    assert result_a == result_b == result_c, f"Mismatch: {result_a} vs {result_b} vs {result_c}"
    print(f"  All approaches match: {result_a} ✓")
    
    # Test case 3: Empty news feed
    print("\nTest 3: Empty news feed")
    twitter3 = Twitter()
    result3 = twitter3.getNewsFeed(1)
    expected3 = []
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print(f"  Result: {result3} ✓")
    
    # Test case 4: Single user, multiple tweets
    print("Test 4: Single user, multiple tweets")
    twitter4 = Twitter()
    for i in range(1, 6):
        twitter4.postTweet(1, i)
    result4 = twitter4.getNewsFeed(1)
    expected4 = [5, 4, 3, 2, 1]  # Most recent first
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print(f"  Result: {result4} ✓")
    
    # Test case 5: More than 10 tweets
    print("Test 5: More than 10 tweets (should return only 10)")
    twitter5 = Twitter()
    for i in range(1, 16):
        twitter5.postTweet(1, i)
    result5 = twitter5.getNewsFeed(1)
    assert len(result5) == 10, f"Test 5 failed: expected length 10, got {len(result5)}"
    assert result5 == [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], f"Test 5 failed: wrong tweets"
    print(f"  Result length: {len(result5)}, most recent: {result5[0]} ✓")
    
    # Test case 6: Follow multiple users
    print("Test 6: Follow multiple users")
    twitter6 = Twitter()
    twitter6.postTweet(1, 1)
    twitter6.postTweet(2, 2)
    twitter6.postTweet(3, 3)
    twitter6.follow(1, 2)
    twitter6.follow(1, 3)
    result6 = twitter6.getNewsFeed(1)
    assert len(result6) == 3, f"Test 6 failed: expected length 3, got {len(result6)}"
    assert set(result6) == {1, 2, 3}, f"Test 6 failed: wrong tweets {result6}"
    print(f"  Result: {result6} ✓")
    
    # Test case 7: Unfollow non-existent user
    print("Test 7: Unfollow non-existent user")
    twitter7 = Twitter()
    twitter7.postTweet(1, 1)
    twitter7.unfollow(1, 2)  # User 2 not followed
    result7 = twitter7.getNewsFeed(1)
    expected7 = [1]
    assert result7 == expected7, f"Test 7 failed: expected {expected7}, got {result7}"
    print(f"  Result: {result7} ✓")
    
    # Test case 8: Follow self (should be no-op)
    print("Test 8: Follow self (should be no-op)")
    twitter8 = Twitter()
    twitter8.postTweet(1, 1)
    twitter8.follow(1, 1)  # Follow self
    result8 = twitter8.getNewsFeed(1)
    expected8 = [1]
    assert result8 == expected8, f"Test 8 failed: expected {expected8}, got {result8}"
    print(f"  Result: {result8} ✓")
    
    # Test case 9: Multiple tweets from different users
    print("Test 9: Multiple tweets from different users")
    twitter9 = Twitter()
    twitter9.postTweet(1, 1)
    twitter9.postTweet(2, 2)
    twitter9.postTweet(1, 3)
    twitter9.postTweet(2, 4)
    twitter9.follow(1, 2)
    result9 = twitter9.getNewsFeed(1)
    expected9 = [4, 3, 2, 1]  # Most recent first
    assert result9 == expected9, f"Test 9 failed: expected {expected9}, got {result9}"
    print(f"  Result: {result9} ✓")
    
    # Test case 10: Unfollow then get feed
    print("Test 10: Unfollow then get feed")
    twitter10 = Twitter()
    twitter10.postTweet(1, 1)
    twitter10.postTweet(2, 2)
    twitter10.follow(1, 2)
    twitter10.unfollow(1, 2)
    result10 = twitter10.getNewsFeed(1)
    expected10 = [1]  # Should not include user 2's tweets
    assert result10 == expected10, f"Test 10 failed: expected {expected10}, got {result10}"
    print(f"  Result: {result10} ✓")
    
    # Test case 11: Many users, many tweets
    print("Test 11: Many users, many tweets")
    twitter11 = Twitter()
    for i in range(1, 6):
        twitter11.postTweet(i, i * 10)
    twitter11.follow(1, 2)
    twitter11.follow(1, 3)
    twitter11.follow(1, 4)
    result11 = twitter11.getNewsFeed(1)
    assert len(result11) == 4, f"Test 11 failed: expected length 4, got {len(result11)}"
    assert set(result11) == {10, 20, 30, 40}, f"Test 11 failed: wrong tweets {result11}"
    print(f"  Result: {result11} ✓")
    
    # Test case 12: Timestamp ordering
    print("Test 12: Timestamp ordering")
    twitter12 = Twitter()
    twitter12.postTweet(1, 1)
    twitter12.postTweet(2, 2)
    twitter12.postTweet(1, 3)
    twitter12.follow(1, 2)
    result12 = twitter12.getNewsFeed(1)
    # Should be ordered by timestamp: 3 (most recent), then 2, then 1
    expected12 = [3, 2, 1]
    assert result12 == expected12, f"Test 12 failed: expected {expected12}, got {result12}"
    print(f"  Result: {result12} ✓")
    
    # Test case 13: Follow/unfollow multiple times
    print("Test 13: Follow/unfollow multiple times")
    twitter13 = Twitter()
    twitter13.postTweet(2, 1)
    twitter13.follow(1, 2)
    twitter13.unfollow(1, 2)
    twitter13.follow(1, 2)
    twitter13.postTweet(2, 2)
    result13 = twitter13.getNewsFeed(1)
    # When you follow a user, you see all their tweets (not just ones posted after following)
    expected13 = [2, 1]  # Both tweets from user 2, most recent first
    assert result13 == expected13, f"Test 13 failed: expected {expected13}, got {result13}"
    print(f"  Result: {result13} ✓")
    
    # Test case 14: Edge case - user with no tweets
    print("Test 14: User with no tweets")
    twitter14 = Twitter()
    twitter14.postTweet(2, 1)
    twitter14.follow(1, 2)
    result14 = twitter14.getNewsFeed(1)
    expected14 = [1]
    assert result14 == expected14, f"Test 14 failed: expected {expected14}, got {result14}"
    print(f"  Result: {result14} ✓")
    
    # Test case 15: Complex scenario
    print("Test 15: Complex scenario")
    twitter15 = Twitter()
    twitter15.postTweet(1, 1)
    twitter15.postTweet(2, 2)
    twitter15.postTweet(3, 3)
    twitter15.follow(1, 2)
    twitter15.follow(1, 3)
    twitter15.postTweet(2, 4)
    twitter15.postTweet(3, 5)
    twitter15.unfollow(1, 3)
    result15 = twitter15.getNewsFeed(1)
    # Should have: 4 (user 2, most recent), 2 (user 2), 1 (user 1)
    # Should NOT have: 3, 5 (user 3, unfollowed)
    expected15 = [4, 2, 1]
    assert result15 == expected15, f"Test 15 failed: expected {expected15}, got {result15}"
    print(f"  Result: {result15} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()
