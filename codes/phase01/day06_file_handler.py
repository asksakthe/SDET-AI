import os


def read_file(file_path):
    try:
        with open(file_path, 'r') as foo:
            content = foo.read()
            return content
    except FileNotFoundError as e:
        return F"getting {e} for file {file_path} "
# Function 2 — read file, return as list of lines (no empty lines)
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

if __name__ == '__main__':
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "newFile.txt")
    code_funct = safe_read_file(filepath=file_path)
    print(f"output of safe_read_file and length of safe_read_file function: {len(code_funct)}")
    print(f"First letter of safe_read_file function: {code_funct[0]}")
    print("*****************************")
    code01 = read_file(file_path)
    print(f"First letter of read_file function: {code01[0]}")
    print("*****************************")
    code02 = read_lines(file_path)
    print(f"output of read_lines function: {code02}")
    print("*****************************")
    code03 = read_as_documents(filepath=file_path)
    print(f"First letter of read_as_documents function: {code03[0]}")
    print("*****************************")



