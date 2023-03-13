import json
import requests

# Send the "initialize" request to the language server
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "processId": None,
        "rootUri": "file:///Users/jingfangzhou/Code/src2metadata/src",
        "capabilities": {},
        "trace": "off"
    }
}
response = requests.post("http://localhost:port/language-server-python", json=request)

# Send the "textDocument/definition" request to get the definition of a variable
request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "textDocument/definition",
    "params": {
        "textDocument": {
            "uri": "file:///Users/jingfangzhou/Code/src2metadata/src/vscode_lsp.py"
        },
        "position": {
            "line": 3,
            "character": 5
        }
    }
}
response = requests.post("http://localhost:port/language-server-python", json=request)

# Print the result of the request
print(response.json())