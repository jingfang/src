# file to get table description from a file

from langchain.llms import OpenAI
from langchain import PromptTemplate

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

start_prompt = PromptTemplate(
    input_variables=["code"],
    template=start_template,
)


llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

root_dir = '/Users/jingfangzhou/Code/src2metadata/'
file_path = root_dir + 'netcon-score-server/ui/components/problems/id/GradingForm.vue'

# get content of filepath as code
with open(file_path, 'r') as f:
    code = f.read()

column = "answer"
table = "confirming"
type_ = "boolean"

input_ = start_prompt.format(column=column,table=table, type=type_, code=code)
res = llm(input_)

print(res)