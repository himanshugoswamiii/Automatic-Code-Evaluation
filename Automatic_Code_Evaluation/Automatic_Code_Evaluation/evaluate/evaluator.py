from django.shortcuts import render
import requests as req

def code_submit(request):
    return render(request, "submit_code.html")

def executor(request):
    # code = request.GET['code']
    # data = {'request': request, 'error': True, 'output': "This is the output"}
    input = {'clientId': '26558e6412ef9b47e68c356c08e24eb7',
             'clientSecret': '43c73c299f602fbb7dacb3023bd0e64a6068a0f18ffbd81f327b840e959a187',
             'language': 'java',
             'versionIndex': '0',
             'stdin': '',
             'script': ''
             }
    op = req.post("https://api.jdoodle.com/v1/execute",json=input)
    print(op.json())
    #return render(request, "submit_code.html", data)

executor("")

def contact(request):
    return render(request,'contact.html')



