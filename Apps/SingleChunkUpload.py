import requests
import base64
import sys
import string
import os
import json
import schedule
import time
import streamlit as st

# Replace with your file metadata


def SingleChunkUpload(username, password,wGuid,mGuid,id, name,chunkCount,delimiter,encoding,firstDataRow,format,headerRow,separator):
    user = 'Basic ' + str(base64.b64encode((f'{username}:{password}'
                                            ).encode('utf-8')).decode('utf-8'))
    url = (f'https://api.anaplan.com/1/3/workspaces/{wGuid}/models/{mGuid}/' +
       f'files/{fileData["id"]}')

    putHeaders = {
        'Authorization': user,
        'Content-Type': 'application/octet-stream'}

# Opens the data file (filData['name'] by default) and encodes it to utf-8
    dataFile = open(fileData['name'], 'r').read().encode('utf-8')

    fileUpload = requests.put(url,
                          headers=putHeaders,
                          data=(dataFile))
    if fileUpload.ok:
        print('File Upload Successful.')
    else:
        print('There was an issue with your file upload: '
          + str(fileUpload.status_code))



def main():
    st.title('Get Import IDs :open_file_folder:')
    username = st.text_input("Enter username: ")
    password = st.text_input("Enter password: ",type="password")
    wGuid = st.text_input("Enter Workspace ID: ")
    mGuid = st.text_input("Enter Model ID: ")
    id= st.text_input("Enter File ID: ")
    name= st.text_input("Enter File Name: ")
    chunkCount= st.text_input("Enter ChunkCount: ")
    delimiter= st.text_input("Enter delimiter: ")
    encoding= st.text_input("Enter encoding: ")
    firstDataRow= st.text_input("Enter firstDataRow: ")
    format= st.text_input("Enter format: ")
    headerRow= st.text_input("headerRow: ")
    separator= st.text_input("separator: ")
    timer = st.text_input("Time interval in days: ")
    time = st.text_input("Upload Time: ")


    # schedule.every(7).day.do(SingleChunkUpload)
    # schedule.every(5).day.at("11:11").do(SingleChunkUpload)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    if st.button("Upload"):
        if username and password and timer:
           # Actions = SingleChunkUpload(username, password,wGuid,mGuid,id, name,chunkCount,delimiter,encoding,firstDataRow,firstDataRow,format,headerRow,separator)
           schedule.every(5).day.at("11:11").do(SingleChunkUpload)
           while True:
              schedule.run_pending()
              time.sleep(1)
        else:
           st.write("Failed to upload.")



if __name__ == '__main__':
    main()