__author__ = 'Administrator'
import re
def match(line):
    #matchObj1=re.match(r'^www.(.*).(com|edu|net)$', line, re.M|re.I)
    matchObj1=re.match(r'^www.\S+.(com|edu|net)$', line, re.M|re.I)
    if matchObj1:
        print "matchObj.group() : ", matchObj1.group()
    else:
        print "match error"
match("www. baidu.com")
match("www.baidu.edu")
match("www.baidu.cm")
match("ww.baidu.com")