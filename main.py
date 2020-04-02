import os
import sys
import nltk
import re

def get_sentences(file_path):
    nltk.download('punkt')
    with open(file_path) as f:
        content = f.read()
        sentences = nltk.tokenize.sent_tokenize(content)
        return sentences

def get_average_sentence_length(sentences):
    total = 0
    for sentence in sentences:
        total += len(re.findall(r'\w+', sentence))
        
    return total/len(sentences)

def highlight_short_sentence(sentence, deviation=3):
    return f'**{sentence}**'

def highlight_long_sentence(sentence, deviation=3):
    return f'*{sentence}*'

def main(file_path, output_path='output'):
    sentences = get_sentences(file_path)
    avg_length = get_average_sentence_length(sentences)
    processed = []

    for sentence in sentences:
        words = re.findall(r'\w+', sentence)
        highlighted = ''
        if len(words) < avg_length:
           highlighted = highlight_short_sentence(sentence)
        elif len(words) > avg_length:
            highlighted = highlight_long_sentence(sentence)
        # sentence is of average length
        else:
            highlighted = sentence
        processed.append(highlighted)
    
    with open(f'{output_path}.md', 'w') as f:
        f.write('\n'.join(processed))


    