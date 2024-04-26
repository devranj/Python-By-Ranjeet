
#Regex usage there is a log file you need to search an error quick

import re
text = "ranjeet works for arcsight"
pattern = r"arcsight"

search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("patern not found")



