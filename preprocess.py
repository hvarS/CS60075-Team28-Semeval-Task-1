import os
import csv
import nltk
import string
import argparse
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer

# lemmatize words
lemmatizer = WordNetLemmatizer() 
def lemmatize(text):
    lemmas = [lemmatizer.lemmatize(word) for word in word_tokenize(text)] 
    return " ".join(lemmas)

# remove stopwords
def remove_stopwords(text, token):
	words = [w for w in word_tokenize(text) if (w not in stopwords.words('english')) or w in list(word_tokenize(token))]
	return " ".join(words)

def preprocess(file):
	df = pd.read_csv(file, sep="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
	df["token"] = df['token'].astype(str)

	# lower case
	df['sentence'] = df['sentence'].apply(lambda x: x.lower())
	df['token'] = df['token'].apply(lambda x: x.lower())

	# remove punctuation
	translator = str.maketrans('', '', string.punctuation)
	df['sentence'] = df['sentence'].apply(lambda x: x.translate(translator))
	df['token'] = df['token'].apply(lambda x: x.translate(translator))

	# remove stopwords only if token != a stopword
	try:
		nltk.data.find('corpora/stopwords')
	except LookupError:
		nltk.download('stopwords')

	df['sentence'] = df.apply(lambda x: remove_stopwords(x['sentence'], x['token']) , axis=1)
	
	# lemmatize
	df['sentence'] = df['sentence'].apply(lambda x: lemmatize(x))
	df['token'] = df['token'].apply(lambda x: lemmatize(x))

	return df

def main(args):
	assert os.path.exists(args.file), "{} does not exists".format(args.file)
	preprocessed_df = preprocess(args.file)

	name = args.file.split("/")[-1].split(".")[0]+"_preprocessed"
	preprocessed_df.to_csv(os.path.join("data/preprocessed",name+".csv"))


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--file", type=str, required=True, help="df file path")
	args = parser.parse_args()
	main(args)
