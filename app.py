import streamlit as st
import yaml
from yaml.loader import SafeLoader
from pathlib import Path

# --- Load Personal Details ---
with open("details.yaml") as f:
    details = yaml.load(f, Loader=SafeLoader)

st.set_page_config(
    page_title=f"{details['name']} | Portfolio",
    page_icon="💼",
    layout="wide",
)

# --- Apply CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header ---
st.title(details["name"])
st.markdown(f"### {details['title']}")
st.markdown(details["bio"])

# --- Contact Links ---
st.markdown(
    f"""
    📧 [Email]({details['email']}) | 
    💼 [LinkedIn]({details['linkedin']}) | 
    🐙 [GitHub]({details['github']}) | 
    💬 [WhatsApp]({details['whatsapp']})
    """
)

st.markdown("---")
st.markdown("## 🚀 Featured Projects")
for proj in details["projects"]:
    st.subheader(proj["name"])
    st.write(proj["description"])
    st.caption(f"**Tools:** {proj['tools']}")

st.markdown("---")
st.markdown("## 🧠 Skills")
st.write(", ".join(details["skills"]))
