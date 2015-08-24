__author__ = 'Administrator'
import  sys
textdir=sys.argv[1]
result=sys.argv[2]
sum=0
locate=""
f = open(textdir, 'r')
string = f.readlines()
x=len(string)
f.seek(0)          #relocate
for i in range(x):
    line=f.readline()
    print "line" + str(i+1)+ ':'+ line
    if(line.find(result)>0):
        sum=sum+1
        locate=locate+"line: "+str(i+1)+":"+str(line.find("line"))+'\n'
print "sum of the "+result+" is: "+str(sum)
print "the locate is :\n" +locate
f.close()

