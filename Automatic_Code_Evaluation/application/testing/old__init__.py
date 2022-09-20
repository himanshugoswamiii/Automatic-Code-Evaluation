# import os
# import re
# import requests as req
#
#
# def isRollno(rollno):
#     obj = re.compile(r"[0-9]+")
#     return bool(obj.fullmatch(rollno))
#
#
# def isName(name):
#     obj = re.compile(r"[a-zA-Z ]+")
#     return bool(obj.fullmatch(name))
#
#
# metadata = {'clientId': '26558e6412ef9b47e68c356c08e24eb7',
#             'clientSecret': '43c73c299f602fbb7dacb3023bd0e64a6068a0f18ffbd81f327b840e959a187',
#             'language': 'java',
#             'versionIndex': '0',
#             'stdin': '',
#             'script': ''
#             }
# path = input("Enter directory path")
# teacher_code = input("Enter your code file ")
# print("Do you want automated test cases[Y/N] ")
# automated_testcase = input()
# testcase = input("Enter test case file name ")
#
# try:
#     with open(testcase, 'r') as f:
#         testcase = f.read()
# except Exception as e:
#     print(e)
#     exit(100)
#
# if automated_testcase in ['Y', 'y']:
#     metadata['script'] = testcase
#     metadata['stdin'] = ''
#     response = req.post("https://api.jdoodle.com/v1/execute", json=metadata)
#     details = response.json()
#     if details['statusCode'] == 200:
#         testcase = details['output']
#     else:
#         print("Error while executing test case file ")
#         exit(100)
#
# try:
#     with open(teacher_code, 'r') as f:
#         teacher_code = f.read()
# except Exception as e:
#     print(e)
#     exit(100)
#
# metadata['script'] = teacher_code
# metadata['stdin'] = testcase
# actualoutput = None
# response = req.post("https://api.jdoodle.com/v1/execute", json=metadata)
# details = response.json()
# if details['statusCode'] == 200:
#     actualoutput = details['output']
# else:
#     print("Error while executing teacher code file ")
#     exit(100)
#
# files = os.listdir(path)
# mapping = {'py': ('python3', 4), 'java': ('java', 4), 'cpp': ('cpp', 5)}
#
# for file in files:
#     f = file.split(".")
#     if len(f) == 2:
#         fileprefix = f[0].split("_")
#         f[1] = f[1].strip()
#         if len(fileprefix) == 2:
#             name = fileprefix[0].strip()
#             rollno = fileprefix[1].strip()
#             if isName(name) and isRollno(rollno):
#                 with open(path + "/"+file, 'r') as f1:
#                     student_code = f1.read()
#                     metadata['script'] = student_code
#                     metadata['language'] = mapping[f[1]][0]
#                     metadata['versionIndex'] = mapping[f[1]][1]
#                     response = req.post("https://api.jdoodle.com/v1/execute", json=metadata)
#                     details = response.json()
#                     print(details)
#                     if details['statusCode']==200:
#                         if actualoutput == details['output']:
#                             print(file," passed testcases ",details['cpuTime'] ," : ",details['memory'])
#                         else:
#                             print("error .....",file)
#
#             else:
#                 print("There is some problem with file name ", file)
#         else:
#             print("There is some naming problem with file ", file)
#     else:
#         print("There is some naming problem with file ", file)
