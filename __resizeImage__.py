import os


file = input("file path: ")
fileDir = os.path.dirname(os.path.abspath(file))
fileName, ext = os.path.splitext(os.path.basename(file))
maxResolution = int(input("max image height: "))

i = 1

while i < 4:
    newFileName = fileName + str(i) + ext
    newFilePath = fileDir + "/" + newFileName
    print(newFilePath)
    os.system("cp " + file + " " + newFilePath)

    res = maxResolution

    if i == 1:
        res = maxResolution / 3
    if i == 2:
        res = maxResolution * 2 / 3

    os.system("sips " + newFilePath + " --resampleHeight " + str(res))

    i += 1



