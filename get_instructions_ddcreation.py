from langchain.llms import OpenAI
from langchain import PromptTemplate

template = """
You are the engineer trying to create a data dictionary for a database.

You don't have access to the DB, but you have access to the code repository of the application which generates the data of the database.
This repository consists of mainly {language} files.
I know this application uses {db_type}, and the {table_or_collection} in the DB is the following:

{table_or_collection_name}

Write down step-b
y-step instruction on how to create the data dictionary from the application code.
"""


prompt = PromptTemplate(
    input_variables=["language", "db_type", "table_or_collection", "table_or_collection_name"],
    template=template,
)

llm = OpenAI(model_name="text-davinci-003", temperature=0.9)

res = llm(input_)
print(res)
