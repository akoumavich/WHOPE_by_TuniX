
import sys
import os
import suicide_visualization.suicide_visualization as sv
import matplotlib.pyplot as plt
import tweet_collection.tweet_collection as tc
sys.path.append(os.getcwd())


if __name__ == "__main__":
    df_predicted= tc.get_predicted_dataframe()

    df_predicted_suicidal = tc.get_suicidal_dataframe(df_predicted)
    df_predicted_non_suicidal = tc.get_non_suicidal_dataframe(df_predicted)

    # #saving heatmap
    sv.heatmap_day_hour(df_predicted_suicidal)
    sv.save_plot("heatmap_day_hour_suicidal")
    
    sv.heatmap_day_hour(df_predicted_non_suicidal)
    sv.save_plot("heatmap_day_hour_non_suicidal")

    #show length evolution
    sv.show_length_evolution(df_predicted)
    sv.save_plot("length_evolution")

    df_trained= tc.get_training_dataframe()


    #generate wordclouds for Suicidal predicted tweets
    sv.show_wordcloud(df_trained.iloc[0:100],cat=sv.SUICIDAL,mask_path="wordcloud_masks/sad.png")
    sv.save_plot("wordcloud_suicidal_SAD")
    
    df_trained_non_suicidal=(tc.get_non_suicidal_dataframe(df_trained))

    #generate wordclouds for non suicidal predicted tweets
    sv.show_wordcloud(df_trained_non_suicidal.iloc[0:100],mask_path="wordcloud_masks/hope.png")
    sv.save_plot("wordcloud_non_suicidal_hope")
    
    #plots the repartition of suicidal tweets per day
    sv.show_tweet_per_day(df_predicted_suicidal)
    sv.save_plot("tweets_per_day_suicidal")

    #plots the repartition of suicidal tweets per day
    sv.show_tweet_per_day(df_predicted_non_suicidal)
    sv.save_plot("tweets_per_day_non_suicidal")
    
    #plots the repartition of suicidal tweets per month
    sv.show_tweet_per_month(df_predicted_suicidal)
    sv.save_plot("tweets_per_month_suicidal")

    #plots the repartition of non suicidal tweets per month
    sv.show_tweet_per_month(df_predicted_non_suicidal)
    sv.save_plot("tweets_per_month_non_suicidal")
    
    #plots the repartition of suicidal tweets per year
    sv.show_tweet_per_year(df_predicted_suicidal)
    sv.save_plot("tweets_per_year_suicidal")

    #plots the repartition of non suicidal tweets per year
    sv.show_tweet_per_year(df_predicted_non_suicidal)
    sv.save_plot("tweets_per_year_non_suicidal")
    
    #plots the repartition of suicidal tweets per hour
    sv.show_tweet_per_hour(df_predicted_suicidal)
    sv.save_plot("tweets_per_hour_suicidal")

    #plots the repartition of non suicidal tweets per hour
    sv.show_tweet_per_hour(df_predicted_non_suicidal)
    sv.save_plot("tweets_per_hour_non_suicidal")

    #plots the comparisons of the length of suicidal tweets with non suicidal tweets
    sv.show_boxplot_length(df_predicted)
    sv.save_plot("boxplot_length_predicted")
    
    
    #plots the comparisons of the length of suicidal tweets with non suicidal tweets
    sv.show_boxplot_length(df_trained)
    sv.save_plot("boxplot_length_trained")
    
    #plots the pie
    sv.show_perc_suicidal_non_suicidal(df_predicted)
    sv.save_plot("pie_predicted")

    #plots the pie
    sv.show_perc_suicidal_non_suicidal(df_trained)
    sv.save_plot("pie_trained")
    
   