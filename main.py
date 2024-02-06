import sys
from langchain_community.llms import CTransformers
from langchain.callbacks import StreamingStdOutCallbackHandler
import json, os, time, random


def print_like_human(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()


def input_like_human(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    return input().lower().strip()


def file_analysis(file_path):
    file_path = os.path.normpath(file_path)
    compatible_extensions = ['.py', '.txt', '.json']

    if os.path.isdir(file_path):
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f)) and any(f.endswith(ext) for ext in compatible_extensions)]
        if files:
            print_like_human('No file was specified. Found these compatible files in the directory:')
            for idx, filename in enumerate(files, start=1):
                print_like_human(COLORS['yellow'] + f"{idx}. {filename}")
            choice = input_like_human('Please choose a file by number (or type "exit" to cancel): ')
            if choice.lower() == 'exit':
                return 'reloop'
            try:
                selected_file = files[int(choice) - 1]
                file_path = os.path.join(file_path, selected_file)
            except (ValueError, IndexError):
                print_like_human('Invalid selection. Please try again.')
        else:
            print_like_human('No compatible files found in the directory.')
            return 'reloop'

    content = ''
    if file_path.endswith('.py') or file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.dumps(json.load(file))
    return content


COLORS = {
    'blue': '\033[94m',
    'yellow': '\033[93m'
}

streaming_callback = StreamingStdOutCallbackHandler()
llm = CTransformers(
    model='D:\\Netzwerkfreigabe\\Coding Projekte\\Wolfram\\Wolfram Assistent\\model',
    model_file='wolfram.gguf',
    model_type='llama',
    gpu_layers=80,
    local_files_only=True,
    callbacks=[streaming_callback])

start_instructions = (' Your task is to provide clear answers as briefly and directly as possible, '
                      'without any unnecessary information or detail. I want the information quickly and concisely, '
                      'without any filler words or unnecessary details.')

options = ['Ask a Question', 'File analyzer', 'Exit the process']

while True:
    for idx, entry in enumerate(options, start=1):
        print_like_human(COLORS['yellow'] + f"{idx}. {entry}")
    choice = input_like_human(COLORS['blue'] + 'Choose a option by number. You can leave a mode by typing "exit". \nOption: ')
    try:
        selectedOption = int(choice)
    except ValueError:
        print_like_human("Please enter a valid number.")
        continue

    if selectedOption < 1 or selectedOption > len(options):
        print("Invalid option. Please try again.")
        continue

    if selectedOption == 1:
        while True:
            question = input(COLORS['blue'] + '\nAsk a question: ' + COLORS['yellow'])
            if question.lower() == 'exit':
                break
            question += start_instructions
            llm.invoke(question)
    elif selectedOption == 2:
        while True:
            filepath = input(COLORS['blue'] + 'Please provide me with the filepath of the file you want to analyse (or type "exit" to return).\nFilepath: ')
            if filepath.lower() == 'exit':
                break
            file_content = file_analysis(filepath)
            if file_content == 'reloop':
                continue
            question = "Analyse the following content and give a summary: " + file_content
            llm.invoke(question)
    elif selectedOption == 3:
        break