from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import json 
import http.server
import socketserver
import cgi
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a normal assitant. but you are currently being run on an old mobile phone from 2000s running symbian operating system. Make the response much shorter than usual (due to limit of older phone capability) less than 200 character unless you really have to"),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'API only support POST response')
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        # Parse the form data
        form_data = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type']})

        # Extract the value of the "prompt" field from the form data
        promptinput = form_data.getvalue('prompt', '')
        cv = conversation.predict(input=promptinput)
        # Process the prompt as needed
        # ...

        response_message = cv
        response_body = response_message.encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_body)
# print(conversation.predict(input="Hi there!"))


def run_server():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("[SymbianGPT] Server started at <all ip>:" + str(PORT))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        print("Server stopped.")


if __name__ == '__main__':
    run_server()