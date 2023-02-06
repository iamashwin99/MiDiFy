import streamlit as st
import shelve
import time


def app():
    st.write("# Upload Your own Music!")
    st.write(
        "Upload your own music to the MiDiFy platform and start earning money from your music!")
    music = st.file_uploader("Upload your music here", type=["mid"])
    author = st.text_input("Author Name")
    title = st.text_input("Title")
    release_date = st.date_input("Release Date")
    st.write("## Upload your cover art")
    cover = st.file_uploader("Upload your cover art here", type=[
                             "png", "jpg", "jpeg"])
    upload = st.button("Upload")
    if upload:
        with st.spinner("Uploading data ..."):
            time.sleep(2)
            shelvedb = shelve.open("data.db")
            shelvedb[len(shelvedb)+1] = {"author": author, "title": title,
                                         "release_date": release_date, "cover": cover, "music": music}
            st.success("Done!")
