# SymbianGPT-Backend
Backend for SymbianGPT. used as a bridge between symbian script and open ai api

This Backend need to be run in order to use SymbianGPT

Requirement:
-Python 3
-OpenAI API Key

How To Run:
1,Run pip -r requirement.txt to get all the required module
2.run export OPENAI_API_KEY=<your open ai key here> 
3.run the server using "python server.py" (or "python3 server.py" on linux based server)
4.once it is running you are ready to use SymbianGPT (make sure the url is set correctly)

Limitation:
-Currently it is only designed for single user use. this is not recommended to be hosted on public server and the memory feature is saved on memory and shared for all session (the only way to reset it is to restart the server)
