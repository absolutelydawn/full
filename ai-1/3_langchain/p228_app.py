from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstors import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import PromptTemplate

examples = [
    {"input"}
]