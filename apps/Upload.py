import streamlit as st
import shelve
import time
import os
from lighthouseweb3 import Lighthouse
#set api_key from env variable LH_TOKEN
api_key = os.environ['LH_TOKEN']

lh = Lighthouse(token="os.environ'LH_TOKEN')")
def app():
    st.write("# Upload Your own Music!")
    if "address" in st.session_state:
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
                # time.sleep(2)
                try:
                    response = lh.deploy(cover)
                except:
                    response=""
                shelvedb = shelve.open("data.db")
                shelvedb[str(len(shelvedb)+1)] = {"author": author, "title": title,
                                            "release_date": release_date, "cover": cover, "music": music, "response": response}
                st.success("Done!")
                shelvedb.close()
                # TODO upload to lighthouse

    else:
        st.write("Please connect to a wallet to upload your own music!")
