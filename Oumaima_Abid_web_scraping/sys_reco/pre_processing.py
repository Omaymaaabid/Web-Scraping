import json
import re
from datetime import datetime, timezone
from os import listdir
from os.path import isfile, join

from sklearn.cluster import KMeans
import numpy as np
from cfg import INFILE
from models import video_data_from_dict


def level1_cleaning():
    dt = read_data()
    output = []

    for single_video_data in dt:
        deleteKey(single_video_data, "thumbnails")
        deleteKey(single_video_data, "localized")
        deleteKey(single_video_data, "topicCategories")
        deleteKey(single_video_data, "relevantTopicIds")

        output.append(single_video_data)
    with open('clean_level1.json', 'w') as outfile:
        json.dump(output, outfile)


def level2_cleaning():
    with open("clean_level1.json", "r") as f:
        clean = f.read()
    array = video_data_from_dict(json.loads(clean))

    values2classes(array, "view_count", string2intModifier,5)
    values2classes(array, "like_count", string2intModifier,4)
    values2classes(array, "dislike_count", string2intModifier,4)
    values2classes(array, "favorite_count", string2intModifier,3)
    values2classes(array, "comment_count", string2intModifier,4)
    values2classes(array, "published_at", dateDeltaModifier,3)
    values2classes(array, "duration", yt_durationModifier, 2)

    objs = [
        clean_fields2dict(i) for i in array
    ]
    with open("clean_level2.json", "w") as f:
        json.dump(objs, f)

    all_tags = []
    for i in array:
        if i.tags == None:
            continue
        for j in i.tags:
            all_tags.append(j)
    with open("all_tags.json", "w") as f:
        json.dump(list(set([i.lower() for i in  all_tags])), f)


def merge_all_files():
    mypath = "raw"
    onlyjson = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".json")]
    dc = []
    for f in onlyjson:
        with open("raw/" + f,"r") as g:
            dt = json.load(g)
        dt = dt[list(dt.keys())[0]]["video_data"]
        for i in dt.keys():
            dc.append(dt[i])

    with open("all_games.json","w") as f:
        json.dump(dc,f)





def start_pre_processing():
    merge_all_files()
    level1_cleaning()
    level2_cleaning()


def projectOverField(field_name, array, modifier):
    projections = []
    for i in array:
        projections.append(i.__dict__[field_name])
    return modifier(projections)


def values2classes(array, field, modifier, nbClusters=3):
    projections = projectOverField(field, array, modifier)
    projections = [[1, i] for i in projections]
    X = np.array(projections)
    kmeans = KMeans(n_clusters=nbClusters, random_state=0).fit(X)
    clusters = [i[1] for i in kmeans.cluster_centers_]
    counter = 0
    for i in array:
        #i.__dict__["clean_" + field] = clusters[kmeans.labels_[counter]]
        i.__dict__["clean_" + field + "_class"] = int(str(kmeans.labels_[counter]))
        counter += 1


def identityModifier(array):
    return array


def yt_durationModifier(array):
    return [yt_time(i) for i in array]


def string2intModifier(array):
    return [int(i) for i in array]


def dateDeltaModifier(array):
    t2 = datetime.now(timezone.utc)
    return [((t2 - t1) / 12).seconds for t1 in array]


def read_data():
    # reads file and return a json object
    with open(INFILE, "r") as f:
        all = f.read()
    return json.loads(all)


def clean_fields2dict(obj):
    dc = {}
    dc.update({
        "title": obj.title
    })
    for i in obj.__dict__.keys():
        if i.startswith("clean"):
            dc.update({
                i.replace("clean_", ""): obj.__dict__[i]
            })
    return dc


def deleteKey(dc, key):
    try:
        del dc[key]
    except:
        pass


def yt_time(duration="P1W2DT6H21M32S"):
    """
    Converts YouTube duration (ISO 8061)
    into Seconds

    see http://en.wikipedia.org/wiki/ISO_8601#Durations
    """
    ISO_8601 = re.compile(
        'P'  # designates a period
        '(?:(?P<years>\d+)Y)?'  # years
        '(?:(?P<months>\d+)M)?'  # months
        '(?:(?P<weeks>\d+)W)?'  # weeks
        '(?:(?P<days>\d+)D)?'  # days
        '(?:T'  # time part must begin with a T
        '(?:(?P<hours>\d+)H)?'  # hours
        '(?:(?P<minutes>\d+)M)?'  # minutes
        '(?:(?P<seconds>\d+)S)?'  # seconds
        ')?')  # end of time part
    # Convert regex matches into a short list of time units
    units = list(ISO_8601.match(duration).groups()[-3:])
    # Put list in ascending order & remove 'None' types
    units = list(reversed([int(x) if x != None else 0 for x in units]))
    # Do the maths
    return sum([x * 60 ** units.index(x) for x in units])
