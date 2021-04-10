# CS60075-Team28-Task-1

Here we describe individual files and folder:

* `baselines_and_with_features.ipynb`: contains code for baselines and experiments after adding the extracted features
* `corpus_features_1.ipynb`: extracts the required data, plots from each corpus, which are dumped in `data/MRC/familarity.txt`, `data/sorted`, `plots/`
* `corpus_features_2.ipynb`: generates the respective features from each corpus, i.e. binary features whether the token is present in top `x` words of the corpus and familarity value of token, saving the respective features in `data/added_features`
* `corpus_features_3.ipynb`: generates other features, i.e. POS, wordnet features (synonyms, hyponyms, hypernyms, senses), syllables, token length, etc. dumping csvs to `data/extra_features`
* `eval.py`: Evaluate function
* `preprocess.py`: initial preprocessing, lowercase, remove punctuations, lemmatization

* `references/`: contains labels for evaluate
* `predictions/`: contains the output from experimentations
* `corpus/`: contains relevant corpus files, used in extracting features, can be downloaded from [here](https://drive.google.com/file/d/1w2IJj9JzdBiASOqfXzCdD7eN183dZeGC/view?usp=sharing)

### Older experiments
Conda env setup is only required for initial preprocessing, which was done earlier. We shifted to colab after this. 
* `conda env create -f env.yml`
* `conda activate nlpTask1`
* `preprocess.py [-h] --file FILE`
* `eval.py [-h] --submission_foldername SUBMISSION_FOLDERNAME --reference_filename REFERENCE_FILENAME`
