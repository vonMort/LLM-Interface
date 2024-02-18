import src.logger as lg
from src.question import question_asker_logic
from src.fileanalyser import file_analyser_logic
from langchain_community.llms import GPT4All
from langchain.callbacks import StreamingStdOutCallbackHandler

streaming_callback = StreamingStdOutCallbackHandler()


def initialize_llm():
    llm = GPT4All(
        model='.//model//wolfram.gguf',
        callbacks=[streaming_callback],
        n_threads=12,
        streaming=True,
        verbose=True)
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
        print("Not implemented")
        continue
    elif selectedOption == 4:
        break