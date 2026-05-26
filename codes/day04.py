import day02 # Assuming day02.py contains some relevant code we want to use

            
def safe_analyse(documents):
    try:
        if not isinstance(documents, list):
            print("Error: Input is not a list of documents.")
            return None
        elif len(documents) == 0:
            print("Warning: The document list is empty.")
            return []
        else:
            results = []
            for i, ind in enumerate(documents):
                if isinstance(ind, str):
                    result = {'text': ind, 'Words': day02.get_word_count(ind), 'Chars': day02.get_char_count(ind), 'Upper': day02.make_upper(ind)}
                    results.append(result)
                else:
                    print(f"Warning: Document {i+1} is not a string and will be skipped.")
            print(f"Number of valid documents analyzed: {len(results)}")
            return results       
    except Exception as e:
        print(f"Error: {e}")
        

doc_Normal = ["AI is powerful", "Python is great"]
doc_empty = []
doc_mixed = ["Valid sentence", 12345, None, "Another valid one"]
doc_notList = "I forgot to put this in a list"
doc_collection = [doc_Normal, doc_empty, doc_mixed, doc_notList]
#doc_collection = [ doc_empty, ]
for i, ind in enumerate(doc_collection):
    print(f"Analyzing Document Set {i+1}:")
    result = safe_analyse(ind)
    if result is not None:
        for j, res in enumerate(result):
            print(f"\tDocument {j+1}:\n\t\t Text: {res['text']}\n\t\t Word Count: {res['Words']}\n\t\t Character Count: {res['Chars']}\n\t\t Uppercase: {res['Upper']}\n")

            

