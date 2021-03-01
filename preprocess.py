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

def read_tsv_single(file, test):
	File = open(file, "r")
	data = {"id": [], "corpus": [],  "sentence": [],"token" :[]}
	if not test:
		data['complexity']=[]
	
	File.readline()
	while True:
		line = File.readline()
		if len(line) == 0:
			break

		line = line.split()
		data["id"].append(line[0])
		data["corpus"].append(line[1])
		if not test:
			data["sentence"].append(' '.join(line[1:-2]))
			data["token"].append(line[-2])
			data["complexity"].append(float(line[-1]))
		else:
			data["sentence"].append(' '.join(line[1:-1]))
			data["token"].append(line[-1])
	return pd.DataFrame(data)


def read_tsv_multi(file, test):
	File = open(file, "r")
	data = {"id": [], "corpus": [],  "sentence": [],
			"token": []}
	if not test:
		data['complexity']=[]

	File.readline()
	while True:
		line = File.readline()
		if len(line) == 0:
			break

		line = line.split()
		data["id"].append(line[0])
		data["corpus"].append(line[1])
		if not test:
			data["sentence"].append(' '.join(line[1:-3]))
			data["token"].append(' '.join(line[-3:-1]))
			data["complexity"].append(float(line[-1]))
		else:
			data["sentence"].append(' '.join(line[1:-2]))
			data["token"].append(' '.join(line[-2:]))
	return pd.DataFrame(data)

def preprocess(df):
	
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
	if(args.single):
		df = read_tsv_single(args.file, args.test)
	else:
		df = read_tsv_multi(args.file, args.test)
	print(len(df))
	preprocessed_df = preprocess(df)

	name = args.file.split("/")[-1].split(".")[0]+"_preprocessed"
	preprocessed_df.to_csv(os.path.join("data/preprocessed",name+".csv"), index=False)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--file", type=str, required=True, help="df file path")
	parser.add_argument("--single",action='store_true', help="df file path")
	parser.add_argument("--test",action='store_true', help="df file path")
	args = parser.parse_args()
	main(args)
