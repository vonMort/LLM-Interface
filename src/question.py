import src.logger as lg
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


template = """Question: {question}

Answer:"""


def question_asker_logic(llm):
    while True:
        question = input(lg.COLORS['blue'] + '\nAsk a question: ' + lg.COLORS['yellow'])
        if question.lower() == 'exit':
            break
        prompt = PromptTemplate(template=template, input_variables=["question"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        llm_chain.invoke(question)