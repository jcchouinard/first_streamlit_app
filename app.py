import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="JC Chouinard | Professional Portfolio",
    page_icon="👤",
    layout="wide"
)

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
    }
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    h1 { font-size: 3.5rem !important; }
    h2 { font-size: 2.8rem !important; }
    h3 { font-size: 2.2rem !important; }
    h4 { font-size: 1.8rem !important; }
    .hero-section {
        background-color: #161b22;
        padding: 4rem;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 2rem;
        text-align: center;
    }
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 48px !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 24px !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 70px;
        font-size: 22px !important;
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px 8px 0px 0px;
        color: #8b949e;
        padding: 0 25px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #21262d;
        border-color: #f0f6fc;
        color: #ffffff;
    }
    .content-card {
        background-color: #161b22;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #30363d;
        margin-bottom: 1rem;
    }
    .sidebar-link {
        text-decoration: none;
        color: #58a6ff;
        display: block;
        padding: 8px 0;
        font-size: 1.2rem;
    }
    .testimonial-quote {
        padding: 25px;
        margin: 15px 0;
        border-left: 5px solid #58a6ff;
        background-color: #161b22;
        line-height: 1.6;
        border-radius: 0 8px 8px 0;
    }
    .quote-text {
        font-style: italic;
        font-size: 1.3rem;
        margin-bottom: 10px;
        display: block;
    }
    .quote-author {
        color: #58a6ff;
        font-weight: bold;
        font-size: 1.1rem;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

course_list = [
    ["Hugging Face's Agents Course", "https://huggingface.co/learn/agents-course/unit0/introduction", "Hugging Face", "In Progress"],
    ["Generative AI for Business", "https://www.datacamp.com/completed/statement-of-accomplishment/course/83b189fbacc233ddf0cd8a4e7f9ada1dac6e57dd", "Datacamp", "Completed"],
    ["Building Scalable Agentic Systems", "https://www.datacamp.com/completed/statement-of-accomplishment/course/28615411ee5e63ec7067456ac2ddc45ef06b13a7", "Datacamp", "Completed"],
    ["Introduction to AI Agents", "https://www.datacamp.com/completed/statement-of-accomplishment/course/794f9e895ff00d82a715c386b7e7edf77fc98728", "Datacamp", "Completed"],
    ["Introduction to Kubernetes", "https://www.datacamp.com/completed/statement-of-accomplishment/course/06c59579516074cdbdca5faad1b71f339957a774", "Datacamp", "Completed"],
    ["Introduction to Docker", "https://www.datacamp.com/completed/statement-of-accomplishment/course/fdb983195d98452a9f5a6807da742767c8b50207", "Datacamp", "Completed"],
    ["Containerization and Virtualization Concepts", "https://www.datacamp.com/completed/statement-of-accomplishment/course/35be12e6a43f57c43e337fbf7125db1791684e88", "Datacamp", "Completed"],
    ["Hyperparameter Tuning in Python", "https://www.datacamp.com/completed/statement-of-accomplishment/course/34096144fa15f7b6b2994b1ca67f2c2d3e3087ae", "Datacamp", "Completed"],
    ["Model Validation in Python", "https://www.datacamp.com/completed/statement-of-accomplishment/course/e061570b4ea4e7a50b91800320a7267c8b50a67f", "Datacamp", "Completed"],
    ["Feature Engineering for Machine Learning in Python", "https://www.datacamp.com/completed/statement-of-accomplishment/course/f85fdab4adfc0b413e133aeacdd147b8627d3b3c", "Datacamp", "Completed"],
    ["Machine Learning for Time Series Data in Python", "https://www.datacamp.com/completed/statement-of-accomplishment/course/da40ee1034011733498528200c635df05fa0eb56", "Datacamp", "Completed"],
    ["Dimensionality Reduction in Python", "https://www.datacamp.com/completed/statement-of-accomplishment/course/06807d97175e5b484d508a9c8dea4293a743d51d", "Datacamp", "Completed"],
    ["Extreme Gradient Boosting with XGBoost", "https://www.datacamp.com/completed/statement-of-accomplishment/course/2d9151bc063e9de5d5a08b560b88b035f00d69be", "Datacamp", "Completed"],
    ["Supervised Learning with scikit-learn", "https://www.datacamp.com/completed/statement-of-accomplishment/course/18a9aa6234c96e135944434706ab7289dad70365", "Datacamp", "Completed"],
    ["Foundations of Git", "https://www.datacamp.com/completed/statement-of-accomplishment/course/d9d04d704ba36cc629afbc78ae235b643212087f", "Datacamp", "Completed"],
    ["Joining Data in SQL", "https://www.datacamp.com/completed/statement-of-accomplishment/course/98f01896a396ec60ca404008a6e79438b948b9cd", "Datacamp", "Completed"],
    ["Intermediate SQL", "https://www.datacamp.com/completed/statement-of-accomplishment/course/45bd98fc8861901ad99c3c4c51389c56e5a06a22", "Datacamp", "Completed"],
    ["Introduction to SQL", "https://www.datacamp.com/completed/statement-of-accomplishment/course/6376543f0f06b4cf028281e47e76fc2b50ce71d4", "Datacamp", "Completed"]
]

df_courses_full = pd.DataFrame(course_list, columns=["Course Name", "Url", "Source", "Status"])
df_completed = df_courses_full[df_courses_full["Status"] == "Completed"]
df_in_progress = df_courses_full[df_courses_full["Status"] == "In Progress"]

profile_quotes = [
    "Consistently ahead of industry changes; often flags issues before leadership asks.",
    "Exceptional technical depth with a strong experimentation mindset.",
    "Turns ambiguous problems into concrete systems and measurable outcomes."
]

all_testimonials = [
    {"q": "Recognized as a key company reference on AI innovation", "a": "Manager Summary, Tripadvisor"},
    {"q": "One of the best data-driven SEOs in the industry... getting to hire and work with one of the best has been a great privilege.", "a": "Mike Hudson, previous Manager @SEEK"},
    {"q": "He solidified his reputation as a brilliant and irrepressible SEO who is laser-focused on opportunity.", "a": "Manager Summary, Tripadvisor"},
    {"q": "Jean-Christophe is an outstanding SEO... and is also an absolute wizard with the Python programming language!", "a": "Charly Wargnier, Python Dev - SEO & BI Consultant"},
    {"q": "He knows how to use data science, artificial intelligence... I have learned using Google Search Console with Python from him.", "a": "Koray Tuğberk GÜBÜR, Holistic SEO"},
    {"q": "Understanding of the subject is deep, and the SEO expertise he brings unparalleled.", "a": "Dushyant Sharma, Agentic AI @ Atlassian (previous Collaborator @SEEK)"},
    {"q": "Jean-Christophe is a top tier SEO professional who is not only a master of his technical craft but possesses the ability to think strategically.", "a": "Bo Jing, previous Manager @SEEK"},
    {"q": "Jean Christophe is one of the biggest Python for SEO expert... provides the highest level of SEO services at a fraction of the time.", "a": "Orit Mutznik, Head of Organic Channels, Farfetch"},
    {"q": "JC's use of python to automate and process SEO data has made my work-life a lot less tedious.", "a": "Mike Hudson,  previous Manager @SEEK"},
    {"q": "He is the only team member who regularly reads Google Search filed patents to gain deeper insights.", "a": "Manager Summary, Tripadvisor"},
    {"q": "JC is a massive culture add to the team who brings uplifting, positive energy and encouragement.", "a": "Peer Review, Tripadvisor"},
    {"q": "JC is highly technically proficient. He’s able to think about the minutia of SEO and how Google works.", "a": "Peer Review, Tripadvisor"},
    {"q": "Jean-Christophe is a highly knowledgeable SEO expert that doesn't hesitate to share what he knows.", "a": "Zach Todd, SEO Specialist"},
    {"q": "Reliable and eager to help... having a wealth of technical SEO knowledge to share.", "a": "Peer Review, Tripadvisor"}
]

with st.sidebar:
    st.image('https://www.jcchouinard.com/wp-content/uploads/2019/02/t%C3%A9l%C3%A9chargement.png', width=150)
    st.markdown("### Contact & Social")
    st.markdown('<a href="https://www.jcchouinard.com/" class="sidebar-link">jcchouinard.com</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/jeanchristophechouinard" class="sidebar-link">LinkedIn</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/jcchouinard" class="sidebar-link">GitHub</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.youtube.com/@jcchouinard" class="sidebar-link">@jcchouinard on YouTube</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://x.com/ChouinardJC" class="sidebar-link">X @ChouinardJC</a>', unsafe_allow_html=True)
    st.write("---")
    st.write("Senior SEO Strategist PM")
    st.write("Tripadvisor")

st.markdown("""
    <div class="hero-section">
        <h1 style='color: #f0f6fc; margin-bottom: 0;'>Jean-Christophe Chouinard</h1>
        <p style='font-size: 1.8rem; color: #8b949e;'>Senior SEO Strategist PM @ Tripadvisor | Certified Data Scientist</p>
    </div>
    """, unsafe_allow_html=True)

tab_about, tab_skills, tab_edu, tab_portfolio, tab_testi = st.tabs([
    "Profile", "Expertise", "Education", "Portfolio", "Testimonials"
])

with tab_about:
    col_a1, col_a2 = st.columns([2, 1])
    with col_a1:
        st.markdown("### About Me")
        st.write("JC Chouinard is a senior SEO Strategist at Tripadvisor focusing on AI search and Product Management.")
        st.markdown("---")
        st.markdown("### Guest Contributions")
        st.markdown("""
            * [Public Speaker at SEOIRL 2025](https://seoirl.com/)
            * [Search Engine Journal Author](https://www.searchenginejournal.com/author/jc-chouinard/)
            * [Search Engine Land Author](https://searchengineland.com/author/jean-christophe-chouinard)
            * [OnCrawl Author](https://www.oncrawl.com/author/jc-chouinard/)
            * [Melbourne SEO Meetup (Video)](https://www.youtube.com/watch?v=HB-KD0ATsGg)
            * [Ranksense RSTwittorials (Video)](https://www.youtube.com/watch?v=H67-bBahsaE)
            * [Crawling Mondays (Video)](https://www.youtube.com/watch?v=2RSeVoDIKiM)
            """)
    with col_a2:
        st.metric("Experience", "12+ Years")
        st.metric("Employer", "Tripadvisor")
        st.markdown("""
        **Past Employers**
        - Seek.com.au
        - jobillico.com
        """)

        st.info("Focused on AI Search and Agentic Systems.")

with tab_skills:
    st.markdown('## Skills')
    sk1, sk2, sk3 = st.columns(3)
    with sk1:
        st.markdown("**Languages & Databases**")
        st.write("Python, SQL, JavaScript (Node.js), R, Perl, Snowflake, PostgreSQL, MySQL, Sqlite, BigQuery, GitHub, Gitlab, Kubeflow, Jupyter, CI/CD.")
        
    with sk2:
        st.markdown("**Data Science & AI**")
        st.write("NLP, Causal Inference, Time series (prophet), Scikit-learn, Cursor AI, Gemini API, ChatGPT API, Feature engineering, Product management.")
        
    with sk3:
        st.markdown("**Web & DevOps**")
        st.write("Web Scraping, Xpath, Proxy rotation, APIs, Browser Automation, SEO Experimentation, Log-file analysis, Indexing, Keyword ranking, GCP, SEMRush, Ahrefs, Splunk, Google Analytics, GTM, Screaming Frog.")

    st.markdown("---")
    st.markdown("### Common Blog & Learning Topics")
    def render_chart(file_name, key, title):
        try:
            df = pd.read_csv(file_name)
            df['Topic'] = df['Topic'].replace('datum', 'data')
            row_count = st.slider(f"{title}:", 1, len(df), 10, key=key)
            df_plot = df.sort_values(by="Count", ascending=False).head(row_count).sort_values(by="Count", ascending=True)
            fig = px.bar(df_plot, x="Count", y="Topic", orientation='h', template="plotly_dark", color_discrete_sequence=['#58a6ff'], text="Count")
            fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=30, b=0), height=max(400, row_count * 45), font=dict(size=18))
            st.plotly_chart(fig, use_container_width=True)
        except: st.warning(f"Data file for {title} missing.")
    
    render_chart("processed_topics.csv", "blog_slide", "Blog Topics")
    st.markdown("---")
    render_chart("courses_topics.csv", "course_slide", "Learning Topics (spaCy)")

