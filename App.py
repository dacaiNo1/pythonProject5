import streamlit as st
from Multiapp import MultiApp
from Apps import Get_Action_ID,Get_Export_ID,Get_Import_ID, Get_Process_ID, Get_Files, Run_Import, SingleChunkUpload


app = MultiApp()

st.markdown(""" 
# Hannah's Anaplan Tool (Version 1.0)
### - May or may not be useful 
""")

app.add_app("Get Action ID", Get_Action_ID.main)
app.add_app("Get Process ID", Get_Process_ID.main)
app.add_app("Get Import ID", Get_Import_ID.main)
app.add_app("Get Export ID", Get_Export_ID.main)
app.add_app("Get Files", Get_Files.main)
# app.add_app("Single Chunk Upload",SingleChunkUpload.main)
# app.add_app("Run Import",Run_Import)

app.run()