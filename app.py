import streamlit as st

from agents.search_agent import run_search
from agents.ranking_agent import rank
from agents.completeness_agent import check_completeness

st.set_page_config(page_title="BOM Intelligence Pro")

st.title("⚙️ BOM Intelligence System")

# -------------------------------
# BOM CHECK
# -------------------------------
st.header("1. BOM Completeness Check")

user_input = st.text_input("Enter components (comma separated)", 
                          placeholder="SoC, Battery, Display")

if st.button("Analyze BOM"):
    if user_input:
        user_components = [x.strip() for x in user_input.split(",")]

        missing, deps = check_completeness(user_components)

        st.subheader("🧩 Missing Components")
        st.write(missing if missing else "None")

        st.subheader("⚠️ Dependency Issues")
        st.write(deps if deps else "None")
    else:
        st.warning("Enter components first")

# -------------------------------
# COMPONENT SEARCH
# -------------------------------
st.header("2. Component Search")

query = st.text_input("Search component", 
                      placeholder="e.g. 60W charging IC")

if st.button("Find Parts"):
    if not query:
        st.warning("Enter search query")
    else:
        with st.spinner("Fetching components..."):
            parts = run_search(query)

        if not parts:
            st.error("No parts found")
        else:
            st.subheader("📦 Raw Parts")
            st.json(parts)

            with st.spinner("Analyzing..."):
                analysis = rank(query, parts)

            st.subheader("🧠 AI Recommendation")
            st.write(analysis)
