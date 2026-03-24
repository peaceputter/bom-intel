import streamlit as st

from agents.search_agent import run_search
from agents.ranking_agent import rank
from agents.completeness_agent import check_completeness
from agents.spec_agent import extract_specs

st.set_page_config(page_title="BOM Intelligence Pro")

st.title("⚙️ BOM Intelligence System")

# -------------------------------
# BOM CHECK
# -------------------------------
st.header("1. BOM Completeness Check")

user_input = st.text_input(
    "Enter components (comma separated)",
    placeholder="SoC, Battery, Display"
)

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

query = st.text_input(
    "Search component",
    placeholder="e.g. 60W charging IC"
)

if st.button("Find Parts"):
    if not query:
        st.warning("Enter search query")
    else:
        # Step 1: Search (with query rewrite)
        with st.spinner("🔍 Understanding query..."):
            parts, improved_query = run_search(query)

        # Show rewritten query
        st.subheader("🔍 Improved Query")
        st.write(improved_query)

        # Step 2: Extract specs
        with st.spinner("📊 Extracting specs..."):
            specs = extract_specs(query)

        st.subheader("📊 Extracted Specs")
        st.write(specs)

        # Step 3: Show raw parts
        if not parts:
            st.error("No parts found")
        else:
            st.subheader("📦 Raw Parts")
            st.json(parts)

            # Step 4: AI ranking
            with st.spinner("🧠 Analyzing best options..."):
                analysis = rank(improved_query, parts)

            st.subheader("🧠 AI Recommendation")
            st.write(analysis)
