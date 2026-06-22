import llm_caller as d05
import chunker as d07
import time

#function to perform ai insights on each chunks
def summarise_chunks(chunks):
     # INPUT: list of dicts from day07 — already chunked
    # chunks = [{"chunk_id":1, "text":"...", "word_count":10}, ...]
    results = []
    n = len(chunks)
    for i, textu in enumerate(chunks):
        print(f" Summarising the Chunks {i+1} of total")
        prompt = f"Summarise this exact 5 words : {textu['text']}"
        summary = d05.safe_call_llm(prompt=prompt)
        results.append({'chunk_id': textu['chunk_ID'],'OG_text': textu['text'],'words_Count': textu['wordsCount'], 'Summary':summary})
    time.sleep(3)
    return results

def run_pipeline(chunks):
    print(f"Pipeline begins...")
    print("-"*35 )
    #step 02
    Chunks = d07.process_doc(chunks)
    print(f"Total Chunks: {len(Chunks)}")
    #step 03
    Results = summarise_chunks(Chunks)
    #step 04
    print("*" * 40)
    # for i in Results:
    #     print(f"\nChunk  :{i['chunk_id']}")
    #     print(f"\tOriginal :{i['or']}") 

    return Results
    # input_doc = d07.process_doc(chunks)
    # result_doc = input_doc
    # calling_LLM = summarise_chunks(chunks)
    # #print(calling_LLM[0])
    # for i in range(len(calling_LLM)):
    #     result_doc[i].update({'ai_output': calling_LLM[i]['ai_text']})
    # return result_doc
      
if "__main__" == __name__:
    print(run_pipeline("secondFile.txt"))