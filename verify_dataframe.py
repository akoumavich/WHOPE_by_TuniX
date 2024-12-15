
from tweet_collection import tweet_collection
if __name__=='__main__':
    df=tweet_collection.get_dataframe_to_predict()
    if ('text' in df.columns ):
        print("Your DataSet is ready to be predicted")
    else :
        print("Unfortunatly, your dataset is not valid for prediction")

