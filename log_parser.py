
import re

print("WARNINGS:")

with open("./data/rsvp_agent_log.dat", "r+")as f:
    for i in f:
        match = re.search('WARNING', i)
        if match is None:
            pass
        else:
            print(str(i[0:14]) +  " -- "  + str(i[45:]))