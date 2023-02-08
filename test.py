import requests
import base64
import streamlit as st
import pandas as pd

def get_workspace_ids(username, password):
    user = 'Basic ' + str(base64.b64encode((f'{username}:{password}'
                                            ).encode('utf-8')).decode('utf-8'))
    headers = {'Authorization': user}
    url = 'https://api.anaplan.com/1/3/workspaces'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data)
        print(df)
    else:
        return None

if __name__ == '__main__':
    # st.title('Get Workspace IDs ^_^')
    username = input("Enter username: ")
    password = input("Enter password: ")
    Workspaces = get_workspace_ids(username, password)