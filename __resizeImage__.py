import os
import glob

variable = raw_input('type file name: ')
maxres = int(input('input max h resolution: '))
print(variable)
print(os.path.dirname(os.path.realpath(__file__)))

startFile = ""

for file in glob.glob(variable + ".png"):
    print(file)
    startFile = file

i = 1
while i < 4:
    newFileName = variable + str(i) + ".png"
    b = "cp " + startFile + " " + newFileName
    os.system(b)
    res = maxres
    if i == 1:
        res = maxres / 3
    if i == 2:
        res = maxres / 2
    sip = "sips " + newFileName + " --resampleHeight " + str(res)

    os.system(sip)

    i = i + 1

#scriptName = os.path.basename(__file__)
#os.system("rm " + scriptName + ".py")