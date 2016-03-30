f = open("dsp/python/faculty.csv", "r")

faculty = list(csv.reader(f))
data = faculty[1:]

#Q1

PhD = 0
ScD = 0
MPH = 0
MS = 0
BSEd = 0
JD = 0
MA = 0

for row in data:
    if re.search("PhD|Ph.D.|Ph.D", row[1].strip()) != None:
        PhD += 1
    if re.search("ScD|Sc.D.", row[1].strip()) != None:
        ScD += 1
    if re.search("MA", row[1].strip()) != None:
        MA += 1
    if re.search("MPH", row[1].strip()) != None:
        MPH += 1
    if re.search("JD", row[1].strip()) != None:
        JD += 1
    if re.search("B.S.Ed.", row[1].strip()) != None:
        BSEd += 1
    if re.search("M.S.|MS", row[1].strip()) != None:
        MS += 1

print "PHD: " + str(PhD)
print "ScD: " + str(ScD)
print "MA: " + str(MA)
print "MPH: " + str(MPH)
print "JD: " + str(JD)
print "BSEd: " + str(BSEd)
print "MS: " + str(MS)

#Q2

