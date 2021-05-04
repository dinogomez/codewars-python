def format_duration(seconds):
    
    sec_in_yrs = 60 * 60 * 24 * 365
    sec_in_day = 60 * 60 * 24
    sec_in_hrs = 60 * 60
    sec_in_min = 60
    
    #calc
    yrs = seconds // sec_in_yrs
    day = seconds % sec_in_yrs // sec_in_day
    hrs = seconds % sec_in_day // sec_in_hrs
    min = seconds % sec_in_hrs // sec_in_min
    sec = seconds % sec_in_min
                
    #year handler
    if(yrs > 1):
        str_yrs = str(yrs) + " years"
    else:
        str_yrs = str(yrs) + " year"
    #day handler
    if(day > 1):
        str_day = str(day) + " days"
    else:
        str_day = str(day) + " day"
    #hour handler 
    if(hrs > 1):
        str_hrs = str(hrs) + " hours"
    else:
        str_hrs = str(hrs) + " hour"
    #minute handler
    if(min > 1):
        str_min = str(min) + " minutes"
    else:
        str_min = str(min) + " minute"
    #seconds handler
    if(sec > 1):
        str_sec = str(sec) + " seconds"
    else:
        str_sec = str(sec) + " second"
    
    #Years
    if(seconds >= sec_in_yrs):
        if(seconds == sec_in_yrs):
            seconds ="1 year"
        else: 
            if(day == 0):
                seconds = (str_yrs + ", " + str_hrs + ", " + str_min + " and " + str_sec)
                return seconds
            if(hrs == 0):
                seconds = (str_yrs + ", " + str_day + ", " + str_min + " and " + str_sec)
                return seconds
            if(min == 0):
                seconds = (str_yrs + ", " + str_day + ", " + str_hrs + " and " + str_sec) 
                return seconds
            if(sec == 0):
                seconds = (str_yrs + ", " + str_day + ", " + str_hrs + " and " + str_min)
                return seconds
            else:
                seconds = (str_yrs + ", " + str_day + ", " + str_hrs + ", " + str_min + " and " + str_sec)   
            
        return seconds
    #Days
    elif(seconds < sec_in_yrs and seconds >= sec_in_day):
        if(seconds == sec_in_day):
            seconds = "1 day"
        else:
            if(hrs == 0):
                seconds = (str_day + ", " + str_min + " and " + str_sec)
                return seconds
            if(min == 0):
                seconds = (str_day + ", " + str_hrs + " and " + str_sec)
                return seconds
            if(sec == 0):
                seconds = (str_day + ", " + str_hrs + " and " + str_min)
                return seconds
            else:
                seconds = (str_day + ", " + str_hrs + ", " + str_min + " and " + str_sec)   

        return seconds
    #Hour
    elif(seconds < sec_in_day and seconds >= sec_in_hrs):

        if(seconds == sec_in_hrs):
            seconds = "1 hour"
        else:

            if(min == 0):
                seconds = (str_hrs + " and " + str_sec)
                return seconds
            if(sec == 0):
                seconds = (str_hrs + " and " + str_min)
                return seconds
            else:
                seconds = (str_hrs + ", " + str_min + " and " + str_sec)   

        return seconds
    #Minute
    elif(seconds < sec_in_hrs and seconds >= sec_in_min):
        if(seconds == sec_in_min):
            seconds = "1 minute"
        else:
            if(sec == 0):
                seconds = (str_min)
                return seconds
            else:
                seconds = (str_min + " and " + str_sec)   

            return seconds
    #Seconds
    elif(seconds < sec_in_min):
        if(seconds == 1):
            seconds = "1 second"

        else:
            if(sec == 0):
                seconds = "now"
                return seconds
            else:
                seconds = (str_sec)   

        return seconds
    
             
            
    