from langchain_community.llms import CTransformers
from langchain.callbacks import StreamingStdOutCallbackHandler
from src.question import question_asker_logic
from src.fileanalyser import file_analyser_logic
from src.trainer import trainer_logic
import src.logger as lg


def initialize_llm():
    streaming_callback = StreamingStdOutCallbackHandler()
    llm = CTransformers(
        model='.//model',
        model_file='wolfram.gguf',
        model_type='llama',
        gpu_layers=80,
        local_files_only=True,
        callbacks=[streaming_callback])
    return llm


options = ['Ask a Question', 'File analyzer', 'Training', 'Exit the process']

while True:
    for idx, entry in enumerate(options, start=1):
        lg.print_like_human(lg.COLORS['yellow'] + f"{idx}. {entry}")
    choice = lg.input_like_human(lg.COLORS['blue'] + 'Choose a option by number. You can leave a mode by typing "exit". \nOption: ')
    try:
        selectedOption = int(choice)
    except ValueError:
        lg.print_like_human("Please enter a valid number.")
        continue

    if selectedOption < 1 or selectedOption > len(options):
        print("Invalid option. Please try again.")
        continue

    if selectedOption == 1:
        llm = initialize_llm()
        question_asker_logic(llm)
    elif selectedOption == 2:
        llm = initialize_llm()
        file_analyser_logic(llm)
    elif selectedOption == 3:
        trainer_logic()
    elif selectedOption == 4:
        break