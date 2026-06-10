import day06_file_handler as d6
import os

sin = ['you', 'are', 'world']
#aim is to cleaning the input and return
input01 = "  AI is   transforming.\nthe software   industry. and globally compettion is new normal. you have to adapt. transform your skills into wings.  "
def clean_text(input_str): 
    rem = input_str.replace("\n", " ")
    cle = rem.strip()
    c = cle.split()
    final = " ".join(c)
    #print(final)
    return final

f01 = clean_text(input01)
#aim is to split sentences baased on '.'
def split_into_sentences(input_str):
# Split text at . character
    text_in = input_str.split('.')
    #return text_in
# Strip each sentence
# Remove empty sentences
# Return list of clean sentences
    cleaned_sentences_list = [i.strip() for i in text_in if i.strip()]
    return cleaned_sentences_list
f02 = split_into_sentences(f01)
#print(split_into_sentences(input_str=input01))


#chunking the text with 
def chunk_text(cleaned_sentences_list, chunk_size = 6, overlap = 3):
#     Split text into words
# Create chunks of chunk_size words
# Each chunk overlaps previous by overlap words
# Return list of chunk strings
    cleaned_sentences = "".join(cleaned_sentences_list).split(',')
    return cleaned_sentences
    # start = 0
    # chunk_List =[]
    
    # while start < len(cleaned_sentences):
    #     end = start + chunk_size
    #     chunk = ''.join(cleaned_sentences[start:end])
    #     #print(f"inside function : {chunk}")
    #     chunk_List.append(chunk)
    #     start = end - overlap
    
    # return chunk_List
f03 = chunk_text(f02)
print(f"len of {sum([len(i) for i in f03[0].split(' ')])}\n  the type of out:{type(f03)} \n   the output of :{f03}")
# def process_document(filepath, chunk_size=5, overlap=2):
#     file_in = d6.read_file(file_path=filepath)
#     fun01 = clean_text(file_in)
#     print("*** output of fun01*******")
#     print(fun01)
#     fun02 = (split_into_sentences(fun01))
#     print("***output of fun02 ***")
#     print(fun02)
#     fun03 = chunk_text(fun02)
#     print("***output of fun03 ******")
#     print(fun03)
#     chunk_dic = {}
#     for i,j in enumerate(fun03):
#          chunk_dic['chunk_id'] = i
#          chunk_dic['text'] = j
#          chunk_dic['word_Count'] = len(j.split(' '))
#          print(f"############### output of  chunk dic {chunk_dic} #################")
#     return chunk_dic

# if __name__ == "__main__":
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     filePath = os.path.join(script_dir, "newFile.txt")
#     chunks_act = process_document(filepath=filePath,chunk_size=15, overlap=3)
#     print(f"Total Chunks : {len(chunks_act)}, Type : {type(chunks_act)}")
#     for i, j in chunks_act.items():
#         print(j)
#     # for c in chunks_act:
#     #     print(f"\nChunk {chunks_act['chunk_id']}:")
#     #     print(f"  Words : {chunks_act['word_Count']}")
#     #     print(f"  Text  : {chunks_act['text']}")


actual_input = """   AI is transforming the software \nindustry rapidly.
LangChain is a framework\n for building LLM       applications.
RAG stands for          Retrieval Augmented Generation.
Agents can use     tools to complete complex tasks.
Python is the primary language for AI engineering.
Vector \ndatabases store    embeddings for \nsemantic search.
Prompt engineering \nis the art of crafting effective prompts.
Fine tuning adapts a model     to specific domain knowledge."""
# func01 = clean_text(input_str=actual_input)
# print(func01)
# print("************************")
# func02 = split_into_sentences(func01)
# print(func02)
# print("************************")
# print(chunk_text(func02))
