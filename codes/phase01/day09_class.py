#import os
import day07_02chunker as d7

class AIPipeline:
    def __init__(self, chunk_size = 10, overlap = 3):
        self.chunks = []
        self.results = []

    def document_processing(self, file_name):
        print("===== Documents processing to chunks =====")
        self.chunks = d7.process_doc(filName=file_name)
        print(len(self.chunks))
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
        for chunk in self.chunks:
            print(chunk)
        return self.chunks


if __name__ == "__main__":
    class_obj = AIPipeline()
    class_obj.document_processing("secondFile.txt")
    class_obj.summarise()


                
