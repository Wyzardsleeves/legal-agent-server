# Langchain imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load documents
north_carolina_constitution_loader = PyPDFLoader("./resources/NorthCarolina_Constitution.pdf")
legal_survival_guide_florida_loader = PyPDFLoader("./resources/Legal Survival Guide - Florida Laws You Should Know.pdf")
florida_board_of_bar_examiners_loader = PyPDFLoader("./resources/Florida Board of Bar Examiners.pdf")
texas_constitution_loader = PyPDFLoader("./resources/Texas Constitution.pdf")
texas_business_commerce_loader = PyPDFLoader("./resources/Texas_BUSINESSANDCOMMERCECODE.pdf")
texas_alchoholic_beverage_loader = PyPDFLoader("./resources/Texas_ALCOHOLICBEVERAGECODE.pdf")
texas_election_code_loader = PyPDFLoader("./resources/Texas_ELECTIONCODE.pdf")
texas_estates_code_loader = PyPDFLoader("./resources/Texas_ESTATESCODE.pdf")
the_smart_guide_mbe_loader = PyPDFLoader("./resources/The-Smart-Guide-to-the-MBE.pdf")
nyc_laws_loader = PyPDFLoader("./resources/nyc_laws.pdf")
new_york_city_zoning_laws_loader = PyPDFLoader("./resources/new_york_city_zoning_laws.pdf")
basic_laws_book_2016_loader = PyPDFLoader("./resources/basic-laws-book-2016.pdf")
constitution_loader = PyPDFLoader("./resources/constitution.pdf")
lobby_guide_texas_loader = PyPDFLoader("./resources/lobby_guide_texas.pdf")

# Load PDF documents
nc_constitution_pdf_docs = north_carolina_constitution_loader.load()
legal_survival_guide_florida_pdf_docs = legal_survival_guide_florida_loader.load()
florida_board_of_bar_examiners_pdf_docs = florida_board_of_bar_examiners_loader.load()
texas_constitution_pdf_docs = texas_constitution_loader.load()
texas_business_commerce_pdf_docs = texas_business_commerce_loader.load()
texas_alchoholic_beverage_pdf_docs = texas_alchoholic_beverage_loader.load()
texas_election_code_pdf_docs = texas_election_code_loader.load()
texas_estates_code_pdf_docs = texas_estates_code_loader.load()
the_smart_guide_mbe_pdf_docs = the_smart_guide_mbe_loader.load()
nyc_laws_pdf_docs = nyc_laws_loader.load()
new_york_city_zoning_laws_pdf_docs = new_york_city_zoning_laws_loader.load()
basic_laws_book_2016_pdf_docs = basic_laws_book_2016_loader.load()
constitution_pdf_docs = constitution_loader.load()
lobby_guide_texas_pdf_docs = lobby_guide_texas_loader.load()


# Create vectorstores
north_carolina_constitution_vectorstore = FAISS.from_documents(nc_constitution_pdf_docs, embeddings)
legal_survival_guide_florida_vectorstore = FAISS.from_documents(legal_survival_guide_florida_pdf_docs, embeddings)
florida_board_of_bar_examiners_vectorstore = FAISS.from_documents(florida_board_of_bar_examiners_pdf_docs, embeddings)
texas_constitution_pdf_vectorstore = FAISS.from_documents(texas_constitution_pdf_docs, embeddings)
texas_business_commerce_vectorstore = FAISS.from_documents(texas_business_commerce_pdf_docs, embeddings)
texas_alchoholic_beverage_vectorstore = FAISS.from_documents(texas_alchoholic_beverage_pdf_docs, embeddings)
texas_election_code_vectorstore = FAISS.from_documents(texas_election_code_pdf_docs, embeddings)
texas_estates_code_vectorstore = FAISS.from_documents(texas_estates_code_pdf_docs, embeddings)
the_smart_guide_mbe_vectorstore = FAISS.from_documents(the_smart_guide_mbe_pdf_docs, embeddings)
nyc_laws_vectorstore = FAISS.from_documents(nyc_laws_pdf_docs, embeddings)
new_york_city_zoning_laws_vectorstore = FAISS.from_documents(new_york_city_zoning_laws_pdf_docs, embeddings)
basic_laws_book_2016_vectorstore = FAISS.from_documents(basic_laws_book_2016_pdf_docs, embeddings)
constitution_vectorstore = FAISS.from_documents(constitution_pdf_docs, embeddings)
lobby_guide_texas_vectorstore = FAISS.from_documents(lobby_guide_texas_pdf_docs, embeddings)


