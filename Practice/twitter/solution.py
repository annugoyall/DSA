from collections import defaultdict
from itertools import chain
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following_set = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.counter, tweetId])
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        queue = [userId]
        queue.extend(self.following_set[userId])
        tweets_list = [self.tweets[user] for user in queue]
        tweets_list = list(chain.from_iterable(tweets_list))
        tweets_list.sort(reverse=True)
        l = min(10, len(tweets_list))
        return [tweet[1] for tweet in tweets_list[:l]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following_set[followerId]:
            self.following_set[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_set[followerId]:
            self.following_set[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
print(obj.getNewsFeed(1))
obj.follow(1,2)
obj.postTweet(2,6)
print(obj.getNewsFeed(1))
obj.unfollow(1,2)
print(obj.getNewsFeed(1))