import requests
import base64
import streamlit as st
import pandas as pd


def get_ChunkData_ids(username, password,wGuid,mGuid):
    user = 'Basic ' + str(base64.b64encode((f'{username}:{password}'
                                            ).encode('utf-8')).decode('utf-8'))
    headers = {'Authorization': user}
    url = 'https://api.anaplan.com/1/3/workspaces/' +
                            f'{wGuid}/models/{mGuid}/files/{fileID}' +
                            '/chunks'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data)
        df.astype(str)
        st.dataframe(df)
        st.download_button("Download as CSV", df.to_csv(),file_name='Chunk Data.csv', mime = 'text/csv')
    else:
        return None



def main():
    st.title('Get Export IDs ^_^')
    username = st.text_input("Enter username: ")
    password = st.text_input("Enter password: ",type="password")
    wGuid = st.text_input("Enter Workspace ID: ")
    mGuid = st.text_input("Enter Model ID: ")
    if st.button("Send"):
        if username and password:
           Actions = get_ChunkData_ids(username, password,wGuid,mGuid)
        else:
           st.write("Failed to retrieve workspaces.")



if __name__ == '__main__':
    main()