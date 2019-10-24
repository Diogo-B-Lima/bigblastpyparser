from mainParser import BigBlastParser
from pathlib import Path
import os


CURRENT_PATH = Path(os.getcwd())
RESULTS_DIRECTORY = str(CURRENT_PATH.parent)+ "/big-blast-results/genome-comparison-refseq-vs-genbank/"
BIG_BLAST_RESULTS = RESULTS_DIRECTORY + "finalResults.json"
BIG_BLAST_RESULTS_COMPLEMENTARY = RESULTS_DIRECTORY + "complementary_finalResults.json"


if __name__ == "__main__":

    parser = BigBlastParser()
    parser.setOutputDirectory(RESULTS_DIRECTORY)
    #print(parser.getEvalueThreshold())
    #print(parser.getEvalueThreshold())
    parser.readJson(BIG_BLAST_RESULTS)
    #print(parser.head())
    #print(parser.tail())
    #print(parser.getHitsByQuery("POE91707.1"))

    # parser.setIdentityThreshold(1)
    # perfectHits = parser.getHitsByThresholds()
    # #parser.writeResultsinJson(perfectHits, "perfectHits")
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







