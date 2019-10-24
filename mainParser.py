import json


class BigBlastParser:

    ###### CONSTRUCTOR ######

    def __init__(self):


        self.bigBlastResults = {} # store first BLAST of BIDIRECTIONAL BEST HITS SEARCH in a dictionary
        self.bigBlastComplementaryResults = {} # store second BLAST of BIDIRECTIONAL BEST HITS SEARCH in a dictionary
        self.evalueThreshold = 100.0 # evalue threshold is the only maximum threshold
        self.targetCoverageThreshold = 0.0 # all other thresholds are intended to be minimum thresholds
        self.queryCoverageThreshold = 0.0
        self.alignmentLengthThreshold = 0.0
        self.bitScoreThreshold = 0.0
        self.identityThreshold = 0.0
        self.scoreThreshold = 0.0
        self.outputDirectory = ""  # directory where analysis results will be stored


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
            self.bigBlastComplementaryResults = data

        elif complementary == False:
            self.bigBlastResults = data

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")



    def head(self, complementary = False):
        """
        returns the value of the first key stored in the bigBlastParser results
        :param complementary: Boolean to work with the "normal" or "complementary" results of Bidirectional Best Hits Search BLAST
        :return: value of first key in bigBlastParser results
        """

        if complementary == True:
            results = self.bigBlastComplementaryResults

        elif complementary == False:
            results = self.bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        firstKey = list(results.keys())[0]
        return results[firstKey]


    def tail(self, complementary = False):

        if complementary == True:
            results = self.bigBlastComplementaryResults

        elif complementary == False:
            results = self.bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        firstKey = list(results.keys())[-1]
        return results[firstKey]


    def getHitsByQuery(self, query, complementary = False):

        if complementary == True:
            results = self.bigBlastComplementaryResults

        elif complementary == False:
            results = self.bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        return results[query]


    def getHitsByThresholds(self, complementary = False):

        if complementary == True:
            results = self.bigBlastComplementaryResults

        elif complementary == False:
            results = self.bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        hitsByThresholds = {}
        for queryGeneLocusTag in results:
            hitsByThresholds[queryGeneLocusTag] = {}
            for hitsGeneLocusTag in results[queryGeneLocusTag]:

                hitMeetsThreshold = True
                hit = results[queryGeneLocusTag][hitsGeneLocusTag]
                for parameters in hit:

                    if parameters == "score" and float(hit[parameters]) < self.scoreThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "target_coverage" and float(hit[parameters]) < self.targetCoverageThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "align_len" and float(hit[parameters]) < self.alignmentLengthThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "bitScore" and float(hit[parameters]) < self.bitScoreThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "identity" and float(hit[parameters]) < self.identityThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "query_coverage" and float(hit[parameters]) < self.queryCoverageThreshold:
                        hitMeetsThreshold = False
                        break

                    elif parameters == "e_value" and float(hit[parameters]) > self.evalueThreshold:
                        hitMeetsThreshold = False
                        break


                if hitMeetsThreshold:
                    hitsByThresholds[queryGeneLocusTag][hitsGeneLocusTag] = hit

        return hitsByThresholds

    def getBestHit(self, queryGeneLocusTag, results, parameter):

        bestHit = None
        bestParameter = None
        for hitsGeneLocusTag in results[queryGeneLocusTag]:
            hit = results[queryGeneLocusTag][hitsGeneLocusTag]

            if parameter == 'e_value':

                if bestParameter == None:
                    bestParameter = float(hit['e_value'])
                    bestHit = hit
                elif :


        return bestHit

    def getHitsByParameter(self, complementary = False, parameter = 'evalue'):

        if complementary == True:
            results = self.bigBlastComplementaryResults

        elif complementary == False:
            results = self.bigBlastResults

        else:
            raise Exception("complementary argument must be a boolean, you provided a " + str(type(complementary)) +" instead")

        HitsByParameter={}


    def writeResultsinJson(self, data, jsonFileName):

        if not self.outputDirectory:
            raise Exception("Please set a working directory before writing files")

        jsonFileNameProcessed = str(jsonFileName)
        if not jsonFileNameProcessed.endswith(".json"):
            jsonFileNameProcessed += ".json"

        self.__dumpJSON(data, self.outputDirectory+jsonFileNameProcessed)


    def countQueriesWithHits(self, data):

        count = 0
        for query in data:
            if len(data[query])>0:
                count += 1

        return count




    ##### INTERNAL AUXILIAR METHODS #####

    def __dumpJSON(self, data, jsonFileName):

        with open(jsonFileName, "w") as output:
            json.dump(data, output)



    ##### GETTERS #####

    def getEvalueThreshold(self):

        return self.evalueThreshold

    def getTargetCoverageThreshold(self):

        return self.targetCoverageThreshold

    def getQueryCoverageThreshold(self):

        return self.queryCoverageThreshold

    def getAlignmentLengthThreshold(self):

        return self.alignmentLengthThreshold

    def getBitScoreThreshold(self):

        return self.bitScoreThreshold

    def getIdentityThreshold(self):

        return self.identityThreshold

    def getScoreThreshold(self):

        return self.scoreThreshold

    def getOutputDirectory(self):

        return self.outputDirectory


    ##### SETTERS #####

    def setEvalueThreshold(self, value):

        valueProcessed = str(value).lower()
        self.evalueThreshold = float(valueProcessed)

    def setTargetCoverageThreshold(self, value):

        self.targetCoverageThreshold = float(value)

    def setQueryCoverageThreshold(self, value):

        self.queryCoverageThreshold = float(value)

    def setAlignmentLengthThreshold(self, value):

        self.alignmentLengthThreshold = float(value)

    def setBitScoreThreshold(self, value):

        self.bitScoreThreshold = float(value)

    def setIdentityThreshold(self, value):

        self.identityThreshold = float(value)

    def setScoreThreshold(self, value):

        self.scoreThreshold = float(value)

    def setOutputDirectory(self, value):

        self.outputDirectory = str(value)






