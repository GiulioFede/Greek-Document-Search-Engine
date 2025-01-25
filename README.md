# Greek Document Search Engine

## Overview

The **Greek Document Search Engine** is a powerful search tool designed for querying large databases of Greek documents. This project utilizes advanced natural language processing (NLP) and machine learning techniques to provide accurate search results from a selection of pre-indexed texts. The system is built with flexibility in mind, allowing users to specify various search parameters and customize the number of results they want to retrieve.

Users can input a query in Greek, and the system will return the most relevant sentences from documents based on the context of the search term, highlighting matching words and citations within the text. 

### Key Features
- **Flexible Query Input**: Users can input Greek text and specify the number of results they want to retrieve.
- **Contextual Search**: The search engine analyzes the context and content of the query, matching it to the most relevant sentences in various documents in the database.
- **Word Matching & Highlighting**: The engine highlights common words between the query and the results to provide better search accuracy.
- **Citations Highlighting**: Citations within the results are highlighted and can be hovered over to show additional information.

### How It Works

1. **User Input**: The user inputs a Greek text query into the system along with the number of search results they wish to retrieve.
2. **Text Processing**: The query text is preprocessed to normalize any special characters, removing unnecessary spaces and invisible characters.
3. **Model & Index Loading**: The system loads a pre-trained masked language model (https://huggingface.co/bowphs/GreBerta) and an index built from the Greek document database to retrieve the best matches.
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

### Dataset
The dataset, which cannot be shared, must be structured as follows:
- db_folder
   1. document_1
      - json_file_1
      - json_file_2
      - ....

   2. document_2
      - json_file_1
      - json_file_2
      - ....
where each json has this format (an example in provided):
```
{
    "author_id": "1207",
    "id": "001",
    "name": "Fragmenta Aratea",
    "content": [
        {
            "citation": "1.1",
            "text": " Hipparch. I p. 1013A (178P. 24M.) ὅτι μὲν οὖν Εὐδόξωι "
        },
        {
            "text": "ἐπακολουθήσας ὁ Ἄρατος συντέταχε τὰ Φαινόμενα, ἱκανῶς οἶ"
        },
        {
            "text": "μαι δεικνύναι διὰ τῶν προειρημένων, ἐν οἷς δὲ διαπίπτουσιν "
        },
        {
            "text": "οὗτοί τε καὶ οἱ συνεπιγραφόμενοι αὐτοῖς, ὧν ἐστι καὶ Α*ΤΤΑΛΟΣ, "
        },
        {
            "citation": "1.5",
            "text": "νῦν ὑποδείξομεν. ἐκθησόμεθα δὲ εὐθέως καὶ ἐν οἷς ἰδίαι ἕκαστος "
        },
      ...
```
### Running the Project
To create a FAISS index and a SQL database, run the following script:
```
nohup python -u create_index.py --config "/home/giuliofederico/Itserr/config/index_config.py" > log.txt 2>&1 &
```


