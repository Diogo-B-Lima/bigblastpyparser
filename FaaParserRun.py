from FaaParser import FaaParser
from pathlib import Path
import os
import pandas as pd


CURRENT_PATH = Path(os.getcwd())
DATA_DIRECTORY = str(CURRENT_PATH.parent)+ "/big-blast-results/genome-comparison-refseq-vs-genbank/"
NEW_GENOME_GCF = DATA_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
OLD_GENOME_GCA = DATA_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"



if __name__ == "__main__":

    # parser = FaaParser()
    # parser.setOutputDirectory(DATA_DIRECTORY)
    # parser.readFaa(NEW_GENOME_GCF)
    # parser.writeGeneLocusTag("GCF_newGenomeLocusTags")
    #
    # parser2 = FaaParser()
    # parser2.setOutputDirectory(DATA_DIRECTORY)
    # parser2.readFaa(OLD_GENOME_GCA)
    # parser2.writeGeneLocusTag("GCA_oldGenomeLocusTags")

    #parser3 = FaaParser()
    #parser3.setOutputDirectory(DATA_DIRECTORY)
    #parser3.readFaa(OLD_GENOME_GCA)
    #parser3.exportToCSV("GCA_002906115.1_CorkOak1.0_protein.csv")

    #parser4 = FaaParser()
    #parser4.readFaa(NEW_GENOME_GCF)
    #parser4.exportToCSV("GCF_002906115.1_CorkOak1.0_protein.csv")


    data = pd.read_csv("C:/Users/Diogo/Nextcloud/cork2019/bigBlast/big-blast-parser-python/GCF_002906115.1_CorkOak1.0_protein.csv")
    print(len(data["Sequence"]))
    print(len(data["Sequence"].unique()))
    print(len(data["Sequence"]) - len(data["Sequence"].unique()))


