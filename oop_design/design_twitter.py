from collections import defaultdict

class Twitter:
    def __init__(self):
        self.subscriptions = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((tweet_id, self.timestamp))
        self.timestamp += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        min_heap = []
        users = set(self.subscriptions[user_id])

        for user in users:
            for tweet_id, time in self.tweets[user]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (time, tweet_id))
                else:
                    heapq.heapreplace(min_heap, (time, tweet_id))

        min_heap.sort(reverse=True)
        return [tweet_id for _, tweet_id in min_heap]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.subscriptions[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.subscriptions[follower_id].discard(followee_id)


def test_solution():
    twitter = Twitter()
    twitter.post_tweet(1, 5)
    assert twitter.get_news_feed(1) == [5], "Test 1 failed"