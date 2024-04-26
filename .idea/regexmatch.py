import re
text = " we are the best indians"
pattern = r"the"

match = re.match(pattern,text)
if match:
    print("the match found:", match.group())
else:
    print("the match not found")