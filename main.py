import polyline
import json
import pandas as pd


#Get raw file from Strava
file=open('response.json', encoding="utf8")
data=json.load(file)
df=pd.json_normalize(data)


#Clean out data I dont need.
def cleanStrava():
    df.drop(columns=['resource_state','name','sport_type',
    'workout_type','id','start_date','start_date_local',
    'timezone','utc_offset','location_city','location_state',
    'kudos_count','comment_count','athlete_count','photo_count',
    'trainer','commute','manual','private','visibility','flagged',
    'gear_id','start_latlng','end_latlng','max_speed','kilojoules',
    'device_watts','has_heartrate','heartrate_opt_out','display_hide_heartrate_option',
    'elev_high','elev_low','upload_id','upload_id_str','external_id','from_accepted_tag',
    'pr_count','total_photo_count','has_kudoed','athlete.id','athlete.resource_state',
    'map.id','map.resource_state','average_heartrate','max_heartrate','suffer_score',
    'achievement_count','location_country','type'],inplace=True)
    df.drop([2,4],inplace=True)
    df.reset_index(inplace=True)
    df.drop(columns=['index'],inplace=True)
    #Change Decoded map info to Long & Lat points
    df['map.summary_polyline'] = df['map.summary_polyline'].apply(lambda x: polyline.decode(x))




#       _________FUNCTION CALLS_________
cleanStrava()
print(df.head(10)).transpose()