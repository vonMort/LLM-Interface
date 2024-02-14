import src.logger as lg
from src.logger import COLORS
import os, json


def file_analyser_logic(llm):
    while True:
        filepath = input(lg.COLORS[
                             'blue'] + 'Please provide me with the filepath of the file you want to analyse (or type "exit" to return).\nFilepath: ')
        if filepath.lower() == 'exit':
            break
        file_content = file_analysis(filepath)
        if file_content == 'reloop':
            continue
        question = "Analyse the following content and give a summary: " + file_content
        llm.invoke(question)


def file_analysis(file_path):
    file_path = os.path.normpath(file_path)
    compatible_extensions = ['.py', '.txt', '.json']

    if os.path.isdir(file_path):
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f)) and any(f.endswith(ext) for ext in compatible_extensions)]
        if files:
            lg.print_like_human('No file was specified. Found these compatible files in the directory:')
            for idx, filename in enumerate(files, start=1):
                lg.print_like_human(COLORS['yellow'] + f"{idx}. {filename}")
            choice = lg.input_like_human('Please choose a file by number (or type "exit" to cancel): ')
            if choice.lower() == 'exit':
                return 'reloop'
            try:
                selected_file = files[int(choice) - 1]
                file_path = os.path.join(file_path, selected_file)
            except (ValueError, IndexError):
                lg.print_like_human('Invalid selection. Please try again.')
        else:
            lg.print_like_human('No compatible files found in the directory.')
            return 'reloop'

    content = ''
    if file_path.endswith('.py') or file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.dumps(json.load(file))
    return content
