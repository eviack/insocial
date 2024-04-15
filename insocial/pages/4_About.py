import streamlit as st
from streamlit_extras.let_it_rain import rain


st.title('About')
hide_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_style, unsafe_allow_html=True) 

st.markdown('''
            This project was created for **Bennett University Internal SIH Hackathon 2023**.

            **Team Members:** 
            
            [Sukant Aryan](https://www.linkedin.com/in/sukantaryan)\n
            [Samaksh Tyagi](https://www.linkedin.com/in/samakshtyagi)\n
            ''')

rain(
  emoji='✨',
  font_size=54,
  falling_speed=10,
  animation_length=50
)
