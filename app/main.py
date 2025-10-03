import dotenv
import os
from langchain_azure_ai.embeddings import AzureAIEmbeddingsModel

from src.utils.text_preprocessor import chunks_pdf
from src.utils.chroma_db import save_to_chroma
from src.utils.color_print import Color, ColorPrint

dotenv.load_dotenv()

documents_directory_path = "documents"
endpoint = "https://models.github.ai/inference"
model_name = "openai/text-embedding-3-small"
git_token = os.environ["GITHUB_TOKEN"]

chunks = chunks_pdf(documents_directory_path)

embedding_model = AzureAIEmbeddingsModel(
    endpoint=endpoint, credential=git_token, model=model_name
)

db = save_to_chroma(chunks, embedding_model)

query = "¿Como puedo pagar?"

docs = db.similarity_search(query, k=1)

context = "\n\n---\n\n".join([doc.page_content for doc in docs])

ColorPrint.print_colored(f"Context: {context}", Color.CYAN)
