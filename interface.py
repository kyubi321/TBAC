import streamlit as st
import csv

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("styles.css")
def authenticate(username,password):
    with open('files/sec_pract_mod.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == username and row[2] == password:
                return True
    return False

def main():

    st.markdown("<div class='center'>", unsafe_allow_html=True)
    #st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.markdown("<h1 class='login-title'>LOGIN</h1>",unsafe_allow_html=True)


    username = st.text_input("Username")
    password = st.text_input("password", type="password")

    if st.button("Login"):
        if authenticate(username,password):
            st.success("Login Successful!")
        else:
            st.error("Invalid username or password")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()