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
    return response['statusCode'] != 200 or (response['cpuTime'] is None and response['memory'] is None)


def get_ex(filename):
    temp = filename.split(".")
    if len(temp) != 2:
        return None
    else:
        return temp[1].strip()


def io_file(basedir, ext):
    try:
        text = None
        with open(basedir + "io_file." + ext) as f:
            text = f.read()
        return text
    except Exception as e:
        raise Exception("Unable to read IO files ...")


def output(filename, basedir, std_in=''):
    data = read_file(filename)
    extension = get_ex(filename)
    if extension not in supported_ext():
        raise Exception(extension, " is not supported ")
    else:
        io_data = io_file(basedir, extension)
        language_details = ext_to_lang()[extension]
        metadata = get_metadata(language=language_details[0], version_index=language_details[1], std_in=std_in,
                                script=data + "\n" + io_data)
        response = execute(metadata)
        if any_error(response):
            if 'error' in response:
                raise Exception(response['error'])
            else:
                raise Exception(response['output'])
        else:
            return response['output'], ext_to_lang()[extension][0]


def parse(status):
    lines = status.split("\n")
    splitor = lines[0].strip()
    log_data = ''
    count = 0
    score = None
    time = None
    for i in range(1, lines):
        line = lines[i].strip()
        if len(line) == len(splitor) and line == splitor:
            count += 1
        if count == 0:
            log_data += line
        elif count == 1:
            score = line
        elif count == 2:
            time = line
    return log_data, score, time


def evaluate_students(path, testcase):
    result = []
    files = os.listdir(path)
    for file in files:
        if verify_file(file):
            name, roll_no = get_name_roll(file.split(".")[0])
            score = None
            time = None
            language = None
            try:
                status = output(path + "/" + file, testcase)
                details = parse(status[0])
                log_data = details[0]
                score = details[1]
                time = details[2]
                language = status[1]
            except Exception as e:
                log_data = e.__str__()
                score = 0
                language = None
                time = None

            with open(path + "/results/" + name + "_" + roll_no + ".txt", 'w') as f:
                f.write(log_data)
            result.append((roll_no, name, score, time, language))
    return result


def interface(testcase_file, basedir):
    testcases = read_file(testcase_file)
    results = evaluate_students(basedir, testcases)
    result_file = basedir + "/results/student_record.xls"
    writer.write(result_file, results)
