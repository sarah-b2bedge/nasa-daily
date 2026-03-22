import streamlit as st
import requests

api_key = "hqGbT3TOzsGWXeYmS7znqVfsYXz9gzH79ifcgqtk"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

st.title("Galaxy by the lake")
st.video(content["url"])
st.text(content["explanation"])
