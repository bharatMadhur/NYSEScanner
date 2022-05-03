from main import newsOfTheStock
import pandas as pd


email_id = []
def generateNewsletter():
    global email_id
    news=newsOfTheStock()
    news_df= pd.DataFrame(news)
    result = news_df['title'].head(10)
    print(result)
generateNewsletter()