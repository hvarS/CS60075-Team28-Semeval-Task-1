# CS60075-Team28-Task-1

## Steup the repo on colab
To execute code, please clone it in your drive. To clone it, just follow these simple steps for adding ssh key to your github account:
* Make a copy and execute this colab [file](https://colab.research.google.com/drive/13XQR16ltagN0QYB2u8yxc66d7yV2U10f?usp=sharing). The same file is also available here - https://github.com/hvarS/CS60075-Team28-Task-1/blob/main/setup_on_colab.ipynb 

## Repo Details
All the .ipynb python notebooks of preprocessing, extracting features and eperimentations can be executed easily after cloning the repository to your drive. Relevant PATHS are already given, and works if above mentioned steps are followed for cloning. 

### Final submission files
We have included different properly commented files, which represents out scores we reported from different approaches for better readability:
* `baseline.ipynb` : Baseline scores
* `baseline_with_features.ipynb` : Scores after adding features
* `attention_multi.ipynb` : Task2 scores using attention-based approach
* `attention_single.ipynb`: Task1 scores using attention-based approach

Last two files also consists of other experimentations, i.e using BERT instead of Bi-LSTM, not using anything expect dense layers for attention, using CNN+Regression. But we did'nt report them, as we got better results using Bi-LSTM. The code is still available at the end of the files.

**Files are better viewed using colab, Table of contents**

### Files for preprocessing and other experimentation 
Here we describe other individual files and folder:

* `baselines_and_with_features.ipynb`: contains code for baselines and experiments after adding the extracted features
* `corpus_features_1.ipynb`: extracts the required data, plots from each corpus, which are dumped in `data/MRC/familarity.txt`, `data/sorted`, `plots/`
* `corpus_features_2.ipynb`: generates the respective features from each corpus, i.e. binary features whether the token is present in top `x` words of the corpus and familarity value of token, saving the respective features in `data/added_features/`
* `corpus_features_extraction_multi.ipynb and corpus_features_extraction_single.ipynb`: generates other features, i.e. POS, wordnet features (synonyms, hyponyms, hypernyms, senses), syllables, token length, etc. dumping csvs to `data/extra_features/`
* `eval.py`: Official Evaluate function
* `preprocess.py`: initial preprocessing, lowercase, remove punctuations, lemmatization

* `references/`: contains labels for evaluate
* `predictions/`: contains the output from experimentations
* `corpus.zip`: contains relevant corpus files

## Scores Screenshot
Task1 Submission![image](https://user-images.githubusercontent.com/43145576/114409836-7b571080-9bc8-11eb-9581-750f32e48a03.png)
Task2 Submission![image](https://user-images.githubusercontent.com/43145576/114409984-9cb7fc80-9bc8-11eb-8a50-b3f42069f6f2.png)

### Older experiments
Conda env setup is only required for initial preprocessing, which was done earlier. We shifted to colab after this. 
* `conda env create -f env.yml`
* `conda activate nlpTask1`
* `preprocess.py [-h] --file FILE`
* `eval.py [-h] --submission_foldername SUBMISSION_FOLDERNAME --reference_filename REFERENCE_FILENAME`
