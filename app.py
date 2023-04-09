from flask import Flask, render_template, request
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from config import Config

app = Flask(__name__)

config = Config()
app.secret_key = config.SECRET_KEY
openai_api_key = config.openai_api_key


with open("./en.yusufali.txt", "r") as f:
  quran_text = ' '.join([t.split("\n")[0] for t in f.readlines()])




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        result = ask_holy_quran(query)
        return render_template('index.html', result=result)
    return render_template('index.html')

def ask_holy_quran(query):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(quran_text)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts, embeddings)
    qa = VectorDBQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type="stuff", vectorstore=vectorstore)
    return qa.run(query)

if __name__ == '__main__':
    app.run(debug=True)
