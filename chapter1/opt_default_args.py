# coding: utf-8
def sayhello(message="Hello World", caps=False):
    print(message.upper() if caps else message)
    
sayhello()
sayhello(message="hi there", caps=True)
