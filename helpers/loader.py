# Langchain imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# add a try/except 
import os

def get_pdf_files():
  """Get all PDF files from the resources directory"""
  resources_dir = "./resources"
  pdf_files = [f for f in os.listdir(resources_dir) if f.endswith('.pdf')]
  return(sorted(pdf_files))

pdfList = get_pdf_files()

retrievers = {}
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

for pdf in pdfList:
  pdf_name = pdf.removesuffix(".pdf").lower().replace(' ', '_').replace('-', '_').replace('.', '_').replace('&', 'and').replace('__', '_').replace("'", "").replace("(", "").replace(")", "") # I used AI for this line I look foward to discussing whether or not this is slop.

  try:
    print(f"Loading {pdf}...")
    # Create loaders for each PDF
    pdf_loader = PyPDFLoader(f"./resources/{pdf}")
    # Load PDF documents
    pdf_docs = pdf_loader.load()
    # Create vectorstores
    pdf_vectorstore = FAISS.from_documents(pdf_docs, embeddings)
    # Create retrievers
    pdf_retriever = pdf_vectorstore.as_retriever()
    # Add retriever to dictionary
    retrievers[f'{pdf_name}_retriever'] = pdf_retriever
    print(f"Successfully loaded {pdf}")
  except Exception as e:
    print(f"ERROR loading {pdf}: {str(e)}")
    # Skip this PDF and continue with the next one
    continue

# Create router with metadata
retriever_infos = [
  {
    "name": "North Carolina Constitution",
    "description": "This is for North Carolina's constitution.",
    "retriever": retrievers['north_carolina_constitution_retriever']
  },
  {
    "name": "Legal Survival Guide - Florida Laws You Should Know",
    "description": "Use this retriever for Florida laws and fun-facts that are good to be aware of.",
    "retriever": retrievers['legal_survival_guide_florida_retriever']
  },
  {
    "name": "Florida Board of Bar Examiners",
    "description": "Use this retriever for any concerns regarding the BAR exam, more specifically Florida's bar.",
    "retriever": retrievers['florida_board_of_bar_examiners_retriever']
  },
  {
    "name": "Texas Constitution",
    "description": "Use this to reference anything concerning Texas's Constitution.",
    "retriever": retrievers['texas_constitution_retriever']
  },
  {
    "name": "Texas Business and Commerce Code",
    "description": "Use this as reference for the Business and Commerce laws and rules within the State of Texas.",
    "retriever": retrievers['texas_business_commerce_retriever']
  },
  {
    "name": "Texas Alchoholic Beverage Code",
    "description": "Use this as reference for the Alchoholic Beverage laws and rules within the State of Texas.",
    "retriever": retrievers['texas_alchoholic_beverage_retriever']
  },
  {
    "name": "Texas Election Code",
    "description": "Use this retriever for any concerns regarding the rules and laws of the Texas election process.",
    "retriever": retrievers['texas_election_code_retriever']
  },
  {
    "name": "Texas Estates Code",
    "description": "Use this as reference for the Estates Code laws and rules within the State of Texas.",
    "retriever": retrievers['texas_estates_code_retriever']
  },
  {
    "name": "The Smart Guide to the MBE",
    "description": "This retriever is for the MBE and the BAR Exam.",
    "retriever": retrievers['the_smart_guide_mbe_retriever']
  },
  {
    "name": "NYC Laws",
    "description": "Use in regards to the general laws within New York City.",
    "retriever": retrievers['nyc_laws_retriever']
  },
  {
    "name": "New York City Zoning Laws",
    "description": "Use this to refer to any ordinance or zoning laws within New York City.",
    "retriever": retrievers['new_york_city_zoning_laws_retriever']
  },
  {
    "name": "Basic Laws Book 2016",
    "description": "Use this to refer to the basic laws of the United States of America.",
    "retriever": retrievers['basic_laws_book_2016_retriever']
  },
  {
    "name": "Constitution of the United States",
    "description": "Use this retriever as a reference to the Constitution of the United States.",
    "retriever": retrievers['constitution_retriever']
  },
  {
    "name": "Lobby Guide Texas",
    "description": "Use this to refer to the rules concerning Lobbying in the state of Texas.",
    "retriever": retrievers['lobby_guide_texas_retriever']
  }
]
