from zipfile import ZipFile
import os


def createZip(location):
    filenames = os.listdir(location)
    zipObj = ZipFile(location + 'result.zip', 'w')
    for file_name in filenames:
        zipObj.write(location + " / " + file_name)
    zipObj.close()
