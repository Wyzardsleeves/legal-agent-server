# Basic imports
import os, json
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

# Environment variables
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("DEEPSEEK_API_KEY")

# Langchain imports
from langchain.chains import MultiRetrievalQAChain
from langchain_deepseek import ChatDeepSeek

# Custom imports
from helpers.loader import retriever_infos

app = Flask(__name__)

CORS(app) # Enables CORS for all routes and origins

# Access environment variables for DeepSeek
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=SECRET_KEY,
    # other params...
)

qa_chain = MultiRetrievalQAChain.from_retrievers(
  llm=llm,
  retriever_infos=retriever_infos,
  default_chain_llm=llm,
)

@app.route('/')
def index():
  return '<p>Welcome to the API.</p></br/><p>Please let Justin know if you are seeing this! (jlattimoreweb@gmail.com)</p>'


@app.route('/chat', methods=['POST'])
def chat():

  # Handle data from Frontend
  byte_string = request.data
  decoded = byte_string.decode('utf-8')
  extract = json.loads(decoded)

  question = extract.get("message")
  response = qa_chain.invoke(question)

  if not question or question == '':
    return jsonify({"error": "No question provided"}), 400

  try:
    responseBody = {
      "answer": response,
    }

    return make_response(jsonify(responseBody)), 200

  except Exception as e:
    return jsonify({"error": str(e)}), 500

