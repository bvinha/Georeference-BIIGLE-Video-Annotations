#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:47:14 2024

@author: beatriz
"""

## Calculate annotation time, based on time of the start of the video 
## and on the seconds of annotation frame 

import pandas as pd

# import raw biigle annotations
biigle_raw = pd.read_csv('./00_raw_biigle_annotations.csv')

# import navigation file
# to run the code as it is, time column should be as HHMMSS (e.g., "16:53:47" should be represented as "165347")
rov_nav = pd.read_csv('./00_raw_rov_navigation.csv', sep = ",", dtype={'time':float}) 
                      dtype={'time':float})

# Convert start_time and frame_secs to timedelta in biigle annotations file
biigle_raw['start_time'] = pd.to_timedelta(pd.to_datetime(biigle_raw['start_time']).dt.strftime('%H:%M:%S'))
biigle_raw['frames_sec'] = pd.to_timedelta(biigle_raw['frames_sec'], unit = 'seconds')

# Check - start_time and frames_sec must be timedelta
biigle_raw.dtypes

# Sum start time of the video with frames_sec to obtain new column 
# with annotation time
biigle_raw['annotation_time'] = biigle_raw['start_time']+biigle_raw['frames_sec']
print(biigle_raw) #check if new column was added to the dataframe with annotation time

# In order to run the rest of the code, the 'annotation_time' column needs to 
# be in a specific format, in this case, as integer (float64) values. 
# For example, "16:53:47" should be represented as "165347". 
# So, in the lines below, this will be done manually and a new column 
# will be created (time).

# Convert annotation_time to total seconds, then format manually to HHMMSS
biigle_raw['hours'] = biigle_raw['annotation_time'].dt.components['hours']
biigle_raw['minutes'] = biigle_raw['annotation_time'].dt.components['minutes']
biigle_raw['seconds'] = biigle_raw['annotation_time'].dt.components['seconds']

# Create 'time' column in HHMMSS format
biigle_raw['time'] = (biigle_raw['hours'] * 10000 + biigle_raw['minutes'] * 100 + biigle_raw['seconds']).astype(float)

# Delete columns
biigle_raw.drop(['hours', 'minutes', 'seconds'], axis=1, inplace=True)

## Merge timestamped annotations with ROV navigation 

# time must be float64 for both dataframes
rov_nav.dtypes
biigle_raw.dtypes 

# Georeference biigle annotations by merging df based on time
angeo_ref = pd.merge_asof(biigle_raw.sort_values('time'), rov_nav.sort_values('time'), on="time", direction="nearest")

# Delete columns
angeo_ref.drop(['time', 'start_time', 'frames_sec'], axis=1, inplace=True) 
print(angeo_ref) # check

# Save georeferenced annotations as csv file
angeo_ref.to_csv('./Biigle_annotations_georef.csv', index=False)