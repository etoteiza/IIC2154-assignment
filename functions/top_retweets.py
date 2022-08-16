import heapq

def top_retweets(data):
    
    top = heapq.nlargest(10, data, key=lambda i:i["retweetCount"])
    print(top)