import streamlit as st
from collections import Counter

st.title("📝 Text Analyzer")
st.write("Enter your text and analyze it.")

text = st.text_area("Enter your text:")

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        words = text.split()
        word_count = len(words)
        character_count = len(text)
        sentence_count = text.count(".") + text.count("!") + text.count("?")

        common_words = Counter(words).most_common(5)

        st.subheader("📊 Results")

        st.write("**Words:**", word_count)
        st.write("**Characters:**", character_count)
        st.write("**Sentences:**", sentence_count)

        st.subheader("🔥 Most Common Words")

        for word, count in common_words:
            st.write(word, "→", count)

        st.success("Analysis completed!")