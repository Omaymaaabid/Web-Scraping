# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:40:07 2020

@author: ASUS
"""


from youtube_statistics import YTstats
API_KEY="AIzaSyAjq9cdtHgwV5LobYK8ADZbJwAplNCsuUI"

#freefire_id = 'UC_vVy4OI86F0amXqFN_zTMg'
#freefire_id = 'H2ODelirious'
freefire_id = 'UCiMRGE8Sc6oxIGuu_JxFoHg'
channel_id = freefire_id

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()