import os
import day06_file_handler as D6

actual_input = """   AI is transforming the software \nindustry rapidly.
LangChain is a framework\n for building LLM       applications.
RAG stands for          Retrieval Augmented Generation.
Agents can use     tools to complete complex tasks."""
#aim is to remove the \n and extra spaces

def cleaning_Text(in_str):
    space_del = in_str.strip()
    line_remin = space_del.replace("\\n"," ")
    line_rem = line_remin.replace("\n"," ")
    mul_space = " ".join(line_rem.split())
    return mul_space
#print(cleaning_Text(in_str=actual_input))
#aim is to split the sentences based on '.' & return as list
def split_sent(str_in):
    split_list = [x for x in str_in.split('.') if x]
    return split_list
#chunk the text wit some overlap
def chunk_text(list_in, chunk_Siz=30, overlap = 10):
    stri = " ".join(list_in)
    #print(f"DEBUG stri[:50]: {repr(stri[:50])}")
    words = stri.split()
    #print(f"DEBUG first 5 words: {words[:5]}") 
    n = len(words)
    l1 = []
    start = 0
    while start < n:
        end = start + chunk_Siz
        chunk = " ".join(words[start:end])
        l1.append(chunk)
        start += (chunk_Siz-overlap)
    return l1
    #return n

def process_doc(filName):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_in = os.path.join(file_dir,filName)
    try:
        with open(file_in,'r') as foo:
            cont = foo.read()
            f01 = cleaning_Text(cont)
            f02 = split_sent(f01)
            f03 = chunk_text(f02)
            result = []
            for i, content in enumerate(f03):
                result.append({'chunk_ID': i+1, 'text': content, 'wordsCount': len(content.split())})
            return result 
    except FileNotFoundError as e:
        return f"check the file present bcoz getting {e}"
    #return file_dir

if "__main__" == __name__:
    fi = process_doc(filName='newFile.txt')
    



