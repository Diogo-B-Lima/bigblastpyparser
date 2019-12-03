from BigBlastParser import BigBlastParser
from pathlib import Path
import os
import pandas as pd


CURRENT_PATH = Path(os.getcwd())
RESULTS_DIRECTORY = str(CURRENT_PATH.parent)+ "/big-blast-results/genome-comparison-refseq-vs-genbank/"
BIG_BLAST_RESULTS = RESULTS_DIRECTORY + "finalResults.json"
BIG_BLAST_RESULTS_COMPLEMENTARY = RESULTS_DIRECTORY + "complementary_finalResults.json"
NEW_GENOME_GCF = RESULTS_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
OLD_GENOME_GCA = RESULTS_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"
DEMO = RESULTS_DIRECTORY + "demo.json"
DATA_DIRECTORY = RESULTS_DIRECTORY + "../../../databases/data/"


def findQueriesWithNoHits():

    parser = BigBlastParser()
    parser.setOutputDirectory(RESULTS_DIRECTORY)
    parser.readJson(BIG_BLAST_RESULTS)
    parser.readJson(BIG_BLAST_RESULTS_COMPLEMENTARY, complementary = True)
    print("Queries with no hits - old genome")
    print(len(parser.getQueriesWithNoHits(NEW_GENOME_GCF)))
    print()
    print("Queries with no hits - new genome")
    print(len(parser.getQueriesWithNoHits(OLD_GENOME_GCA, complementary = True)))


def findBestHitForEachQueryByParameter():

    parser = BigBlastParser()
    parser.setOutputDirectory(RESULTS_DIRECTORY)
    parser.readJson(BIG_BLAST_RESULTS)
    parser.readJson(BIG_BLAST_RESULTS_COMPLEMENTARY, complementary = True)
    bestTC =  parser.getBestHitByParameter("target_coverage")
    parser.writeResultsinJson(bestTC, "bestTargetCoverage")
    bestIdentityComplementary = parser.getBestHitByParameter("identity", complementary = True)
    parser.writeResultsinJson(bestIdentityComplementary, "bestIdentityComplementary")


    print(parser.getBigBlastResults()["POE87087.1"])


def convertJSON2CSV():

    parser = BigBlastParser()
    parser.setOutputDirectory(RESULTS_DIRECTORY)
    parser.JSON2CSV(BIG_BLAST_RESULTS, BIG_BLAST_RESULTS.replace(".json", ".csv"))
    parser.JSON2CSV(BIG_BLAST_RESULTS_COMPLEMENTARY, BIG_BLAST_RESULTS_COMPLEMENTARY.replace(".json", ".csv"))


def fixJSON2CSVHopefully():

    parser = BigBlastParser()
    parser.setOutputDirectory(RESULTS_DIRECTORY)
    parser.readJson(DEMO)






if __name__ == "__main__":

    pass

    # parser = BigBlastParser()
    # parser.setOutputDirectory(RESULTS_DIRECTORY)
    # parser.readJson(BIG_BLAST_RESULTS)
    #
    # parser.setIdentityThreshold(1)
    # perfectHits = parser.getHitsByThresholds()
    # parser.writeResultsinJson(perfectHits, "perfectHits")
    #
    # print(len(perfectHits))
    # print(parser.countQueriesWithHits(perfectHits))
    #
    # print("#"*20)
    #
    # parserComplementary=BigBlastParser()
    # parserComplementary.setOutputDirectory(RESULTS_DIRECTORY)
    # parserComplementary.readJson(BIG_BLAST_RESULTS_COMPLEMENTARY)
    # parserComplementary.setIdentityThreshold(1)
    # perfectHitsComplementary = parserComplementary.getHitsByThresholds()
    #
    # print(len(perfectHitsComplementary))
    # print(parserComplementary.countQueriesWithHits(perfectHitsComplementary))

    #findQueriesWithNoHits()
    #findBestHitForEachQueryByParameter()

    #convertJSON2CSV()
    #fixJSON2CSVHopefully()








