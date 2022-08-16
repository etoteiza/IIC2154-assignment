from functions.load_data import load_data
from functions.top_retweets import top_retweets

if __name__ == "__main__":
    
    data = load_data()

    top_retweets(data)