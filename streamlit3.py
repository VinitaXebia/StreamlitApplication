import streamlit as st
import wikipediaapi
import time
# Streamlit UI
st.title("Wikipedia Answer Streamer")
# Language Selection Dropdown
language_mapping = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it"
}
selected_language = st.selectbox("Choose language:", list(language_mapping.keys()))
summary_length = st.selectbox("Choose summary length:", [100, 250, 500])
query = st.text_input("Enter your query:")
if st.button("Search"):
    if query:
        with st.spinner("Searching Wikipedia..."):
            wiki_wiki = wikipediaapi.Wikipedia(
                language=language_mapping[selected_language], 
                user_agent="WikipediaStreamer/1.0 (your-email@example.com)"
            )
            page = wiki_wiki.page(query)
            if page.exists():
                response_text = page.summary 
                words = response_text.split()[:summary_length]
                response_text = " ".join(words)                
                placeholder = st.empty()  
                streamed_text = ""
                for word in response_text.split():
                    streamed_text += word + " "
                    placeholder.write(streamed_text)
                    time.sleep(0.05)  
            else:
                st.error("No Wikipedia page found for this query.")