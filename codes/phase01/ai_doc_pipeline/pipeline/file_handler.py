import os

def file_read(file_in):
    try:
        with open(file_in,'r') as foo:
            content = foo.read()
            return content
    except FileNotFoundError as e:
        return f"The respective {file_in} are not present in location"
    
def read_lines(filepath):
    with open(filepath, 'r') as foo:
        lines = foo.readlines()
        doc_list = []
        for i in lines:
            doc_list.append(i)
        if len(doc_list) == 0:
            return f"The file {filepath} has no contents, please check"
        else:
            return len(doc_list)
            

def read_as_documents(filepath):
    with open(filepath, 'r') as foo:
        file_content = foo
        result = []
        for i, cont in enumerate(file_content):
            dic = {"line Num": i+1, "text": cont.strip()}
            result.append(dic)
        return result

def safe_read_file(filepath):
    try:
        with open(filepath) as foo:
            fileContents = foo.read()
            if not fileContents.strip():
                return f"Error : {filepath} is empty"
            return fileContents
    except FileNotFoundError:
        return f"The {filepath} file doesn't exist, Check once"
 