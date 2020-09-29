import json

from pre_processing import start_pre_processing
from user_data_engine import UserProfile, delegate


def build_model():
    clean_data = start_pre_processing()
    profiles = []
    for i in range(50):
        profiles.append(delegate().build_profile())

    with open(r'' + 'profiles.json', "w") as f:
        json.dump(profiles, f)


if __name__ == "__main__":
    build_model()
