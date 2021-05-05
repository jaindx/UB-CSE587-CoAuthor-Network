import streamlit as st
import pandas as pd
import base64

st.title('CO-AUTHORS NETWORK EXPLORER')

st.markdown("""
This app allows you to explore the network of co-authors of research papers in business journals and the number of papers for which they have collaborated!
* **Data source:** [JSTOR](https://jstor.org).
""")

df = pd.read_csv('output.txt', delimiter = "\t")

st.sidebar.header('List of first authors')
author = st.sidebar.selectbox('', df)

def load_coauthors(author):
    coauthors = df.query('AUTHOR == "%s"' % author)
    return coauthors['COAUTHORS']
coauthors = load_coauthors(author)

#Format the data
str_coauthors = coauthors.values[0].replace('{','').replace('}', '').replace("'",'').strip()


st.header('Co-Authors of Selected Author')
st.markdown("<font color=‘blue’>%s</font>" % str_coauthors.replace(',','</br>'), unsafe_allow_html=True)

def filedownload(coauthors):
    csv = coauthors.to_csv(index=False)
    b64 = base64.b64encode(coauthors.values[0].replace("'",'"').encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/json;base64,{b64}" download="coauthors.json">Download as JSON File</a>'
    return href

st.markdown(filedownload(coauthors), unsafe_allow_html=True)