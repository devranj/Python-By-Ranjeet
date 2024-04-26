
import re
text = "ranjeet is new with the cisco"
pattern = r"cisco"

search = re.search(pattern,text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")