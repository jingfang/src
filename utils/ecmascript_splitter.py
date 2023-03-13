import re

file_path = '/Users/jingfangzhou/Code/src2metadata/roseflix-backend/src/models/user.ts'

# split outermost code block
def split_outermost_blocks(file_path):
    # read file by line
    with open(file_path, 'r') as f:
        lines = f.readlines()
    outermost_blocks = []
    start_line = 0
    cur_line = 0
    parenthesis_count = 0
    brace_count = 0
    while cur_line < len(lines):
        # if the current line is empty, skip it
        if lines[cur_line].strip() == '':
            cur_line += 1
            continue
        # check if the current line is the end of the outermost block
        # if so, add the block to the list
        # and update the start_line and end_line
        # else, just update the end_line
        
        # count unsolved parenthesis and braces in the line
        parenthesis_count += lines[cur_line].count("(")
        parenthesis_count -= lines[cur_line].count(")")
        brace_count += lines[cur_line].count("{")
        brace_count -= lines[cur_line].count("}")
        # if both of them are 0, then it is a outermost block
        if parenthesis_count == 0 and brace_count == 0:
            end_line = cur_line + 1
            outermost_blocks.append(lines[start_line:end_line])
            start_line = end_line
        cur_line += 1

    # concat each block into a string
    outermost_blocks = [''.join(block) for block in outermost_blocks]

    return outermost_blocks

# outermost_blocks = split_outermost_blocks(file_path)
# for block in outermost_blocks:
#     print('new block')
#     for line in block:
#         print(line, end='')

# split large chunks of code into smaller chunks
def split_large_chunk(chunk):
    # Not implemented yet
    return [chunk]
    # return chunks

# split file into chunks which is smaller than 1000 tokens but as large as possible
def split_ecmascript_file(file_path, max_tokens=1000):
    outermost_blocks = split_outermost_blocks(file_path)
    chunks = []
    chunk = ''
    num_large_tokens = 0
    for block in outermost_blocks:
        if len(block) > max_tokens:
            chunks += split_large_chunk(block)
            num_large_tokens += 1
        if len(chunk) + len(block) < max_tokens:
            chunk += block
        else:
            chunks.append(chunk)
            chunk = block
    print(f"Found {num_large_tokens} large chunks")
    return chunks

chunks = split_ecmascript_file(file_path)
for chunk in chunks:
    print('new chunk')
    for line in chunk:
        print(line, end='')