with tab_edu:
    st.markdown("#### Professional Certifications")
    st.write("Data Scientist Professional Certification | [Full Profile](https://www.datacamp.com/portfolio/jcchouinard)")
    st.write("---")
    st.markdown("#### Academic Degree")
    st.write("Bachelor of Business Administration | Université de Sherbrooke | 2012")
    st.write("---")
    st.markdown("#### In Progress")
    st.dataframe(df_in_progress, column_config={"Url": st.column_config.LinkColumn("Course Link")}, hide_index=True, use_container_width=True)
    st.write("---")
    st.markdown("#### Completed Courses")
    st.dataframe(df_completed, column_config={"Url": st.column_config.LinkColumn("Certificate")}, hide_index=True, use_container_width=True)

with tab_portfolio:
    st.markdown("### Featured Systems")
    p1, p2 = st.columns(2)
    with p1:
        st.markdown("""<div class="content-card"><h4>1. GSC API Tool</h4><p>Python automation for deep log-file and SEO data analysis.</p><a href="https://github.com/jcchouinard/GoogleSearchConsole-Tutorial">View Repository</a></div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class="content-card"><h4>2. Reddit API Ingestion</h4><p>Scalable NLP analysis system for community discussions.</p><a href="https://www.jcchouinard.com/reddit-api/">View Case Study</a></div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Blog Posts by Topic")
    try:
        df_urls = pd.read_csv("top_urls_by_topic.csv")
        sel_topic = st.selectbox("Explore related blog posts:", sorted(df_urls['topic'].unique()))
        for url in df_urls[df_urls['topic'] == sel_topic]['url']:
            st.markdown(f"- [{url}]({url})")
    except: st.warning("Topic data missing.")

with tab_testi:
    st.markdown("### Industry Recognition & Peer Feedback")
    for t in all_testimonials:
        st.markdown(f'''
            <div class="testimonial-quote">
                <span class="quote-text">"{t['q']}"</span>
                <span class="quote-author">— {t['a']}</span>
            </div>
        ''', unsafe_allow_html=True)

st.write("---")
st.markdown("<center><small>Built with Streamlit by JC Chouinard | 2025</small></center>", unsafe_allow_html=True)