import gradio as gr
import ollama

def format_history(msg:str, history:list[list[str,str]], system_prompt:str):
    chat_history = [{"role":"system", "content":system_prompt}]
    for query, response in history:
        chat_history.append({"role":"user", "content":query})
        chat_history.append({"role":"system", "content":response})
    chat_history.append({"role":"user", "content":msg})
    return chat_history

def generate_response(msg:str, history:list[list[str,str]], system_prompt:str):
    chat_history = format_history(msg, history, system_prompt)
    response = ollama.chat(model = "llama3", stram=True, messages = chat_history)
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token
        yield message
        
