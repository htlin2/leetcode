import collections, heapq

class Twitter:

    def __init__(self):
        self.user_tweet = collections.defaultdict(list)
        self.follower_followee = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # hashmap = {userId: [tweetId1, tweetId2]} least recent -> most recent
        self.user_tweet[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # most recent -> least recent limit 10
        followeeIds = self.follower_followee[userId]
        followeeIds.add(userId)
        tweets = []
        for followeeId in followeeIds:
            tweets += self.user_tweet[followeeId]
        heapq.heapify(tweets)
        res = []
        while tweets and len(res) < 10:
            time, tweetId = heapq.heappop(tweets)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # follower_followee = {followerId: set(followeeId)}
        self.follower_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.follower_followee[followerId]:
            return
        self.follower_followee[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
1: [3,5]
"""