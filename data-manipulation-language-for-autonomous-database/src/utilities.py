import os, json
from datetime import datetime, timedelta, time as datetime_time
from src.parameters import *

class utilities_config:

    # Add entry to json object in LOCAL
    def add_entry_to_json_object_in_local(object_name, data_list):
        try:            
            if os.path.isfile(object_name):                
                print ('  Local file exists...')
                with open(object_name, 'r+') as file:
                    obj_list = json.load(file)
                    
                    for d in data_list:
                        obj_list.append(d)

                    file.seek(0)
                    json.dump(obj_list, file)
            else:                
                print ('  Local file not exist...')
                with open(object_name, 'w') as file:
                    json.dump(data_list, file)

            print('  Add entry to json object (' + object_name + ')...[Succeded]\n')

        except Exception as e:
            print(e)

    def time_diff(start, end):        
        if isinstance(start, datetime_time): # convert to datetime
            assert isinstance(end, datetime_time)
            start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
        if start <= end: # e.g., 10:33:26-11:15:49
            return end - start
        else: # end < start e.g., 23:55:00-00:25:00
            end += timedelta(1) # +day
            assert end > start
            return end - start