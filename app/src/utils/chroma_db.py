import os
import shutil
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma

from .color_print import Color, ColorPrint

PATH = "chroma_db"


def save_to_chroma(chunks: list[Document], embedding_model) -> Chroma:
    """Saves document chunks to a Chroma vector store.

    Args:
        chunks (list[Document]): The document chunks to save.
        embedding_model (_type_): The embedding model to use for the chunks.

    Returns:
        Chroma: The Chroma vector store instance.
    """
    if os.path.exists(PATH):
        try:
            shutil.rmtree(PATH)
        except Exception as e:
            ColorPrint.print_colored(
                f"Error removing existing Chroma DB directory: {e}", Color.RED
            )
            raise

    db = Chroma.from_documents(
        chunks,
        persist_directory=PATH,
        embedding=embedding_model,
    )

    ColorPrint.print_colored(
        f"Saved {len(chunks)} chunks to Chroma DB at {PATH}", Color.GREEN
    )

    return db
