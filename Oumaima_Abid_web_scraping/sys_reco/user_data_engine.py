import json
from random import choice, randint


def getTags():
    with open("all_tags.json","r") as f:
        return json.load(f)

def random_name():
    ls1 = ["oumaima", "zeineb", "hamza", "yossra", "chayma", "imen","akram","oussama","tamim","youssef","khalid","zacharia"]
    ls2 = ["abid", "ghorbel", "abdelhedi", "jelayel","garbouj"]

    return choice(ls1) + ' ' + choice(ls2)

def random_boolean(perc):
    rnd = randint(0,100)
    if rnd > perc:
        return False
    else:return True

def delegate():
    return choice([ActiveUser(),UserThatComments(),ActiveUser(),UserThatComments(),ActiveUser(),UserThatComments(),PassiveUser(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient(),UserThatIsPatient()])

class UserProfile:
    def __init__(self):
        self.name = random_name()
        self.like_videos = randint(0,100)
        self.dislike_videos = randint(0,100)
        self.comment_videos = randint(0,100)
        self.watch_long_videos = randint(0,100)

    def build_profile(self):
        all = []
        for i in range(randint(50,100)):
            dc = {
                "name" : self.name,
                "tags" : list(set([choice(getTags()),choice(getTags()),choice(getTags()),choice(getTags())])),
                "liked" : random_boolean(self.like_videos),
                "disliked" : random_boolean(self.dislike_videos),
                "commented" : random_boolean(self.comment_videos),
                "is_long_video" : random_boolean(self.watch_long_videos)
            }

            all.append(dc)

        return all


class ActiveUser(UserProfile):
    # user that likes and dislikes but does not comment
    def __init__(self):
        UserProfile.__init__(self)
        self.like_videos = 50
        self.dislike_videos = 50
        self.comment_videos = 0
        self.watch_long_videos = 0


class UserThatComments(ActiveUser):
    # user that likes and comment
    def __init__(self):
        ActiveUser.__init__(self)
        self.name = random_name()
        self.like_videos = 60
        self.dislike_videos = 40
        self.comment_videos = 40
        self.watch_long_videos = 0


class PassiveUser(UserProfile):
    # user that does not comment or like
    def __init__(self):
        UserProfile.__init__(self)
        self.name = random_name()
        self.videos_liked = 5
        self.videos_disliked = 5
        self.videos_commented = 5
        self.long_videos_watched = 0


class UserThatIsPatient(PassiveUser):
    # watch long videos
    def __init__(self):
        PassiveUser.__init__(self)
        self.name = random_name()
        self.like_videos = 9
        self.dislike_videos = 7
        self.comment_videos = 5
        self.watch_long_videos = 60
