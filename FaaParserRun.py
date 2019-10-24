from FaaParser import FaaParser
from pathlib import Path
import os


CURRENT_PATH = Path(os.getcwd())
DATA_DIRECTORY = str(CURRENT_PATH.parent)+ "/big-blast-results/genome-comparison-refseq-vs-genbank/"
OLD_GENOME_GCF = DATA_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
NEW_GENOME_GCA = DATA_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"



if __name__ == "__main__":

    parser = FaaParser()
    parser.setOutputDirectory(DATA_DIRECTORY)
    parser.readFaa(OLD_GENOME_GCF)
    parser.writeGeneLocusTag("GCF_oldGenomeLocusTags")

    parser2 = FaaParser()
    parser2.setOutputDirectory(DATA_DIRECTORY)
    parser2.readFaa(NEW_GENOME_GCA)
    parser2.writeGeneLocusTag("GCA_newGenomeLocusTags")

