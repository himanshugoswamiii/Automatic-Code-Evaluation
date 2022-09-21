from pathlib import Path
import os
from django.http import FileResponse
import application.evaluate.main as main
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Modify no of parents according to this file's location
basedir = os.path.join(BASE_DIR, 'media/')


def fetch_files(request):
    ip = request.META.get('REMOTE_ADDR').replace('.','_')
    os.makedirs(basedir + str(ip)+"/results")
    files = [request.FILES['teachercode'], request.FILES['testcase'], *request.FILES.getlist('student')]
    for file in files:
        file_name = basedir + str(ip) + "/" + str(file.name)
        with open(file_name, 'wb+') as dest:
            for ch in file.chunks():
                dest.write(ch)
    record = [basedir + str(ip) + "/" + str(files[0].name), basedir + str(ip) + "/" + str(files[1].name),
              basedir + str(ip)]
    return record


def download(result_file):
    data = open(result_file, 'rb')
    response = FileResponse(data)
    response['Content-Type'] = 'application/x-binary'
    response['Content-Disposition'] = 'attachment; filename="student_record.xls"'
    return response


def cleanup(request):
    ip = request.META.get('REMOTE_ADDR').replace('.','_')
    shutil.rmtree(basedir + str(ip))


# To upload the file
def executor(request):
    ip = request.META.get('REMOTE_ADDR').replace('.','_')
    files = fetch_files(request)
    automated = request.POST["optradio"]
    if automated == 'Yes':
        automated = True
    else:
        automated = False
    stdin = request.POST["stdin"]
    result_file = main.interface(files[0], files[1], automated, files[2], stdin, basedir + str(ip) + "/results")
    response = download(result_file)
    cleanup(request)
    return response
