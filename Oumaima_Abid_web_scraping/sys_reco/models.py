# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = video_data_from_dict(json.loads(json_string))

from enum import Enum
from datetime import datetime
import dateutil.parser


def from_none(x):
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c, x):
    assert isinstance(x, c)
    return x.value


def from_datetime(x):
    return dateutil.parser.parse(x)


def from_str(x):
    assert isinstance(x, str)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_stringified_bool(x):
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_bool(x):
    assert isinstance(x, bool)
    return x


def is_type(t, x):
    assert isinstance(x, t)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class ChannelID(Enum):
    UC9_YYD_G57_EP_LQX_A9_C_TZ_ZX_SE_Q = "UC9YydG57epLqxA9cTzZXSeQ"


class ChannelTitle(Enum):
    CALL_OF_DUTY = "Call of Duty"


class YtRating(Enum):
    YT_AGE_RESTRICTED = "ytAgeRestricted"


class ContentRating:
    def __init__(self, yt_rating):
        self.yt_rating = yt_rating

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        yt_rating = from_union([YtRating, from_none], obj.get("ytRating"))
        return ContentRating(yt_rating)

    def to_dict(self):
        result = {}
        result["ytRating"] = from_union([lambda x: to_enum(YtRating, x), from_none], self.yt_rating)
        return result


class DefaultAudioLanguage(Enum):
    EN = "en"
    EN_US = "en-US"


class Definition(Enum):
    HD = "hd"
    SD = "sd"


class Dimension(Enum):
    THE_2_D = "2d"


class LiveBroadcastContent(Enum):
    NONE = "none"


class ProjectionEnum(Enum):
    RECTANGULAR = "rectangular"


class VideoDatum:
    def __init__(self, published_at, title, channel_id, description, channel_title, tags, category_id, live_broadcast_content, default_audio_language, view_count, like_count, dislike_count, favorite_count, comment_count, duration, dimension, definition, caption, licensed_content, content_rating, projection):
        self.published_at = published_at
        self.title = title
        self.channel_id = channel_id
        self.description = description
        self.channel_title = channel_title
        self.tags = tags
        self.category_id = category_id
        self.live_broadcast_content = live_broadcast_content
        self.default_audio_language = default_audio_language
        self.view_count = view_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.favorite_count = favorite_count
        self.comment_count = comment_count
        self.duration = duration
        self.dimension = dimension
        self.definition = definition
        self.caption = caption
        self.licensed_content = licensed_content
        self.content_rating = content_rating
        self.projection = projection

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        try:
            published_at = from_union([from_datetime, from_none], obj.get("publishedAt"))
        except:
            published_at = None
        try:
            title = from_union([from_str, from_none], obj.get("title"))
        except:
            title = None
        try:
            channel_id = from_union([ChannelID, from_none], obj.get("channelId"))
        except:
            channel_id = None
        try:
            description = from_union([from_str, from_none], obj.get("description"))
        except:
            description = None
        try:
            channel_title = from_union([ChannelTitle, from_none], obj.get("channelTitle"))
        except:
            channel_title = None
        try:
            tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        except:
            tags = None
        try:
            category_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("categoryId"))
        except:
            category_id = None
        try:
            live_broadcast_content = from_union([LiveBroadcastContent, from_none], obj.get("liveBroadcastContent"))
        except:
            live_broadcast_content = None
        try:
            default_audio_language = from_union([DefaultAudioLanguage, from_none], obj.get("defaultAudioLanguage"))
        except:
            default_audio_language = None
        try:
            view_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("viewCount"))
        except:
            view_count = None
        try:
            like_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("likeCount"))
        except:
            like_count = None
        try:
            dislike_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("dislikeCount"))
        except:
            dislike_count = None
        try:
            favorite_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("favoriteCount"))
        except:
            favorite_count = None
        try:
            comment_count = from_union([from_none, lambda x: int(from_str(x))], obj.get("commentCount"))
        except:
            comment_count = None
        try:
            duration = from_union([from_str, from_none], obj.get("duration"))
        except:
            duration = None
        try:
            dimension = from_union([Dimension, from_none], obj.get("dimension"))
        except:
            dimension = None
        try:
            definition = from_union([Definition, from_none], obj.get("definition"))
        except:
            definition = None
        try:
            caption = from_union([from_none, lambda x: from_stringified_bool(from_str(x))], obj.get("caption"))
        except:
            caption = None
        try:
            licensed_content = from_union([from_bool, from_none], obj.get("licensedContent"))
        except:
            licensed_content = None
        try:
            content_rating = from_union([ContentRating.from_dict, from_none], obj.get("contentRating"))
        except:
            content_rating = None
        try:
            projection = from_union([from_none, lambda x: from_union([ProjectionEnum, lambda x: int(x)], from_str(x))],
                                    obj.get("projection"))
        except:
            projection = None
        return VideoDatum(published_at, title, channel_id, description, channel_title, tags, category_id, live_broadcast_content, default_audio_language, view_count, like_count, dislike_count, favorite_count, comment_count, duration, dimension, definition, caption, licensed_content, content_rating, projection)

    def to_dict(self):
        result = {}
        result["publishedAt"] = from_union([lambda x: x.isoformat(), from_none], self.published_at)
        result["title"] = from_union([from_str, from_none], self.title)
        result["channelId"] = from_union([lambda x: to_enum(ChannelID, x), from_none], self.channel_id)
        result["description"] = from_union([from_str, from_none], self.description)
        result["channelTitle"] = from_union([lambda x: to_enum(ChannelTitle, x), from_none], self.channel_title)
        result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        result["categoryId"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.category_id)
        result["liveBroadcastContent"] = from_union([lambda x: to_enum(LiveBroadcastContent, x), from_none], self.live_broadcast_content)
        result["defaultAudioLanguage"] = from_union([lambda x: to_enum(DefaultAudioLanguage, x), from_none], self.default_audio_language)
        result["viewCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.view_count)
        result["likeCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.like_count)
        result["dislikeCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.dislike_count)
        result["favoriteCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.favorite_count)
        result["commentCount"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.comment_count)
        result["duration"] = from_union([from_str, from_none], self.duration)
        result["dimension"] = from_union([lambda x: to_enum(Dimension, x), from_none], self.dimension)
        result["definition"] = from_union([lambda x: to_enum(Definition, x), from_none], self.definition)
        result["caption"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(bool, x))(x)).lower())(x))], self.caption)
        result["licensedContent"] = from_union([from_bool, from_none], self.licensed_content)
        result["contentRating"] = from_union([lambda x: to_class(ContentRating, x), from_none], self.content_rating)
        result["projection"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: to_enum(ProjectionEnum, (lambda x: is_type(ProjectionEnum, x))(x)))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.projection)
        return result


def video_data_from_dict(s):
    return from_list(VideoDatum.from_dict, s)


def video_data_to_dict(x):
    return from_list(lambda x: to_class(VideoDatum, x), x)
