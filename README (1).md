
# InSocial: 📊 Sentiment Analysis Web Application
![image](https://github.com/samakshty/InSocial/assets/140980901/87d3ab68-034c-4ed0-b170-840d97d0e214)


## ⭐⭐ Project Showcase at SIH 2023, Bennett University

### Deployed Application: https://insocial.streamlit.app/

Developed by [Samaksh Tyagi](https://github.com/samakshty) and [Sukant Aryan](https://github.com/eviack)

### Video Demo


https://github.com/samakshty/InSocial/assets/140980901/c0f23e42-e643-49ef-80ae-2008748da25c





## Table of Contents
- [Background](#background)
- [Features](#features)
- [ML Algorithm](#ml-algorithm)
- [Instructions to Run](#instructions-to-run)
- [Requirements](#requirements)
- [Description of Project](#description-of-project)
- [Contributions and Acknowledgments](#contributions-and-acknowledgments)

## Background
With the increasing importance of understanding public sentiment on social media platforms, InSocial aims to provide users with a tool for analyzing sentiment across various online platforms. Our application utilizes state-of-the-art machine learning techniques to provide insightful sentiment analysis on user-specified topics.
 
## Description of Project
The InSocial web application provides users with an intuitive interface to perform sentiment analysis on text data or social media posts. Users can input their desired text or specify social media platforms for analysis. The application utilizes cutting-edge machine learning algorithms to generate insightful sentiment analysis reports, including sentiment scores and visualizations.

## Features
- Real-time sentiment analysis of user-provided text or social media posts.
- Visualizations of sentiment trends over time.
- Customizable sentiment analysis based on specific topics or keywords.
- Integration with popular social media platforms for seamless analysis.

  
<img width="968" alt="What does InSocial do?" src="https://github.com/samakshty/InSocial/assets/140980901/4629235f-8354-4134-9b38-058bd3d72338">

<img width="969" alt="Product Infographics" src="https://github.com/samakshty/InSocial/assets/140980901/b23f5475-aac2-4e8a-9699-4039eca9632d">


## ML Algorithm
<img width="969" alt="Flow of Program" src="https://github.com/samakshty/InSocial/assets/140980901/45a5f0ce-2f21-4360-afee-637cc21555e4">

### Input
User-provided text or social media posts.

### Data Preprocessing
- Employed natural language processing (NLP) techniques for data preprocessing, including:
  - Stop words removal
  - Stemming
  - Lemmatization

### Sentiment Analysis Techniques
- Utilized advanced NLP techniques, including sentiment lexicons and machine learning models.
- Developed an ML model to classify textual data into positive, negative, or neutral sentiment categories.
- Leveraged NLP models from `Hugging Face transformers` to achieve exceptional accuracy in sentiment classification.
- Utilized `VADER` (NLP-based model) for bulk data analysis.
- Trained a `naive Bayes classifier` specifically for analyzing reviews.

### Dataset
- Size ranges from 40,000 to 50,000 samples.

### Output
Sentiment scores and visualizations depicting sentiment trends.


## Instructions to Run
To run this project locally, follow these steps:

- Install Requirements
```pip install -r requirements.txt```

- Run the application
```streamlit run Home.py```

## Requirements
```
pandas
numpy
nltk
scikit-learn
streamlit
matplotlib
plotly==5.17.0
pygwalker==0.4.8
scipy==1.13.0
st_annotated_text==4.0.1
stqdm==0.0.5
streamlit==1.26.0
streamlit_extras==0.4.2
transformers==4.33.2
wordcloud==1.9.2
torch==2.2.2
```

## Contributions and Acknowledgments
This project is open for contributions, and we welcome any feedback or suggestions for improvement. If you find this project useful, feel free to use it for your needs. When attributing this project, please mention:
```
InSocial by Samaksh Tyagi & Sukant Aryan
Repository: https://github.com/samakshtyagi/insocial
```
