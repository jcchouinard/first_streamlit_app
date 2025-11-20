import streamlit as st

st.set_page_config(
    page_title="JC Chouinard Professional Portfolio",
    page_icon="👤",
    layout="wide"
)

NAME = "Jean-Christophe Chouinard"
TITLE = "Senior SEO Strategist PM @ Tripadvisor | Certified Data Scientist"
SOCIAL_MEDIA = {
    'jcchouinard.com': 'https://www.jcchouinard.com/',
    'YouTube': 'https://www.youtube.com/@jcchouinard',
    'X': 'https://x.com/ChouinardJC',
    'LinkedIn': 'https://www.linkedin.com/in/jeanchristophechouinard',
    'GitHub': 'https://github.com/jcchouinard',
    'Datacamp':'https://www.datacamp.com/portfolio/jcchouinard'
}
PROFILE_PIC = 'https://www.jcchouinard.com/wp-content/uploads/2019/02/t%C3%A9l%C3%A9chargement.png'

col1, col2 = st.columns([1, 4])

with col1:
    st.image(PROFILE_PIC, width=150)

with col2:
    st.header(NAME)
    st.title(TITLE)


st.sidebar.title('About JC Chouinard')
for platform, link in SOCIAL_MEDIA.items():
    st.sidebar.markdown(f"[{platform}]({link})")
st.markdown('## About Me')

st.markdown(
    """
    JC Chouinard is a senior SEO Strategist at Tripadvisor, previously SEEK. He is focused on AI search and AI Product Management. He helps the SEO community learn Python and Machine Learning on his blog at [jcchouinard.com](https://www.jcchouinard.com). Build as a [streamlit example](https://jcchouinard-first-streamlit-app-app-i07a2j.streamlit.app/)
    """
)
st.write("")

st.markdown('## Guest Contributions & Speaking')

st.markdown(
    """
    * [Public Speaker at SEOIRL 2025](https://seoirl.com/)
    * [Search Engine Journal](https://www.searchenginejournal.com/author/jc-chouinard/)
    * [Search Engine Land](https://searchengineland.com/author/jean-christophe-chouinard)
    * [OnCrawl](https://www.oncrawl.com/author/jc-chouinard/)
    * [Melbourne SEO Meetup (Video)](https://www.youtube.com/watch?v=HB-KD0ATsGg)
    * [Ranksense RSTwittorials (Video)](https://www.youtube.com/watch?v=H67-bBahsaE)
    * [Crawling Mondays (Video)](https://www.youtube.com/watch?v=2RSeVoDIKiM)
    """
)

st.markdown('## Technical Skills')

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.subheader("Languages & Databases")
    st.markdown("""
    - **Languages:** Python, SQL, JavaScript (Node.js), R, Perl
    - **Databases:** Snowflake, PostgreSQL, MySQL, Sqlite, BigQuery
    - **Tools:** Github, Gitlab, Kubeflow, Jupyter
    - **Other:** CI/CD
    """)

with skill_col2:
    st.subheader("Data Science & AI")
    st.markdown("""
    - **Machine Learning & AI:** NLP, Causal Inference, Time series (prophet), Scikit-learn, Cursor AI
    - **Generative AI:** Gemini API, ChatGPT API
    - **Core Skills:** Feature engineering, Product management
    """)

with skill_col3:
    st.subheader("Web & DevOps")
    st.markdown("""
    - **Web Scraping:** Python, Xpath, Proxy rotation, APIs, Browser Automation
    - **SEO:** Experimentation, Log-file analysis, Indexing, Keyword ranking
    - **Cloud:** Google Cloud Platform (GCP)
    - **Tools:** SEMRush, Ahrefs, Splunk, Google Analytics, GTM, Screaming Frog
    """)

st.markdown('## Portfolio Projects')

with st.container(border=True):
    st.markdown("### 1. Google Search Console API Tutorial/Tool")
    st.markdown("**Technologies:** Python, Google Search Console API, Data Processing")
    st.write(
        """
        Comprehensive guide and code repository demonstrating how to effectively extract, process, and analyze SEO data
        using the Google Search Console API with Python. This project focuses on automating reporting and deep log-file analysis.
        """
    )
    st.markdown("[View on GitHub](https://github.com/jcchouinard/GoogleSearchConsole-Tutorial)")

with st.container(border=True):
    st.markdown("### 2. Reddit API Data Ingestion and Analysis")
    st.markdown("**Technologies:** Python, Reddit API (PRAW), Web Scraping, NLP/Text Analysis")
    st.write(
        """
        Detailed resource on connecting to the Reddit API for large-scale data ingestion. The project covers advanced web scraping techniques,
        data structuring, and utilizing text analysis methods like NLP to derive insights from community discussions.
        """
    )
    st.markdown("[View on Website](https://www.jcchouinard.com/reddit-api/)")



