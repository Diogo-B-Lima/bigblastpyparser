from BigBlastParser import BigBlastParser
from pathlib import Path
import os


CURRENT_PATH = Path(os.getcwd())
RESULTS_DIRECTORY = str(CURRENT_PATH.parent)+ "/big-blast-results/genome-comparison-refseq-vs-genbank/"
BIG_BLAST_RESULTS = RESULTS_DIRECTORY + "finalResults.json"
BIG_BLAST_RESULTS_COMPLEMENTARY = RESULTS_DIRECTORY + "complementary_finalResults.json"
NEW_GENOME_GCF = RESULTS_DIRECTORY + "GCF_002906115.1_CorkOak1.0_protein.faa"
OLD_GENOME_GCA = RESULTS_DIRECTORY + "GCA_002906115.1_CorkOak1.0_protein.faa"


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





if __name__ == "__main__":

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
    findBestHitForEachQueryByParameter()








