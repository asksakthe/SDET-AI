import time
import chunker as d7
import llm_caller as d5

class AIPipeline:
    def __init__(self):
        self.chunks = []
        self.results = []

    def document_processing(self, file_name,chunk_size = 10, overlap = 3):
        self.chunk_size = chunk_size
        self.overlap = overlap
        print("\t\t===== Documents processing to chunks =====\n")
        self.chunks = d7.process_doc(filName=file_name, chunk_Siz = self.chunk_size, overlap=self.overlap)
        #print(len(self.chunks))
        return self.chunks
    
    def summarise(self):
        # loop through self.chunks
        # call day05 safe_call_llm for each chunk
        # store results in self.results
        # print progress for each chunk
        # use time.sleep(1) between calls
        if not self.chunks:
            print("No Chunks available, call doc")
            return []
        for i, chunk in enumerate(self.chunks):
            #print(f"\t\t******  *Summarising the Chunk {i+1}  *************\n")
            prompt = f"Summarise this with exact 5 words {chunk['text']}"
            calling_d5 = d5.safe_call_llm(prompt)
            self.results.append({'chunk_ID': i+1, 'Doc_txt_Chunk':chunk['text'], 'Doc_txt_Count':chunk['wordsCount'],'AI_Thought':calling_d5})
            #print(f"{self.results}\n")
            time.sleep(5)
        return self.results
    
    def run_pipeline(self, file_name):
        print(f"========== Pipeline Begins =============\n")
        func01 = self.document_processing(file_name)
        func02 = self.summarise()
        return func02

    def Statuss(self):
        return f"+++++++++++++++++++  Totally {len(self.chunks)} and {len(self.results)} ++++++++++++++++++++++"


if __name__ == "__main__":
    class_obj = AIPipeline()
    class_obj.run_pipeline("secondFile.txt")
    print(class_obj.Statuss())
    class_obj.summarise()
    print(class_obj.Statuss())


                
