from collections import defaultdict
import heapq

def top_users_tweets(data):

    users = defaultdict(int)

    for tweet in data:
        users[tweet["user"]["username"]] += 1

    top_users = heapq.nlargest(10, users.items(), key = lambda x:x[1])

    print(top_users)