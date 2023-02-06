import streamlit as st
from streamlit_option_menu import option_menu
from apps import Listen, Discover, Upload, About
from web3 import Web3


st.set_page_config(page_title="MiDiFy - Listen. Discover. Create", page_icon="🎼", layout="wide", initial_sidebar_state="expanded")


# # setup constants 
# connectedChains={
#     "Ethereum":1,
#     "Polygon":137,
#     "Avalanche":43114,
#     "Binance Smart Chain":56,
#     "Klaytn":8217
# }


# infura_url='https://mainnet.infura.io/v3/1a8b2eb3cfe6493695013d90eec174a4' #your uri
# w3 = Web3(Web3.HTTPProvider(infura_url))

apps = [
    {"func": Listen.app, "title": "Listen", "icon": "music"},
    {"func": Discover.app, "title": "Discover", "icon": "search"},
    {"func": Upload.app, "title": "Create", "icon": "upload"},
    {"func": About.app, "title": "About", "icon": "info-circle"},
    
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

# setup  states variables 
params = st.experimental_get_query_params()

# if "page" in params:
#     default_index = int(titles_lower.index(params["page"][0].lower()))
# else:
#     default_index = -1
# if "address" in params:
#     st.session_state["address"] = params["address"][0]
# else:
#     st.session_state["address"]="0xd0aD800d5799D114c2B165dA63D47708712B15e8"

# st.session_state["chains"] = connectedChains


# Fill in sidebar data
with st.sidebar:

    st.sidebar.title("About")
    st.sidebar.info(
        """
        MiDiFy is a  simple decentralised music streaming service built on top of the Lighthouse SDK.
    """
    )
