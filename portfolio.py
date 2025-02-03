import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.markdown("""
<style>
    .reportview-container .main .block-container{
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
    }
    h1 {
        color: #0066cc;
    }
    h2, h3, h4, h5, h6 {
        color: #212529;
    }
    .stButton>button {
        color: #f8f9fa;
        background-color: #0066cc;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004c99;
    }
</style>
""", unsafe_allow_html=True)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Carlos Lester M Covarrubias II, ECE
##### *Resume* 
''')

# Create three columns
col4, col5, col6 = st.columns([2.2,2,2])

# Load the image
image = Image.open('images/lester.jpg')

# Display the image in the middle column
with col5:
    st.image(image, width=150)
st.markdown('## Summary', unsafe_allow_html=True)

st.info('''
- Licensed Electronics Engineer with hands-on experience in AI/ML development. Won 1st Place in BPI DATA Wave 2024 Hackathon (ML Track). Completed intensive Eskwelabs’ Data Science Fellowship with five successful projects including NLP solutions, GenAI, and end-to-end ML applications.
- Effective communicator with a strong background in business partner collaboration at my current company and startup pitching from independent projects. Streamlined processes in company projects and successfully completed multiple collaborative projects during Eskwelabs' 15-week intensive bootcamp.
- Seeking Data Analyst/Scientist role to drive business value through data-driven solutions.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/carlos-lester-covarrubias-ii-ece-6b235112b/" target="_blank">Carlos Lester M Covarrubias II</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#data-science-portfolio">Data Science Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Science** (Electronics and Communications Engineering), *Ateneo de Zamboanga University*, Philippines',
'2012-2017')
st.markdown('''
''')

st.markdown('''
## Certications and Licenses
''')
txt('**Associate Data Analyst in SQL**, (DataCamp Career Track) *DataCamp*, Philippines',
'November 2024-February 2025')
st.markdown('''
''')

txt('**Neural Networks and Deep Learning**, (Coursera Certification) *Coursera*, Philippines',
'September 2024-September 2024')
st.markdown('''
''')

txt('**Data Science Fellowship Cohort 13** (Data Science Bootcamp), *Eskwelabs*, Philippines',
'May 2024-August 2024')
st.markdown('''
''')

txt('**Getting Grounded on Analytics** (Data Analytics), *Development Academy of the Philippines*, Philippines',
'2020')
st.markdown('''
''')

