import os
import PyPDF2
os.environ["OPENAI_API_KEY"] = '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'

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader('./data').load_data()
# index = GPTSimpleVectorIndex.from_documents(documents)
# print(index)

# response = index.query("summarize this article")
# print(response) 

pdfFileObj = open('./data/DONE_NL103_shannon.pdf', encoding="latin1")
pdfReader = PyPDF2.PdfReader(pdfFileObj)

pageObj = pdfReader.pages[0] 
x=pageObj.extract_text()

index = GPTSimpleVectorIndex.from_documents(x)


response = index.query("summarize this article")
print(response) 
pdfFileObj.close()