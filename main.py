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

def highlight_short_sentence(avg_length, sentence, deviation=3):
    

def highlight_long_sentence(avg_length, sentence, deviation=3):
    pass

def main(file_path, output_path):
    sentences = get_sentences(file_path)
    avg_length = get_average_sentence_length(sentences)
    processed = []

    for sentence in sentences:
        words = re.findall(r'\w+', sentence)
        if len(words) < avg_length:
            highlight_short_sentences(avg_length, sentence)
        else if len(words) > avg_length:
            highlight_long_sentence(avg_length, sentence)
        # sentence is of average length
        else:
            pass
        processed.push(sentence)
    
    with open(f'{output_path}.md', 'w') as f:
        f.write(''.join(processed))



    