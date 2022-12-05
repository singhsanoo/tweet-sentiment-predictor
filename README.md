# tweet-sentiment-predictor

![1,2,3](https://user-images.githubusercontent.com/93777016/205468893-845257df-4e81-41d3-94b1-d32e9e215afb.png)

# Contributors (Group 5)

-Brandon Groenewold
-Sanoo Singh
-Jon Kwiatkowski
-Nhan Tran
-Adrian Wood

## Major Tasks:
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

After training and testing is concluded, there should be two Models that can formulate Predictions with the "SGD Model" and "Logical model". These are able to identify positive and negative tweets from a dataset. This model can be used with new information and can make a  determination on new entered  tweets and decide if the tweet is positive or negative with increasing levels of accuracy. The models can now be used with any new tweets collected  in the future for farther development.


# Imports
pandas, numpy, NLTK, string, re, dump, RegexpTokenizer, stopwords, TfidfVectorizer, train_test_split, MultinomialNB, confusion_matrix, f1_score, GridSearchCV, SGDClassifier, LogisticRegression, LGBMClassifier. 

# Instructions
- Clone this repo to your computer
- Run app.py 
- Type in your tweet into the Tweet Input box to see the prediction results

## Landing Page
![Landing Page](https://user-images.githubusercontent.com/107283582/205543265-4e1cb5ab-699f-49eb-b481-c6d28b81639f.png)

## Word Cloud for positive tweets
![Screenshot 2022-12-03 220951](https://user-images.githubusercontent.com/93777016/205473855-ca189b2c-91d7-4028-bc5c-527cc392a6c6.png)


## Word Cloud for negitive tweets


![Screenshot 2022-12-03 220920](https://user-images.githubusercontent.com/93777016/205473869-1ee87d33-ec99-499b-a704-ad0e62bdf200.png)




