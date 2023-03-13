prompt = """
You as an assitant engineer are trying to create a data dictionary for a database.
What is the schema and desciption of the columns you can infer from the following code?:

  create_table "issue_comments", id: :uuid, default: -> { "gen_random_uuid()" }, force: :cascade do |t|
    t.string "text", null: false
    t.boolean "from_staff", null: false
    t.uuid "issue_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["issue_id"], name: "index_issue_comments_on_issue_id"
  end
  
Return the table schema in the following format:

# Table name 1
(describe what does each record mean here)
## column description
| Column name | type | PK | FK | required | description|
| --- | --- | --- | --- | --- | --- |
| column name 1 | string | No | No | Yes | (description of the column name 1) |
| column name 2 | Boolean | No | No | Yes | (description of the column name 2) |
...
## index description
- index 1: description

"""

list_markdown_represenation = """
give me text representation of the markdown table of the above column description
"""

list_up_enum_prompt = """
list all the integer columns which might effectively enum (meaning, they are only expected to have certain types of value, and they are assigned different meanings.).

example 1:
| Column name | Type | PK | FK | Required | Description |
| --- | --- | --- | --- | --- | --- |
| age | integer | No | No | No | Age of the customer. |
| gender | integer | No | No | No | Gender of the customer. |
| created_at | datetime | No | No | Yes | Timestamp indicating when the customer setting was created. |

answer: gender

example 2:
| Column name | Type | PK | FK | Required | Description |
| --- | --- | --- | --- | --- | --- |
| age | integer | No | No | No | Age of the customer. |
| gender | string | No | No | No | Gender of the customer. |
| created_at | datetime | No | No | Yes | Timestamp indicating when the customer setting was created. |

answer: No matching column found.

example 3:
| Column name  | Type    | PK   | FK   | Required | Description                                                      |
| ------------ | ------- | ---- | ---- | -------- | ---------------------------------------------------------------- |
| id           | uuid    | Yes  | No   | Yes      | Unique identifier for each record in the `categories` table      |
| code         | string  | No   | No   | Yes      | Code representing a category                                      |
| title        | string  | No   | No   | Yes      | Title of the category                                             |
| description  | string  | No   | No   | Yes      | Description of the category                                       |
| order        | integer | No   | No   | Yes      | Ordering of the category                                          |
| created_at   | datetime| No   | No   | Yes      | Timestamp of when the record was created                          |
| updated_at   | datetime| No   | No   | Yes      | Timestamp of when the record was last updated                     |

answer: (generate the answer here)

You should simply reply with the column name or "No matching column found.". Don't add any explanation.
"""