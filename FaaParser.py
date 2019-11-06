import re


class FaaParser:


    ###### CONSTRUCTOR ######

    def __init__(self):

        self.__geneLocusTag = []
        self.__faa = ""
        self.__outputDirectory = ""


    def readFaa(self, faaFile):

        with open(faaFile, "r") as input:
            file = input.readlines()

        output = []
        for line in file:
            lineProcessed = line.replace("\n", "")
            output.append(lineProcessed)
            if ">" in lineProcessed:
                locusTag = lineProcessed.split(" ")[0].replace(">", "")
                self.__geneLocusTag.append(locusTag)


    def writeGeneLocusTag(self, fileName):

        geneLocusTagForWriting = self.insertLineBreaksInList(self.__geneLocusTag)

        with open(self.__outputDirectory + fileName, "w") as output:
            output.writelines(geneLocusTagForWriting)


    def insertLineBreaksInList(self, list):

        res = []
        for item in list:
            res.append(item+"\n")

        return res


    def getFAA(self):

        return self.__faa


    def getGeneLocusTag(self):

        return self.__geneLocusTag

    def getOutputDirectory(self):

        return self.__outputDirectory


    def setGeneLocusTag(self, value):

        self.__geneLocusTag = value


    def setFAA(self, faa):

        self.__faa = str(faa)


    def setOutputDirectory(self, value):

        self.__outputDirectory = str(value)