txt('**Licensed Electronics Engineer**, *Professional Regulation Commission*, Philippines',
'2017-Present')
st.markdown('''
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Field Services Engineer**, PLDT, Inc., Philippines',
'2019-Present')
st.markdown('''
- Efficiently managed and resolved troubleshooting tickets, addressing a wide range of technical issues.  
- Collaborated with business partners to coordinate tandem repair and installation efforts. Maintained clear and effective communication to streamline processes and ensure timely completion of projects.
- Conducted thorough inspections of business partners' work in both repair and installation tasks. Ensured adherence to industry standards and company protocols, consistently delivering high-quality service.
- chieved recognition as one of the top 5 employees in the region, reflecting dedication to excellence and outstanding performance in technical and customer service roles.
''')


txt('**Professional Services Engineer (Business Analyst)**, Juris Technologies Sdn Bhd., Malaysia',
'2022-2023')
st.markdown('''
- Worked as Contractor in a WFH Setup that uses Juris system framework to configure according to clients specifications by using PL/SQL and PhP Programming. 
- Proficient in banking processes and workflows, requirements gathering, and documentation.
- Experienced in User Acceptance Testing (UAT) and defect management. Competent in system analysis, test development, and execution.
''')

txt('**Software Engineer (Intern)**, FactSet , Philippines',
'2018')
st.markdown('''
- Designs implementation and deployment of large-scale and complex financial applications.
''')

txt('**Junior RF Engineer**, Globe Telecom',
'2017')
st.markdown('''
- Perform frequency and BCC planning Optimization and Enhancement of Wireless Telecommunications Networks
''')


#####################
st.markdown('''
## Data Science Portfolio
''')

# Function to convert image to base64
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Project details: paths and descriptions
projects = [
    {
        "title": "BPI: Bridging Potential and Investment Through Machine Learning",
        "image_path": "images/BPI.png",
        "description": ("This is our project that my team and I secured first place in the BPI DATA Wave Hackathon "
                        " with an innovative machine learning solution that revolutionizes loan assessment for MSMEs (Micro, Small, and Medium Enterprises). "
                        "This model incorporates non-traditional data points beyond standard financial metrics, enabling more comprehensive and equitable credit evaluation. "
                        "By aligning with the hackathon's mission of expanding financial inclusion, "
                        "our solution helps create fairer lending opportunities for small businesses that have "
                        "historically faced barriers in accessing traditional financing. "),
        "link": "https://msme-loan-prediction.streamlit.app/"
    },
    {
        "title": "Askwelabs: AI-Powered Chatbot and Study Path Recommendations",
        "image_path": "images/askwelabscover.png",
        "description": ("Askwelabs is an AI-driven platform offering a Q&A Chatbot that answers common questions "
                        "about Eskwelabs and analyzes resumes to recommend whether users should join a bootcamp or "
                        "pursue self-study. It also features a Study Path Recommendation System that creates "
                        "personalized learning plans based on user preferences in difficulty and focus area, "
                        "whether Data Analytics or Data Science. Built with ChromaDB, LangChain, and OpenAI’s GPT-3.5 Turbo, "
                        "Askwelabs delivers tailored educational guidance."),
        "link": "https://askwelabscapstoneproject.streamlit.app/"
    },
    {
        "title": "Course Recommender App",
        "image_path": "images/coursera_header.png",
        "description": ("Coursera Plus is a Course Recommender App that makes use of Coursera data to develop a "
                        "machine learning model that can assist you in deciding the perfect online learning course "
                        "fit to your needs. The project was built using the OpenAI API key for the LLM Embedding "
                        "and Retrieval-Augmented Generation (RAG) techniques."),
        "link": "https://courseraplus-cmcova.streamlit.app/"
    },
    {
        "title": "Reddit AITA Predictor",
        "image_path": "images/Intro_Objective.png",
        "description": ("Developed an innovative AI-driven system that analyzes complex social situations and provides ethical judgments with remarkable accuracy. This project showcases advanced machine learning techniques and demonstrates the ability to tackle real-world challenges using Natural Language Processing (NLP) and Large Language Models (LLMs). "
                        "Technical Highlights: "

"Utilized stratified k-fold cross-validation for robust model evaluation. "
"Implemented dynamic few-shot learning, adapting the KNN concept to enhance classification accuracy. "
"Optimized model parameters, particularly the 'n_examples' feature, to maximize performance"),
        "link": "https://aitapredictor-cmc.streamlit.app/"
    },
    {
        "title": "Self-Accident Detection App: Leveraging Machine Learning to Predict and Prevent Self-Accidents",
        "image_path": "images/MLDetection.png",
        "description": ("The goal of this project is to enhance road safety by applying machine learning techniques to predict and prevent self-accidents. This approach highlights the challenges and proposes solutions derived from predictive models, contributing to safer driving conditions."),
        "link": "https://mltrafficsafety-cmcova.streamlit.app/"
    },
    {
        "title": "Hello, Risk, Goodbye",
        "image_path": "images/adobo_front.png",
        "description": ("Churn Risk Profiling for Cost Optimization: Developed a predictive customer segmentation model to identify and mitigate churn risks, enabling strategic cost savings."
                        ),
        "link": "https://eskwelabssprint1-cmcova.streamlit.app/"
    }
]

# Convert images to base64 and add CSS for layout
st.markdown(
    """
    <style>
        .project-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
        }
        .project {
            border: 1px solid #e6e6e6;
            border-radius: 8px;
            padding: 16px;
            background-color: #f9f9f9;
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .project img {
            max-width: 80%;
            border-radius: 8px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .project h2 {
            margin-top: 16px;
        }
        .project p {
            text-align: justify;
        }
        .project a {
            margin-top: auto;
            text-decoration: none;
            color: #1a73e8;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display projects in sections
for idx, project in enumerate(projects):
    image_base64 = image_to_base64(project['image_path'])
    if idx == 0:
        # First project centered
        st.markdown(
            f"""
            <div class="centered-project" style="text-align:center;">
                <div class="project">
                    <a href="{project['link']}" target="_blank">
                        <img src="data:image/png;base64,{image_base64}" alt="Project Image">
                    </a>
                    <h2>{project['title']}</h2>
                    <p>{project['description']}</p>
                    <a href="{project['link']}" target="_blank">Click here to view</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Subsequent projects side by side
        if idx % 2 == 1:
            st.markdown('<div class="project-container">', unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <div class="project">
                <a href="{project['link']}" target="_blank">
                    <img src="data:image/png;base64,{image_base64}" alt="Project Image">
                </a>
                <h2>{project['title']}</h2>
                <p>{project['description']}</p>
                <a href="{project['link']}" target="_blank">Click here to view</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if idx % 2 == 0 or idx == len(projects) - 1:
            st.markdown('</div>', unsafe_allow_html=True)

#####################
def txt5(a, b, c=''):
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

def proficiency_emoji(level):
    if level == 'Advanced':
        return '🔥'
    elif level == 'Intermediate':
        return '📈'
    else:
        return '🌱'

st.markdown('''
## Skills
''')
txt5('Programming', '`Python`, `C++`, `Linux`', f"{proficiency_emoji('Intermediate')} {proficiency_emoji('Intermediate')} {proficiency_emoji('Intermediate')}")
txt5('Data processing/wrangling', '`SQL`, `pandas`, `numpy`', f"{proficiency_emoji('Advanced')} {proficiency_emoji('Advanced')} {proficiency_emoji('Advanced')}")
txt5('Data visualization', '`matplotlib`, `seaborn`, `plotly`', f"{proficiency_emoji('Advanced')} {proficiency_emoji('Intermediate')} {proficiency_emoji('Intermediate')}")
txt5('Machine Learning', '`scikit-learn`, `NLP`, `RAG`', f"{proficiency_emoji('Intermediate')} {proficiency_emoji('Intermediate')} {proficiency_emoji('Intermediate')}")
txt5('Deep Learning', '`Generative AI`', f"{proficiency_emoji('beginner')}")
txt5('Web development', '`HTML`, `CSS`', f"{proficiency_emoji('Intermediate')} {proficiency_emoji('beginner')}")
txt5('Model deployment', '`streamlit`', f"{proficiency_emoji('Intermediate')}")

#####################
st.markdown('''
## Interests
''')
txt3('Sports and Fitness', '`Basketball`, `Cross-Fit`')
txt3('Music and Dancing', '`R&B`, `Pop`, `Hip Hop`')
txt3('Traveling', '`Exploring new cultures`')
txt3('Research Paneling', '`Participating in school research presentation`')
txt3('Video Games', '`MOBA`, `Strategy games`')
txt3('Self-Improvement', '`Reading`, `Working-out`')


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/carlos-lester-covarrubias-ii-ece-6b235112b/')
txt2('DataCamp', 'https://www.datacamp.com/portfolio/clfinancialxxvi')
txt2('GitHub', 'https://github.com/lestong26')
txt2('Email', 'clfinancialxxvi@gmail.com')
