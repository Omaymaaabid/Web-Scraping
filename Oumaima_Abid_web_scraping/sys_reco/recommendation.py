import json


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

    print(videos_liked/len(profile),videos_commented/len(profile),videos_disliked/len(profile),long_videos/len(profile))
