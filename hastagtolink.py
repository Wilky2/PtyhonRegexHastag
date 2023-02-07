import re


def replaceHastagPerLink(text):
    return re.sub("#\w+",lambda match : "<a href=\"\">"+ str(match.group())+"</a>",text)
    
text = "Aller sur #facebook puis sur #twitter ensuite aller sur #instagram"

replaceHastagPerLink(text)
