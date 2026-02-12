class Twitter:
    timestamp = 0

    class Tweet:
        def __init__(self, tweetId):
            self.id = tweetId
            self.time = Twitter.timestamp
            Twitter.timestamp += 1
            self.next = None

    class User:
        def __init__(self, userId):
            self.id = userId
            self.followed = set()
            self.tweetHead = None

            self.follow(userId)

        def follow(self, userId):
            self.followed.add(userId)
        
        def unfollow(self, userId):
            if userId != self.id:
                self.followed.discard(userId)
        
        def post(self, tweetId):
            tweet = Twitter.Tweet(tweetId)
            tweet.next = self.tweetHead
            self.tweetHead = tweet

    def __init__(self):
        self.userMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMap:
            self.userMap[userId] = self.User(userId)
        
        self.userMap[userId].post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.userMap:
            return []
        
        newsFeed = []
        heap = []

        followedUsers = self.userMap[userId].followed

        for user in followedUsers:
            if user in self.userMap:
                tweet = self.userMap[user].tweetHead
                if tweet:
                    heapq.heappush(heap, (-tweet.time, tweet))

        count = 0

        while heap and count < 10:
            time, tweet = heapq.heappop(heap)
            newsFeed.append(tweet.id)
            count += 1
            if tweet.next:
                heapq.heappush(heap, (-tweet.next.time, tweet.next))
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            self.userMap[followerId] = self.User(followerId)
        
        if followeeId not in self.userMap:
            self.userMap[followeeId] = self.User(followeeId)
        
        self.userMap[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap:
            self.userMap[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)