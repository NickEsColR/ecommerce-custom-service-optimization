from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunks_pdf(directory_path: str) -> list[Document]:
    """
    Splits PDF documents into chunks.

    Args:
        directory_path (str): The path to the directory containing PDF documents.

    Returns:
        list[Document]: A list of Document objects representing the chunks.
    """
    document_loader = PyPDFDirectoryLoader(directory_path)
    documents = document_loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)

    return chunks
