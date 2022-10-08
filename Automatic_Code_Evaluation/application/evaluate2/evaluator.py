from pathlib import Path
import os
from django.http import FileResponse
import application.evaluate2.main as main
import application.evaluate2.zipcreator as zip
import shutil
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Modify no of parents according to this file's location
basedir = os.path.join(BASE_DIR, 'media/')


def fetch_files(request):
    ip = request.META.get('REMOTE_ADDR').replace('.', '_')
    os.makedirs(basedir + str(ip) + "/results")
    os.makedirs(basedir + str(ip) + "/io")
    files = [request.FILES['testcase'], *request.FILES.getlist('student')]
    parent = basedir + str(ip) + "/"
    for file in [*request.FILES.getlist('io')]:
        file_name = parent + "io/" + str(file.name)
        with open(file_name, 'wb+') as dest:
            for ch in file.chunks():
                dest.write(ch)
    for file in files:
        file_name = parent + str(file.name)
        with open(file_name, 'wb+') as dest:
            for ch in file.chunks():
                dest.write(ch)
    record = [parent + "/" + str(files[0].name), basedir + str(ip)]
    return record


def download(result_file):
    data = open(result_file, 'rb')
    response = FileResponse(data)
    response['Content-Type'] = 'application/x-binary'
    response['Content-Disposition'] = 'attachment; filename="result.zip"'
    return response


def cleanup(request):
    ip = request.META.get('REMOTE_ADDR').replace('.', '_')
    shutil.rmtree(basedir + str(ip))


# To upload the file
def executor(request):
    try:
        files = fetch_files(request)
        main.interface(files[0], files[1])
        zip.createZip(files[1]+"/results")
        response = download(files[1]+"/results/result.zip")
        cleanup(request)
    except Exception as e:
        cleanup(request)
        return render(request, "error.html", {'message': e.__str__()})
    return response
