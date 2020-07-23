from typing import List
from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = defaultdict(set)
        self.followee = defaultdict(set)
        self.num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].add((self.num, tweetId))
        self.num += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        post = self.posts[userId].copy()
        for followeeId in self.followee[userId]:
            post.update(self.posts[followeeId])
        # for i in range(len(post)):
        # 排序
        post = list(post)
        post.sort(key=lambda x: x[0], reverse=True)
        tweets = [tweetId for _, tweetId in post]
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:

        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId is not followerId:
            self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followee[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
# obj.postTweet(1, 3)
# obj.postTweet(1, 4)
# obj.postTweet(1, 5)
# obj.postTweet(1, 6)
# obj.postTweet(1, 7)
obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
obj.getNewsFeed(1)
obj.unfollow(1, 2)
obj.getNewsFeed(1)