import json
from random import random

with open("clean_level2.json","r") as f:
    all = json.load(f)

with open("profiles.json","r") as f:
    profiles = json.load(f)

for profile in profiles:
    videos_liked = 0
    videos_disliked = 0
    videos_commented = 0
    long_videos = 0

    for i in profile:
        if i["liked"]:
            videos_liked+= 1
        if i["disliked"]:
            videos_disliked+= 1
        if i["commented"]:
            videos_commented+= 1
        if i["is_long_video"]:
            long_videos+= 1

    scores = []
    views_score = 0
    like_score = videos_liked/len(profile)
    dislike_score = videos_disliked/len(profile)
    favorite_score = 0
    comment_score = videos_commented/len(profile)
    published_score = 0
    duration_score = long_videos/len(profile)


    for i in all:
        feeling_lucky = random()
        score = (1 + i["view_count_class"])*views_score + (1+ i["like_count_class"]) * like_score + \
                (1+  i["dislike_count_class"]) * dislike_score + \
                (1 + i["favorite_count_class"]) * favorite_score + \
                (1 + i["comment_count_class"]) * comment_score + \
                (1 + i["published_at_class"]) * published_score + \
                (1 + i["duration_class"]) * duration_score + feeling_lucky
        scores.append([i["title"],score])

    scores = sorted(scores, key=lambda l: l[1], reverse=False)
    print('## For ' + profile[0]["name"] + " we recommend")
    for i in scores[:5]:
        print(i)