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
st.info('''With a passion for Machine Learning and programming, I am committed to designing and developing intelligent systems that learn autonomously from data. Expertise in end-to-end ML workflows and experience in solving real-world problems make me a valuable asset to any team. With my creativity and Passion for innovation, I am always eager to tackle new challenges and find innovative solutions to transform data into information and information into insights.
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

txt('**Erasmus Mundus + Joint Master Degree**, *Norwegian University of Science and Technology*, Norway',
'2021-2023')
st.markdown('''
- Masters in Colour and Visual Computing, Norwegian University of Science and Technology, Norway. 
- Masters in Photonics, Image and Vision, University of Granada, Spain.
- Research thesis entitled `Deep Learning based multi-exposure Fusion for High Dynamic Range Imaging`. In association with DxO labs, as part of DxO PhotoLab R&D.
- Received Erasmus Mundus Scholarship covering tuition and stipend for the academic years 2021-22 and 2022-23.
- Courses: Deep Learning for Visual Computing, Data Science, Computer Vision, Image Processing and Analysis.
''')

txt('**Bachelor of Technology in Computer Science and Engineering** (Biological Science), *Mahindra University*, India',
'2016-2020')
st.markdown('''
- GPA: `9.21/10`
- Bachelors thesis entitled `Deep Learning-based Visual Inspection System surface damage detection in concrete surfaces`.'
- Received Mahindra Ecole Centrale Academic Excellence Scholarship for the academic years 2017-18 and 2018-19.
- Courses: Deep Learning, Machine Learning, Information Retrieval & NLP, Advanced Data Analytics, Data Structures, System Software, Object-Oriented Programming, Software Engineering, Mathematics(I-IV), Distributed Systems, Computer Networks, Microprocessor and Interfacing, Digital Electronics, System Software, Web Programming.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Intern, Image Processing AI**, *DxO labs*, Paris, France',
'Feb2023- Aug 2023')
st.markdown('''
- Pursuing my Master Thesis as part of DxO Labs research studies for DxO Photolab 8. DxO is a market leader in AIbased photography software
- Responsible for designing and developing End-to-end ML workflow for `Deep HDR Merge`, a `deep learning-based multi-exposure fusion technique for HDR Imaging`.
- Created a large-scale dataset with RAW images at different exposures and corresponding HDR pairs, a first of its kind in the open literature.
- Experimenting with several neural network architectures to achieve multi-exposure fusion.
- Aiming to ship the "Deep HDR Merge" feature with the DxO Photolab product. DxO Photolab is a digital image editing software package designed for professional photographers
''')

txt('**Machine Learning Intern**, Picterus AS, Trondheim, Norway',
'Jul 2022- Aug 2022')
st.markdown('''
- Picterus AS develops software for smartphone-based monitoring of jaundice in newborn babies. 
- Conducted pilot research exploring deep learning techniques to `reconstruct spectral reflectance of baby skin from smartphone images`.
- Designed and developed a prototype using Hierarchical Regression Networks for spectral reconstruction.
- The study found the results satisfying, paving the way for full research into further developing and integrating the prototype into the product.
''')
txt('**Software Developer Intern**, Dell, Hyderabad, India',
'Jan 2020- Mar 2020')
st.markdown('''
- Worked on developing and deploying `automated database migration` scripts for Business Intelligence Team at Dell Financial Services
''')
txt('**Research Intern**, Norwegian University of Science and Technology, Gjovik, Norway',
'Jun 2019- Aug 2019')
st.markdown('''
- Worked on developing an application for `Detecting potholes & cracks on road surfaces using Computer Vision` and AI from go-pro footage, mounted on car dashboards
''')




#####################
st.markdown('''
## Projects
''')
txt4('Energy Use Intensity Forecaster', 'A web application for the forecasting energy usage intensity of a site based on building characteristics and weather conditions. Demonstrating end-to-end ML workflow.', 'https://energy-intensity-forecast.streamlit.app/')
txt4('Background Eraser', 'A web application for erasing background out of an image using deep-learning based computer vision techniques. Demonstrating end-to-end ML workflow.', 'https://background-eraser.streamlit.app/')
txt4('Stock Forecaster', 'A real-time live dashboard for the prediction and analysis of stocks. Demonstrating end-to-end ML workflow.','https://stock-forecast-web.streamlit.app/')
txt4('Generative AI for realistic material appearance', 'Developing GANs for realistic image synthesis with a particular focus on gloss, translucency and studying the latent space of the models for feature representation','results will be shared after publication')
txt4('Uncertainty estimation in learning-based image quality metrics', 'Developed a novel technique to estimate the uncertainty in learning-based image quality metrics, as part of explainable  AI', 'results will be shared after publication')
txt4('Organic waste classification', 'Deep ConvNets for classifying organic waste images from non-organic ones', 'https://github.com/abhi9741/Organic-Waste-Classification-from-Images-of-Waste')
txt4('Detecting Eye Disease-using Deep Learning', '/  Experimenting with different architectures and techniques to improve classification accuracy in Diabetic Retinopathy', 'https://github.com/abhi9741/Detecting-Eye-Disease-using-Deep-Learning')
txt4('Market Segmentation on E-Commerce Sales Data', '/Segmenting existing customers into various sub-groups based on shared characteristics based on order records from an E-Commerce portal)', 'https://github.com/abhi9741/Market-Segmentation-with-Machine-Learning-from-E-Commerce-Sales-Data')
txt4('Role of Segmentation in Skin Lesion Classification', '/Experimenting with traditional and deep learning-based segmentation techniques to understand the influence of segmentation on skin lesion classification task', 'https://github.com/abhi9741/Role-of-Segementation-in-Skin-Lesion-Classification')
txt4('Weak Supervision for Capsule Endoscopy', 'Researching weak supervision techniques for generating pixel-level semantic segmentation masks from training data containing only image-level bounding box labels', '')




#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `MATLAB`')
txt3('Data processing', '`SQL`, `pandas`, `NumPy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly` ')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`PyTorch`, `TensorFlow`')
txt3('Web development', '`React`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`')

#####################
st.markdown('''
## Social
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/abhinavreddyn/')
txt2('Twitter', 'https://twitter.com/abhinav_nimma')
txt2('GitHub', 'https://github.com/abhi9741')


