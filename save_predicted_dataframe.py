import os , sys
sys.path.append(os.getcwd())
import tweet_collection.tweet_collection as tw
import suicide_training.prediction as pred

#saving the predicted dataset
if __name__=='__main__':
    #importing the dataset that we're gonna do the prediction on
    data=tw.get_dataframe_to_predict()
    #add the predicted target column
    data=pred.predicted_dataframe(data)
    #save the dataset in csv format
    pred.save_predicted_dataframe(data)