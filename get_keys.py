import google.generativeai as palm
from dotenv import load_dotenv, find_dotenv

from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain import PromptTemplate, LLMChain

import json

def get_interval(i1, i2):
    load_dotenv(find_dotenv())

    llm = GooglePalm(temperature=0)

    template = """
    Instrument 1 is flute and instrument 2 is clarinet, your response is:
    {{"key_1": "C", "key_2": "Bb"}}

    Instrument 1 is tenor saxophone and instrument 2 is french horn, your response is:
    {{"key_1": "Bb", "key_2": "F"}}

    Instrument 1 is flute and instrument 2 is violin, your response is:
    {{"key_1": "C", "key_2": "C"}}

    Instrument 1 is {instrument_1} and instrument 2 is {instrument_2} your response is:
    <your_response>

    """

    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    res = llm_chain.run({'instrument_1': i1, 'instrument_2': i2})
    keys = json.loads(res)
    return key_difference(keys['key_1'], keys['key_2'])


key_half_steps = {
    'C': 0,
    'D': 2,
    'Eb': -9,
    'F': -7,
    'G': -5,
    'A': -3,
    'Bb': -2,
}

def key_difference(key_1: str, key_2: str) -> int:
    if key_1 not in key_half_steps or key_2 not in key_half_steps:
        raise ValueError("Invalid key inputs")
    diff = key_half_steps[key_2] - key_half_steps[key_1]
    return diff



#print(get_keys("flute", "clarinet"))