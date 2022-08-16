from functions.load_data import load_data
from functions.top_retweets import top_retweets
from functions.top_users_tweets import top_users_tweets
from functions.top_days import top_days

if __name__ == "__main__":
    
    data = load_data()

    top_retweets(data)

    top_users_tweets(data)

    top_days(data)