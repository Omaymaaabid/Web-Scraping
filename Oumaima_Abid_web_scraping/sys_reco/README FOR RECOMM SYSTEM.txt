**the raw folder contains the dataset scrapped
**all_games/all_tags/clean_level1/clean_level2/profiles all these files will be created after running all the code

1/run the cfg.py (you must change the path of the dataset named all_games.json )
2/run the pre_processing.py to keep the information consistent (the file clean_level1 will be dumped) then assign them to classes(clean_level2 will be dumped)
3/run modelspy , user_data_engine  then entry_point.py to create the profiles.json file (
it is a fictitious database containing the history of each user)
4/run recommendation.py to calculate the score of each video based on the video_liked or commented of disliked etc
5/Finally , run the ScoreBasedRecommendation.py to calculate the final score and for each user we will be recommending 5 videos 

