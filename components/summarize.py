import streamlit as st
import nltk
nltk.download('punkt')

import time

from math import ceil
from newspaper import Article


# from nlp_model import generate_summary

def fetch_text_data(article):
    article.download()
    article.parse()
    article.nlp()
    print('\nTitle\n', article.title)
    print('\nSUMMARY\n', article.summary)
    print('\nKEYWORDS\n', article.keywords)
    return article

def change_complexity(summary, range):
    sens = summary.split('.\n')
    full = []
    for i in sens[0:range]:
        full.append(i)
    final = ''
    for i in full:
        i = i + '.'
        final += i
    final = final.replace('.', '. ')
    return final[:-2]

def app():
    st.title('NLP Article Summary')

    st.write('Summarize politcal articles to a readable length using our Natural Language Processing System')

    url = str(st.text_input('Enter an Article URL'))
    complex_val = st.slider('Length and Complexity', 1, 100)
    reader_article = Article(url)
    if (st.button('Summarize') and url != ''):
        with st.empty():
            for i in range(1):
                processed_article = fetch_text_data(reader_article)
                full_summary = change_complexity(processed_article.summary, ceil(complex_val/25)+1)
                st.caption('Evaluating...')
                time.sleep(1)
            st.caption('Done!')
        st.write('`Title: `', processed_article.title)
        st.write('`Summary: `', full_summary)
        st.write('`Key Topics: `', processed_article.keywords)
    
        # new_summary = generate_summary(processed_article.text, 2)