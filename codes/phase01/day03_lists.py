import day02 # Assuming day02.py contains some relevant code we want to use

documents = [
    "AI is transforming the software industry",
    "LangChain helps build LLM applications",
    "RAG stands for Retrieval Augmented Generation",
    "Agents can use tools to complete tasks",
    "Python is the primary language for AI engineering"
]
def doc_analyser(documents):
    results = []
    for i, ind in enumerate(documents):
        result = {'text': ind, 'Words': day02.get_word_count(ind), 'Chars': day02.get_char_count(ind), 'Upper': day02.make_upper(ind)}
        results.append(result)
    return results

results_end = doc_analyser(documents)

for i, ind in enumerate(results_end):
    print(f"Document {i+1}:\n\t Text: {ind['text']}\n\t Word Count: {ind['Words']}\n\t Character Count: {ind['Chars']}\n\t Uppercase: {ind['Upper']}\n")

# result_dic = {}
# n = len(documents)

# for i in range(n):
#     doc = documents[i]
#     word_count = day02.get_word_count(doc)
#     char_count = day02.get_char_count(doc)
#     upperCase = day02.make_upper(doc)
#     #pre-result = {'text': doc, 'Words': word_count, 'Chars': char_count, 'Upper': upperCase}    
#     print(f"Document {i+1}:\n\t Text: {doc}\n\t Word Count: {word_count}\n\t Character Count: {char_count}\n\t Uppercase: {upperCase}\n")


