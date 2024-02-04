from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_rapper_name(rapper, name, food_type, adjective, hobby):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['rapper', 'name', 'food_type' 'adjective', 'hobby'],
        template="I need to come up with a two-word rapper name based on the following traits. My favorite rapper is {rapper}. My first name is {name}. I like {food_type} food.\
              I'm often described as {adjective} and and my favorite hobby is {hobby}. What should my rapper name be? Provide only one name."
    )


    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='rapper_name')
    response = name_chain({'rapper': rapper, 'name': name, 'food_type': food_type, 'adjective': adjective, 'hobby': hobby})
    return response 

if __name__ == '__main__':
    args_list = ['tyler the creator', 'aiden', 'salty', 'kind','bodybuilding']
#    print(generate_rapper_name(*args_list))