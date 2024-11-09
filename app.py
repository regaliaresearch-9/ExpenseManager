import  setup_db
setup_db.create_expenses_table()

import json
import os
import pandas as pd
import requests
from datetime import datetime, timedelta, date
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader




st.set_page_config(page_title="Dashboard!!!", page_icon=":bar_chart:",layout="wide")
st.markdown('<style>div.block-container{padding-top:5rem;}</style>',unsafe_allow_html=True)


credentials = {
    st.secrets["username"]: {
        'admin': {
            'email': 'jsmith@gmail.com',
            'failed_login_attempts': 0,  # Will be managed automatically
            'logged_in': False,           # Will be managed automatically
            'name': 'Admin',
            'password':  st.secrets["pass"],            # Will be hashed automatically
            'roles': ['admin', 'editor', 'viewer']
        }
    }
}




# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days']
# )


authenticator = stauth.Authenticate(
    credentials,
    "Dashboard",
    "keyss",
    cookie_expiry_days=30
)

authenticator.login()

if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')



