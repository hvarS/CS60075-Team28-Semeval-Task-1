import sys
import csv
import glob
import os.path
import argparse
from collections import defaultdict
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate(submission_foldername, reference_fname):
    # If the question predictions file was supplied, run the scoring on it
    if os.path.exists(submission_foldername):
        for x in os.listdir(submission_foldername):
            result = "\nFor file {}\n".format(x)
            #Read predictions:
            submission_dict = {}
            with open(os.path.join(submission_foldername,x), 'r') as sf:
                csv_reader = csv.reader(sf)
                for item in csv_reader:
                    submission_dict[item[0]] = float(item[1])
            
            #Read reference:
            gold_dict = {}
            with open(reference_fname, 'r') as rf:
                csv_reader = csv.reader(rf)
                for item in csv_reader:
                    gold_dict[item[0]] = float(item[-1])

            #Produce vectors with reference labels and predictions:
            gold = []
            predicted = []
            
            for key, label in gold_dict.items():
                gold.append(label)
                predicted.append(submission_dict[key])
            
            #Calculate scores:
            pearson_score = pearsonr(gold, predicted)[0]
            spearman_score = spearmanr(gold, predicted)[0]
            mae_score = mean_absolute_error(gold, predicted)
            mse_score = mean_squared_error(gold, predicted)
            rsq_score = r2_score(gold, predicted)
            result += "pearson  :  {0}\n".format(pearson_score)
            result += "spearman :  {0}\n".format(spearman_score)
            result += "mae      :  {0}\n".format(mae_score)
            result += "mse      :  {0}\n".format(mse_score)
            result += "r2       :  {0}".format(rsq_score)
            print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission_foldername", type=str, required=True, help="submission folder name")
    parser.add_argument("--reference_filename",type=str, required=True, help="reference file name")
    args = parser.parse_args()
    
    evaluate(args.submission_foldername, args.reference_filename)