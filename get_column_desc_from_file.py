# file to get table description from a file

from langchain.llms import OpenAI
from langchain import PromptTemplate

from utils.ecmascript_splitter import split_ecmascript_file

start_template = """
You as an assitant engineer are trying to create a data dictionary for a database.
You are given a file that might contains the description of column {column} of table {table}.
The {column} is of type {type}.
What is the mapping between value and description of the column {column} you can infer from the following code?:

Code:
{code}

Return the value-description mapping in the following format:
- value1: description1
- value2: description2
"""

following_template = """
As an assistant engineer, you are tasked with creating a data dictionary for a database. 
The previous output listed below contains the schema that you inferred from the database. 
{prev_output}

Now, you have been provided with the following additional code from the same repository, and you need to update the database description and sample data based on the new information.
{code}

Using the code provided, you should update the description of the database and sample data for each table in the schema. 
The updated data dictionary will provide useful information for business analyst using the database.

To update the data dictionary, you should follow the same format as before:
# Table name 1
- column name 1: (description of the meaning of this column that can be inferred from the code)
- column name 2: (description of the meaning of this column that can be inferred from the code)

## sample data of table name 1
- column name 1: generated sample data
- column name 2: generated sample data
"""


start_prompt = PromptTemplate(
    input_variables=["code"],
    template=start_template,
)

following_prompt = PromptTemplate(
    input_variables=["code", "prev_output"],
    template=following_template,
)

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

intermidiate_results = []

def get_table_desc_from_ts_file(filename):
    chunks = split_ecmascript_file(filename)
    for i, chunk in enumerate(chunks):
        if i == 0:
            input_ = start_prompt.format(code=chunk)
        else:
            input_ = following_prompt.format(code=chunk, prev_output=res)
        res = llm(input_)
        print(input_)
        print('res')
        print(res)
        print('---')
        intermidiate_results.append(res)
    final_result = res
    return final_result, intermidiate_results

file_path = '/Users/jingfangzhou/Code/src2metadata/roseflix-backend/src/models/user.ts'
final_result, intermidiate_results = get_table_desc_from_ts_file(filename=file_path)
print(intermidiate_results)
print(final_result)

    # for chunk in chunks:
    #     input_ = start_prompt.format(code=chunk)
    #     print(input_)
    #     res = llm(input_)
    #     print(res)
    #     ress.append(res)

# for res in ress:
#     print(res)