# Create retrievers
north_carolina_constitution_retriever = north_carolina_constitution_vectorstore.as_retriever()
legal_survival_guide_florida_retriever = legal_survival_guide_florida_vectorstore.as_retriever()
florida_board_of_bar_examiners_retriever = florida_board_of_bar_examiners_vectorstore.as_retriever()
texas_constitution_pdf_retriever = texas_constitution_pdf_vectorstore.as_retriever()
texas_business_commerce_retriever = texas_business_commerce_vectorstore.as_retriever()
texas_alchoholic_beverage_retriever = texas_alchoholic_beverage_vectorstore.as_retriever()
texas_election_code_retriever = texas_election_code_vectorstore.as_retriever()
texas_estates_code_retriever = texas_estates_code_vectorstore.as_retriever()
the_smart_guide_mbe_retriever = the_smart_guide_mbe_vectorstore.as_retriever()
nyc_laws_retriever = nyc_laws_vectorstore.as_retriever()
new_york_city_zoning_laws_retriever = new_york_city_zoning_laws_vectorstore.as_retriever()
basic_laws_book_2016_retriever = basic_laws_book_2016_vectorstore.as_retriever()
constitution_retriever = constitution_vectorstore.as_retriever()
lobby_guide_texas_retriever = lobby_guide_texas_vectorstore.as_retriever()

# Create router with metadata
retriever_infos = [
  {
    "name": "North Carolina Constitution",
    "description": "This is for North Carolina's constitution.",
    "retriever": north_carolina_constitution_retriever
  },
    {
    "name": "Legal Survival Guide - Florida Laws You Should Know",
    "description": "Use this retriever for Florida laws and fun-facts that are good to be aware of.",
    "retriever": legal_survival_guide_florida_retriever
  },
  {
    "name": "Florida Board of Bar Examiners",
    "description": "Use this retriever for any concerns regarding the BAR exam, more specifically Florida's bar.",
    "retriever": florida_board_of_bar_examiners_retriever
  },
  {
    "name": "Texas Constitution",
    "description": "Use this to reference anything concerning Texas's Constitution.",
    "retriever": texas_constitution_pdf_retriever
  },
  {
    "name": "Texas Business and Commerce Code",
    "description": "Use this as reference for the Business and Commerce laws and rules within the State of Texas.",
    "retriever": texas_business_commerce_retriever
  },
  {
    "name": "Texas Alchoholic Beverage Code",
    "description": "Use this as reference for the Alchoholic Beverage laws and rules within the State of Texas.",
    "retriever": texas_alchoholic_beverage_retriever
  },
  {
    "name": "Texas Election Code",
    "description": "Use this retriever for any concerns regarding the rules and laws of the Texas election process.",
    "retriever": texas_election_code_retriever
  },
  {
    "name": "Texas Estates Code",
    "description": "Use this as reference for the Estates Code laws and rules within the State of Texas.",
    "retriever": texas_estates_code_retriever
  },
  {
    "name": "The Smart Guide to the MBE",
    "description": "This retriever is for the MBE and the BAR Exam.",
    "retriever": the_smart_guide_mbe_retriever
  },
  {
    "name": "NYC Laws",
    "description": "Use in regards to the general laws within New York City.",
    "retriever": nyc_laws_retriever
  },
  {
    "name": "New York City Zoning Laws",
    "description": "Use this to refer to any ordinance or zoning laws within New York City.",
    "retriever": new_york_city_zoning_laws_retriever
  },
  {
    "name": "Basic Laws Book 2016",
    "description": "Use this to refer to the basic laws of the United States of America.",
    "retriever": basic_laws_book_2016_retriever
  },
  {
    "name": "Constitution of the United States",
    "description": "Use this retriever as a reference to the Constitution of the United States.",
    "retriever": constitution_retriever
  },
  {
    "name": "Lobby Guide Texas",
    "description": "Use this to refer to the rules concerning Lobbying in the state of Texas.",
    "retriever": lobby_guide_texas_retriever
  }
]
