import sys
import os
import re
DEBUG = False
log = open("OUTPUT.log","w")

# ==============================================================================
# Function:  print_or_log
# Parameter: A single string
# Output:    Either prints to CL or prints to log depending on debugging mode.
# ==============================================================================
def print_or_log(string):
    print(string) if DEBUG else log.write(string)



# ==============================================================================
# Function:  timeConversion
# Parameter: a string representing a 12-hour formatted time. i.e: 07:03:36PM
# Output:    A string representing a 24-hour formatted time. i.e: 19:03:36
# ==============================================================================
def timeConversion(timeString):
    # Getting the AM/PM
    dayDesignation = timeString[len(timeString)-2:]
    # Getting time without A/PM
    rawTimeString = timeString[:-2]
    # Removing the : character from the the time string.
    rawTimeString = re.sub(":","",rawTimeString)
    # Getting the hour value
    hour = rawTimeString[:2]
    # Getting the minute value
    minute = rawTimeString[2:4]
    # Getting the second value
    second = rawTimeString[4:6]
    # Setting the 00:##:##AM hour range
    if hour == "12" and dayDesignation == "AM":
        hour = "00"
    # Setting the rest of the PM hours
    if dayDesignation == "PM" and hour != "12":
        # Converting the hour to an integer then adding 12 to it
        hour = int(hour) + 12
    # Sending back the formatted 24-hour time.
    return f"{hour}:{minute}:{second}"

if __name__ == '__main__':

    if (len(sys.argv) > 1 ):
        with open('OUTPUT.log','r') as file:
            time = file.readline()
    else:
        time = ["07:43:56PM"]
    print(timeConversion("".join(time)))

    if (os.path.isfile("OUTPUT.log")):
        log.close()
    if (os.path.getsize("OUTPUT.log") == 0):
        os.remove("OUTPUT.log")