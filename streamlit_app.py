import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Abhinav Reddy Nimma
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- With a passion for Machine Learning and programming, I am dedicated to designing and developing intelligent systems that learn autonomously from data.
- Expertise in end-to-end ML workflows and experience in solving real-world challenges make me a valuable asset to any team.
- With my creativity and passion for innovation, I am always eager to tackle new challenges and find innovative solutions.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Abhinav Reddy Nimma</a>
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
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social">Social Media</a>
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

txt('**Erasmus Mundus + Joint Master Degree, *Norwegian University of Science and Technology*, Norway',
'2021-2023')
st.markdown('''
- Master's in Colour and Visual Computing, Norwegian University of Science and Technology, Norway. 
- Master's in Photonics, Image and Vision, University of Granada, Spain.
- Research thesis entitled `Deep Learning based multi-exposure fusion for High Dynamic Range Imaging`. In association with DxO labs, as part of DxO PhotoLab R&D.
- Received Erasmus Mundus Scholorship of covering tuition and stipend for the academic years 2021-22 and 2022-23.
- Courses: Deep Learning for Visual Computing, Data Science, Computer Vision, Image Processing and Analysis  .
''')

txt('**Bachelor of Technology in Computer Science and Engineering** (Biological Science), *Mahindra university*, India',
'2016-2020')
st.markdown('''
- GPA: `9.21/10`
- Bachelors thesis entitled `deep learning-based Visual Inspection System surface damage detection in concrete surfaces`.'
- Received Mahindra Ecole Centrale Academic Excellence Scholorship for the academic years 2017-18 and 2018-19.
- Courses: Deep Learning, Machie Learning, Information Retrieval & NLP, Advanced Data Analytics, Data Structures, System Software, Object-Oriented Programming, Software Enginerring, Mathematics(I-IV), Distributed Systems, Computer Networks, Microprocessor and Interfacing, Digitl Electronics, System Software, Web Programming,.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Intern, Image Processing AI**, *DxO labs*, Paris, France',
'Feb2023- Aug 2023')
st.markdown('''
- Pursuing my Master Thesis as part of DxO Labs research studies for DxO Photolab 8. DxO is a market leader in AI based photography software
- Responsible for designing and developing End-to-end ML workflow for `Deep HDR Merge`, `deep learning-based multi exposure fusion technique for HDR Imaging`' .
- Created a large scale dataset with RAW images at different exposures and corresponding HDR pairs, a first of its kind in open literature.
- Experimenting with several neural network architectures to achive multi-exposure fusion.
- Aiming to ship "Deep HDR Merge" feature with DxO Photolab product. DxO Photolab is a digital image editing software package designed for professional photographers
''')

txt('**Machine Learning Intern**, Picterus AS, Trondheim, Norway',
'Jul 2022- Aug 2022')
st.markdown('''
- Picterus AS develops software for smartphone based monitoring of jaundice in new born babies. 
- Conducted pilot research exploring deep learning techniques to `reconstruct spectral reflectance of baby skin from smartphone images`.
- Designed and developed a prototype using Hierarchial Regression Networks for spectral reconstruction.
- The study found results satisfying, paving way for a full research into futher developing and integrating the prototype into the product.
''')
txt('**Software Developer Intern**, Dell, Hyderabad, India',
'Jan 2020- Mar 2020')
st.markdown('''
- Worked on developing and depoying `automated database migration` scripts for Business Intelligence Team at Dell Financial Services
''')
txt('**Research Intern**, Norwegian University of Science and Technology, Gjovik, Norway',
'Jun 2019- Aug 2019')
st.markdown('''
- Worked on developing a application for `Detecting potholes & cracks on road surfaces using Computer Vision` and AI from go-pro footage, mounted on car dashboards
''')




#####################
st.markdown('''
## Projects
''')
txt4('Energy Use Intensity Forecaster', 'A web application for the forecasting energy usage intensity of a site based on building characteristics and weather conditions', 'https://energy-intensity-forecast.streamlit.app/')
txt4('Background Eraser', 'A web application for erasing background out of an image using deep learning based computer vision techniques', 'https://background-eraser.streamlit.app/')
txt4('Stock Forecaster', 'A realtime live dashboard for the prediction and analysis of stocks','https://stock-forecast-web.streamlit.app/')
txt4('Weak Supervision for Capsule Endoscopy', 'Researching weak supervision techniques for geenrating pixel-level semantic segemntation masks from trainig data containing only image-level bounding box labels', '')
txt4('Generative AI for realistic material appearance', 'Developing GANs for realistic image synthesis with a particular focus on gloss, translucency and studying the latent space of the models for feature representation','')
txt4('Uncertinity estimation in learning-based image quality metrics', 'Developed novel technique to estimate the uncertainty in learning-based image quality metrics, as part of exlainable AI', '')
txt4('Organic waste classification', 'Deep ConvNets for classifying organic waste images from non organic ones', '')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `MATLAB`')
txt3('Data processing', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly` ')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`PyTorch`, `TensorFlow`')
txt3('Web development', '`React`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/abhinavreddyn/')
txt2('Twitter', 'https://twitter.com/abhinav_nimma')
txt2('GitHub', 'https://github.com/abhi9741')


