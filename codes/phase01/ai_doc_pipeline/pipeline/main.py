import ai_pipeline as pipo

if __name__ == "__main__":
    pipeline = pipo.AIPipeline()
    #(chunk_size = 15, overlap =3)
    pipeline.statuss()
    results = pipeline.run("sample_doc.txt")
    pipeline.statuss()