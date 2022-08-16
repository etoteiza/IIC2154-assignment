import heapq
import re
from collections import defaultdict
import heapq

def top_hashtags(data):
    ht = defaultdict(int)

    for tweet in data:
        hashtags = re.findall(r'\B#\w*[a-zA-Z]+\w*', tweet["content"])
        for i in hashtags:
            ht[i] += 1

    top_hashtags = heapq.nlargest(10, ht.items(), key=lambda i:i[1])
    print(top_hashtags)