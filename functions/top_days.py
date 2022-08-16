from collections import defaultdict
import heapq

def top_days(data):

    days = defaultdict(int)

    for tweet in data:
        date = tweet["date"].split("T")
        days[date[0]] += 1

    top_days = heapq.nlargest(10, days.items(), key = lambda x:x[1])

    print(top_days)

