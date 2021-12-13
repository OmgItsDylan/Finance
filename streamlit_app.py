import streamlit as st 

st.set_page_config(page_title="Finance platform", page_icon="https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png", layout='centered', initial_sidebar_state="collapsed")

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Finance Platform </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("demo")

    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
