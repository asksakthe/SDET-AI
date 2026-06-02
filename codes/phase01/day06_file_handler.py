
def read_file(file_path):
    with open(file_path, 'r') as foo:
        content = foo.read()
        return content

def read_lines(file_path):
    with open(file_path, 'r') as foo:
        lines = file_path.readlines()

    for i, content in enumerate(lines):
        print(f"Line_num {i+1}: content")

    pass

 
    

