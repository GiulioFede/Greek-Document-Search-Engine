# Greek Document Search Engine

## Overview

The **Greek Document Search Engine** is a powerful search tool designed for querying large databases of Greek documents. This project utilizes advanced natural language processing (NLP) and machine learning techniques to provide accurate search results from a selection of pre-indexed texts. The system is built with flexibility in mind, allowing users to specify various search parameters and customize the number of results they want to retrieve.

Users can input a query in Greek, and the system will return the most relevant documents based on the context of the search term, highlighting matching words and citations within the text. The system also offers a robust interface with interactive features such as citations tooltips and word highlighting to improve the user experience.

### Key Features
- **Flexible Query Input**: Users can input Greek text and specify the number of results they want to retrieve.
- **Contextual Search**: The search engine analyzes the context and content of the query, matching it to the most relevant documents in the database.
- **Citations Highlighting**: Citations within the results are highlighted and can be hovered over to show additional information.
- **Search across Multiple Databases**: The system supports querying across various pre-configured databases and indexes, making it adaptable to different document collections.
- **Word Matching & Highlighting**: The engine highlights common words between the query and the results to provide better search accuracy.

### How It Works

1. **User Input**: The user inputs a Greek text query into the system along with the number of search results they wish to retrieve.
2. **Text Processing**: The query text is preprocessed to normalize any special characters, removing unnecessary spaces and invisible characters.
3. **Model & Index Loading**: The system loads a pre-trained masked language model and an index built from the Greek document database to retrieve the best matches.
4. **Database Search**: The system uses a combination of FAISS for fast similarity search and SQLite for managing metadata about the documents in the database.
5. **Result Presentation**: The system outputs a series of results with contextual matches, showing relevant document sections. Citations within these matches are highlighted and can be interacted with for further information.

### Requirements

- Python 3.x
- Gradio
- Hugging Face Transformers
- FAISS
- SQLite
- PyTorch
- Absl

### Installation

To install the necessary dependencies, you can use the following command:

```bash
pip install -r requirements.txt
