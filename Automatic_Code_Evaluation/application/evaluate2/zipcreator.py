from zipfile import ZipFile

def createZip(location):
    import os
    lo = os.getcwd()
    os.chdir(location)
    filenames = os.listdir(location)
    zipObj = ZipFile('result.zip', 'w')
    for file_name in filenames:
        zipObj.write(file_name)
    zipObj.close()
    os.chdir(lo)
