# Tweet-Sentiment-Predictor

![1,2,3](https://user-images.githubusercontent.com/93777016/205468893-845257df-4e81-41d3-94b1-d32e9e215afb.png)

# Contributors (Group 5)

- Brandon Groenewold
- Sanoo Singh
- Jon Kwiatkowski
- Nhan Tran
- Adrian Wood

# Datasets

- [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140) 

- [Original](https://drive.google.com/file/d/1ML1sG56MqlVX6oiNM4WDtPC3AFOO06y0/view?usp=share_link)

- [Cleaned](https://drive.google.com/file/d/1RgRj4J9FJZ0YYN36nSx-umP9eZNPff94/view?usp=share_link)  

- [Lemmatize](https://uom-twitter-sentiment-analysis.s3.us-east-2.amazonaws.com/Lemmatize.csv) 

# Major Tasks
- Apply ETL on the dataset
- Preprocessing
- Split Cleaned Data into Training Set and Testing Set
- Train the Models
- Saving the Vectorizer and Models
- Make Predictions
- Create Word Collage
- Build the website using HTML/CSS
- Build the flask server
- Host the website on Heroku 

# Project Objective

We will use datasets to create a model with (various) features that will predict whether a tweet is positive or negative. Using Pandas, AWS, HTML/CSS/JS/Bootstrap, and NLTK they will be ranked and weighted to see which way they get classified.

# Results:

After training and testing is concluded, there should be four Models (Logistic Regression Classifier, Stochastic Gradient Descent, Multinomial Naive Bayes, Light Gradient-Boosting) that can formulate Predictions. These are able to identify positive and negative tweets from a dataset. These models can be used with new information and can make a  determination on new entered  tweets and decide if the tweet is positive or negative with increasing levels of accuracy. The models can now be used with any new tweets collected  in the future for farther development.

# Imports

- pandas
- numpy
- NLTK
- string
- re
- dump
- RegexpTokenizer
- stopwords
- TfidfVectorizer
- train_test_split
- MultinomialNB
- confusion_matrix
- f1_score
- GridSearchCV
- SGDClassifier
- LogisticRegression
- LGBMClassifier

# Resources 
- https://medium.com/mlearning-ai/how-to-deploy-an-nlp-machine-learning-model-with-flask-on-web-788c2825b792
- https://github.com/conda-forge/lightgbm-feedstock
- https://github.com/javedsha/text-classification
- https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32

# Instructions
- Clone this repo to your computer
- Run app.py 
- Type in your tweet into the Tweet Input box to see the prediction results

# Landing Page
![Landing Page](https://user-images.githubusercontent.com/107283582/205543265-4e1cb5ab-699f-49eb-b481-c6d28b81639f.png)

# Word Cloud Description

A word cloud is a Visualization of a text meant to help understand information at a glance. It is a word image where each word's size is proportional to its importance, the more often it's mentioned within a given text words appear larger.

Being able to see the tweet information was helpful during the training and testing of the models. After looking at the word clouds you could see there are some words that are used in both positive and negitive tweets such as "i'm". This could be caused by people use it in both instances such as "i'm happy" and "i'm sad".

# Word Cloud for positive tweets

appon looking at the word clouds with positive tweets, we found that some of the positive words were a little out of the ordinary like "kackered" and some random  numbers. Some of these might have been able to make it in the positive words based on the words around them or the whole feel of the tweet, Other then the words themself.

![Screenshot 2022-12-03 220951](https://user-images.githubusercontent.com/93777016/205473855-ca189b2c-91d7-4028-bc5c-527cc392a6c6.png)


# Word Clod for negitive tweets

Just like with the positive tweets some of the words the models considered negative were somewhat suprising such as "cool" or "hope". Words that normally have a positive sentiment. After discussing it with the group, We came to the conclusion that some of these words might have made it in the negitive tweets because they could have been used to express expectations that might not have been met. 


![Screenshot 2022-12-03 220920](https://user-images.githubusercontent.com/93777016/205473869-1ee87d33-ec99-499b-a704-ad0e62bdf200.png)
