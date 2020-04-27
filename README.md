# old-article-downloader

## 1. Generate requirements.txt

a. Activate virtual environment

> cd old-article-downloader

>source venv/bin/activate

b. Get requirements.txt

> pip3 freeze > requirements.txt 

## 2. setting up repository

a. Install libraries from requirements.txt

> pip install -r requirements.txt

b. Download NLTK data using python console

> import nltk
> nltk.download('punkt')

## 3. How to run repository ?

a. Execute run.py file.

>nohup python3 run.py

## 4. Install Java for stanford NER ?


>sudo apt-get install default-jre
>
>sudo apt-get install default-jdk
>
>sudo update-alternatives --config java



