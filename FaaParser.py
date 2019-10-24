import re


class FaaParser:


    ###### CONSTRUCTOR ######

    def __init__(self):

        self.geneLocusTag = []
        self.faa = ""
        self.outputDirectory = ""


    def readFaa(self, faaFile):

        with open(faaFile, "r") as input:
            file = input.readlines()

        output = []
        for line in file:
            lineProcessed = line.replace("\n", "")
            output.append(lineProcessed)
            if ">" in lineProcessed:
                locusTag = lineProcessed.split(" ")[0].replace(">", "")
                self.geneLocusTag.append(locusTag)


    def writeGeneLocusTag(self, fileName):

        geneLocusTagForWriting = self.insertLineBreaksInList(self.geneLocusTag)

        with open(self.outputDirectory + fileName, "w") as output:
            output.writelines(geneLocusTagForWriting)


    def insertLineBreaksInList(self, list):

        res = []
        for item in list:
            res.append(item+"\n")

        return res


    def getFAA(self):

        return self.faa


    def getGeneLocusTag(self):

        return self.geneLocusTag

    def getOutputDirectory(self):

        return self.outputDirectory


    def setGeneLocusTag(self, value):

        self.geneLocusTag = value


    def setFAA(self, faa):

        self.faa = str(faa)


    def setOutputDirectory(self, value):

        self.outputDirectory = str(value)





