import streamlit as st
import shelve
def app():
    if "address" in st.session_state:
        shelvedb = shelve.open("data.db")
        for key in shelvedb:
            st.write(f"## {shelvedb[key]['title']}")
            st.write(f"### {shelvedb[key]['author']}")
            st.write(f"### {shelvedb[key]['release_date']}")
            st.image(shelvedb[key]['cover'])
            st.audio(shelvedb[key]['music'])