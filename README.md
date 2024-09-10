
This in an ad-hoc Python script used to merge the time-stamped video annotations of deep-sea benthic megafauna - annotated using the open-source software BIIGLE (biigle.de) (Langenkämper et al., 2017) - with a corresponding navigation file. In this case, the navigation file contains the USBL position of a Remotely Operated Vehicule (ROV) with information on time, latitude and longitude.

# Requirements 

To run this code, you will need:

- **Video annotation reports from BIIGLE**: Exported as a '.csv' file, with an additional for the start time of each annotated video.
  *Note: Before running the script, manually insert a new column with the start time of the video and remove the brackets '[ ]' in the 'frames' column.*

- **Navigation file**: A '.csv' file containing time, latitude and longitude.
  *Note: To run this code, 'time' must be formatted as HHMMSS (e.g., "16:53:47" should be represented as "165347"). Manually edit this column before running the script.*

# Functionality 

This code is used to:
1. **Calculate annotation time**: Based on the 'start_time' and 'frames' columns. The `start_time` represents the start time of the annotated video, and the `frames` column provides the time, in seconds, of the annotation within that video.
2. **Georeference the annotations**: By merging the time-stamped annotations with the time of the navigation file. 

**Reference:**
Langenkämper, D., Zurowietz, M., Schoening, T., & Nattkemper, T. W. (2017). Biigle 2.0-browsing and annotating large marine image collections. Frontiers in Marine Science, 4, 83. doi: 10.3389/fmars.2017.00083
