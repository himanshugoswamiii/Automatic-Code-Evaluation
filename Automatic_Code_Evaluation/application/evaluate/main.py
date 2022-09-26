import re
import requests as req
import os
import application.evaluate.excel_writer as writer


def get_metadata(language='java', version_index=0, std_in='', script=''):
    metadata = {'clientId': '26558e6412ef9b47e68c356c08e24eb7',
                'clientSecret': '43c73c299f602fbb7dacb3023bd0e64a6068a0f18ffbd81f327b840e959a187',
                'language': language,
                'versionIndex': version_index,
                'stdin': std_in,
                'script': script
                }
    return metadata


def read_file(filename):
    text = None
    with open(filename, 'r') as file:
        text = file.read()
    return text


def get_name_roll(filename):
    if is_valid_filename(filename):
        prefix_compo = filename.split("_")
        name = prefix_compo[0].strip()
        roll_no = prefix_compo[1].strip()
        return [name, roll_no]
    else:
        return None


def supported_ext() -> list:
    return ['py', 'java', 'cpp', 'c', 'js']


def ext_to_lang() -> dict:
    return {'py': ('python3', 4), 'java': ('java', 4), 'cpp': ('cpp', 5), 'c': ('c', 5), 'js': ('rhino', 2)}


def is_roll(roll):
    obj = re.compile(r"[0-9]+")
    return bool(obj.fullmatch(roll))


def isname(name):
    obj = re.compile(r"[a-zA-Z ]+")
    return bool(obj.fullmatch(name))


def is_valid_filename(filename: str) -> bool:
    prefix_compo = filename.split("_")
    if len(prefix_compo) != 2:
        return False
    name = prefix_compo[0].strip()
    roll_no = prefix_compo[1].strip()
    return isname(name) and is_roll(roll_no)


def verify_file(filename: str) -> bool:
    file_components = filename.split(".")
    if len(file_components) != 2:
        return False
    main_name = file_components[0].strip()
    extension = file_components[1].strip()
    if (extension not in supported_ext()) or (not is_valid_filename(main_name)):
        return False
    return True


def execute(metadata):
    response = req.post("https://api.jdoodle.com/v1/execute", json=metadata)
    return response.json()


def any_error(response):
    print(response)
    return response['statusCode'] != 200 or (response['cpuTime'] is None and response['memory'] is None)


def get_time_memory(response):
    return str(response['cpuTime']) + " s", str(response['memory']) + " kb"


def get_ex(filename):
    temp = filename.split(".")
    if len(temp) != 2:
        return None
    else:
        return temp[1].strip()


def get_testcases(filename, std_in='', automated=False):
    data = read_file(filename)
    if not automated:
        return data
    else:
        return output(filename, std_in)[0]


def output(filename, std_in=''):
    data = read_file(filename)
    extension = get_ex(filename)
    if extension not in supported_ext():
        raise Exception(extension, " is not supported ")
    else:
        language_details = ext_to_lang()[extension]
        metadata = get_metadata(language=language_details[0], version_index=language_details[1], std_in=std_in,
                                script=data)
        response = execute(metadata)
        if any_error(response):
            if 'error' in response:
                raise Exception(response['error'])
            else:
                raise Exception(response['output'])
        else:
            return [response['output'], get_time_memory(response)]


def evaluate_students(path, testcase, actual_output):
    result = []
    files = os.listdir(path)
    for file in files:
        if verify_file(file):
            name, roll_no = get_name_roll(file.split(".")[0])
            res = None
            time = None
            memory = None
            error = "NA"
            try:
                student_output = output(path + "/" + file, testcase)
                if student_output[0] == actual_output:
                    res = "Accepted"
                    time = student_output[1][0]
                    memory = student_output[1][1]

                else:
                    res = "Rejected"
                    time = "NA"
                    memory = "NA"
            except Exception as e:
                error = e.__str__()
                res = "Rejected"
                time = "NA"
                memory = "NA"
            result.append((name, roll_no, res, time, memory, error))
    return result


def interface(code_file, testcase_file, automated, students_program_path, std_in, basedir):
    testcases = get_testcases(testcase_file, std_in, automated)
    actual_output = output(code_file, testcases)
    if actual_output[0].endswith("JDoodle - output Limit reached.\n") or testcases.endswith(
            "JDoodle - output Limit reached.\n"):
        raise Exception("Limit exceeded\n")
    results = evaluate_students(students_program_path, testcases, actual_output[0])
    result_file = basedir + "/student_record.xls"
    writer.write(result_file, results)
    return result_file
