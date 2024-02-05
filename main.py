import langchain_helper as lch 
import streamlit as st

st.title("Rapper Name Generator")


#rapper, name, food type, adjective, hobby
name = st.sidebar.text_area(label="What is your first name", max_chars=20)
rapper = st.sidebar.text_area(label="Who is your favorite hip hop artist?", max_chars=20)
adjective = st.sidebar.text_area(label='What is an adjective that describes you?', max_chars=20)
hobby = st.sidebar.text_area(label='What do you do for fun?', max_chars=20)
food_type = st.sidebar.selectbox("How do you like your food?", ('Sweet', 'Salty', 'Spicy', 'Sour', 'Bitter', 'Umami'))

if st.sidebar.button('Generate name'):
    response = lch.generate_rapper_name(name=name, rapper=rapper, adjective=adjective, hobby=hobby, food_type=food_type)
    st.write(response['rapper_name'])
