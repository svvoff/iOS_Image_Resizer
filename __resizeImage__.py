import os


file = input("file path: ")
fileDir = os.path.dirname(os.path.abspath(file))
fileName, ext = os.path.splitext(os.path.basename(file))
maxResolution = int(input("max image height: "))

fileCopyName = fileName + "_copy"

fileCopyPath = fileDir + "/" + fileCopyName + ext

os.system("cp " + file + " " + fileCopyPath)

i = 1

while i < 4:

    res = maxResolution

    if i == 1:
        res = maxResolution / 3
    if i == 2:
        res = maxResolution * 2 / 3

    newFileName = fileName + "_" + str(int(res)) + "@" + str(i) + ext
    newFilePath = fileDir + "/" + newFileName
    print(newFilePath)
    os.system("cp " + fileCopyPath + " " + newFilePath)



    os.system("sips " + newFilePath + " --resampleHeight " + str(res))

    i += 1



