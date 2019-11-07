import json
from FaaParser import FaaParser


class BigBlastParser:

    ###### CONSTRUCTOR ######

    def __init__(self):


        self.__bigBlastResults = {} # store first BLAST of BIDIRECTIONAL BEST HITS SEARCH in a dictionary
        self.__bigBlastComplementaryResults = {} # store second BLAST of BIDIRECTIONAL BEST HITS SEARCH in a dictionary
        self.__evalueThreshold = 100.0 # evalue threshold is the only maximum threshold
        self.__targetCoverageThreshold = 0.0 # all other thresholds are intended to be minimum thresholds
        self.__queryCoverageThreshold = 0.0
        self.__alignmentLengthThreshold = 0.0
        self.__bitScoreThreshold = 0.0
        self.__identityThreshold = 0.0
        self.__scoreThreshold = 0.0
        self.__outputDirectory = ""  # directory where analysis results will be stored


    ##### PUBLIC METHODS ######


    def readJson(self, jsonFile, complementary = False):
        """
        Reads a JSON file and loads the data in the BigBlastParser object
        :param jsonFile: Complete path to the file in JSON format
        :param complementary: Boolean to work with the "normal" or "complementary" results of Bidirectional Best Hits Search BLAST
        :return: Void method
        """

        with open(jsonFile) as input:
            data = json.load(input)

        if complementary == True:
            self.__bigBlastComplementaryResults = data

        elif complementary == False:
            self.__bigBlastResults = data

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")



    def head(self, complementary = False):
        """
        returns the value of the first key stored in the bigBlastParser results
        :param complementary: Boolean to work with the "normal" or "complementary" results of Bidirectional Best Hits Search BLAST
        :return: value of first key in bigBlastParser results
        """

        if complementary == True:
            results = self.__bigBlastComplementaryResults

        elif complementary == False:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        firstKey = list(results.keys())[0]
        return results[firstKey]


    def tail(self, complementary = False):

        if complementary == True:
            results = self.__bigBlastComplementaryResults

        elif complementary == False:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        firstKey = list(results.keys())[-1]
        return results[firstKey]


    def getHitsByQuery(self, query, complementary = False):

        if complementary == True:
            results = self.__bigBlastComplementaryResults

        elif complementary == False:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        return results[query]


    def getHitsByThresholds(self, complementary = False):

        if complementary == True:
            results = self.__bigBlastComplementaryResults

        elif complementary == False:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        hitsByThresholds = {}
        for queryGeneLocusTag in results:
            hitsByThresholds[queryGeneLocusTag] = {}
            for hitsGeneLocusTag in results[queryGeneLocusTag]:

                hitMeetsThreshold = True
                hit = results[queryGeneLocusTag][hitsGeneLocusTag]
                for parameters in hit:

                    if parameters == "score" and float(hit[parameters]) < self.__scoreThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "target_coverage" and float(hit[parameters]) < self.__targetCoverageThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "align_len" and float(hit[parameters]) < self.__alignmentLengthThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "bitScore" and float(hit[parameters]) < self.__bitScoreThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "identity" and float(hit[parameters]) < self.__identityThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "query_coverage" and float(hit[parameters]) < self.__queryCoverageThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "e_value" and float(hit[parameters]) > self.__evalueThreshold:
                        hitMeetsThreshold = False
                        break


                if hitMeetsThreshold:
                    hitsByThresholds[queryGeneLocusTag][hitsGeneLocusTag] = hit

        return hitsByThresholds


    def writeResultsinJson(self, data, jsonFileName):

        if not self.__outputDirectory:
            raise Exception("Please set a working directory before writing files")

        jsonFileNameProcessed = str(jsonFileName)
        if not jsonFileNameProcessed.endswith(".json"):
            jsonFileNameProcessed += ".json"

        self.__dumpJSON(data, self.__outputDirectory+jsonFileNameProcessed)


    def countQueriesWithHits(self, data):

        count = 0
        for query in data:
            if len(data[query])>0:
                count += 1

        return count


    def getQueriesWithNoHits(self, faaFile, complementary = False):

        if complementary == False:   # NOTE THAT IN THIS SPECIFIC METHOD WE WANT TO FIND THE FASTA FILE LOCUS TAGS IN THE OPPOSITE BLAST RESULT OF THE BLAST BIDIRECTIONAL SEARCH
            results = self.__bigBlastComplementaryResults

        elif complementary == True:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        faa = FaaParser()
        faa.readFaa(faaFile)

        return self.__findUnilateralNonOverlappingItemsFromTwoCollections(faa.getGeneLocusTag(), results)


    def getBestHitByParameter(self, parameter, complementary = False):


        if complementary == True:
            results = self.__bigBlastComplementaryResults

        elif complementary == False:
            results = self.__bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        parametersList = list(list(results[list(results.keys())[0]].values())[0].keys())

        if parameter not in parametersList:
            raise Exception("you must a enter a valid parameter from the following list:", parametersList)

        queriesWithBestHit = {}
        for queryGeneLocusTag in results:
            queriesWithBestHit[queryGeneLocusTag] = {}
            if parameter == "e_value":
                bestHitValue = 10000000
            else:
                bestHitValue = 0

            for hitsGeneLocusTag in results[queryGeneLocusTag]:
                hit = results[queryGeneLocusTag][hitsGeneLocusTag]
                if parameter == "e_value":
                    if float(hit[parameter]) < bestHitValue:
                        queriesWithBestHit[queryGeneLocusTag] = {hitsGeneLocusTag : hit}
                        bestHitValue = float(hit[parameter])
                else:
                    if float(hit[parameter]) > bestHitValue:
                        queriesWithBestHit[queryGeneLocusTag] = {hitsGeneLocusTag : hit}
                        bestHitValue = float(hit[parameter])

        return queriesWithBestHit




    ##### INTERNAL AUXILIAR METHODS #####

    def __dumpJSON(self, data, jsonFileName):

        with open(jsonFileName, "w") as output:
            json.dump(data, output)



    def __findUnilateralOverlappingItemsFromTwoCollections(self, collection1, collection2):

        result = []
        for item in collection1:
            if item in collection2:
                result.append(item)

        return result


    def __findUnilateralNonOverlappingItemsFromTwoCollections(self, collection1, collection2):

        result = []
        for item in collection1:
            if item not in collection2:
                result.append(item)

        return result




    ##### GETTERS #####

    def getEvalueThreshold(self):

        return self.__evalueThreshold

    def getTargetCoverageThreshold(self):

        return self.__targetCoverageThreshold

    def getQueryCoverageThreshold(self):

        return self.__queryCoverageThreshold

    def getAlignmentLengthThreshold(self):

        return self.__alignmentLengthThreshold

    def getBitScoreThreshold(self):

        return self.__bitScoreThreshold

    def getIdentityThreshold(self):

        return self.__identityThreshold

    def getScoreThreshold(self):

        return self.__scoreThreshold

    def getOutputDirectory(self):

        return self.__outputDirectory

    def getBigBlastResults(self):

        return self.__bigBlastResults

    def getBigBlastComplementaryResults(self):

        return self.__bigBlastComplementaryResults


    ##### SETTERS #####

    def setEvalueThreshold(self, value):

        valueProcessed = str(value).lower()
        self.__evalueThreshold = float(valueProcessed)

    def setTargetCoverageThreshold(self, value):

        self.__targetCoverageThreshold = float(value)

    def setQueryCoverageThreshold(self, value):

        self.__queryCoverageThreshold = float(value)

    def setAlignmentLengthThreshold(self, value):

        self.__alignmentLengthThreshold = float(value)

    def setBitScoreThreshold(self, value):

        self.__bitScoreThreshold = float(value)

    def setIdentityThreshold(self, value):

        self.__identityThreshold = float(value)

    def setScoreThreshold(self, value):

        self.__scoreThreshold = float(value)

    def setOutputDirectory(self, value):

        self.__outputDirectory = str(value)

    def setThresholds(self, evalueThreshold = "", targetCoverageThreshold = "", queryCoverageThreshold = "", alignmentLengthThreshold = "",
                      bitScoreThreshold = "", IdentityThreshold = "", ScoreThreshold = ""):

        if evalueThreshold:
            self.setEvalueThreshold(evalueThreshold)

        if targetCoverageThreshold:
            self.setTargetCoverageThreshold(targetCoverageThreshold)

        if queryCoverageThreshold:
            self.setQueryCoverageThreshold(queryCoverageThreshold)

        if alignmentLengthThreshold:
            self.setAlignmentLengthThreshold(alignmentLengthThreshold)

        if bitScoreThreshold:
            self.setBitScoreThreshold(bitScoreThreshold)

        if IdentityThreshold:
            self.setIdentityThreshold(IdentityThreshold)

        if ScoreThreshold:
            self.setScoreThreshold(ScoreThreshold)


    def setBigBlastResults(self, data):

        self.__bigBlastResults = data


    def setBigBlastComplementaryResults(self, data):

        self.__bigBlastComplementaryResults = data








