import pandas as pd


class FaaParser:


    ###### CONSTRUCTOR ######

    def __init__(self):

        self.__geneLocusTag = []
        self.__outputDirectory = ""
        self.__faaContents = {}


    def readFaa(self, faaFile):

        with open(faaFile, "r") as input:
            file = input.readlines()

        output = []
        sequence = ""
        locusTag = ""
        firstLine = True

        for line in file:
            lineProcessed = line.replace("\n", "")
            output.append(lineProcessed)
            if ">" in lineProcessed:
                if not firstLine:
                    self.__faaContents[locusTag]["Sequence"] = sequence
                locusTag = lineProcessed.split(" ")[0].replace(">", "")
                product = " ".join(lineProcessed.split(" ")[1:]).split(" [")[0]
                self.__geneLocusTag.append(locusTag)
                self.__faaContents[locusTag] = {"Product" : product, "Sequence" : ""}
                sequence = ""

            elif line == file[-1]:
                self.__faaContents[locusTag]["Sequence"] = sequence

            else:
                sequence += lineProcessed
                firstLine = False




    def writeGeneLocusTag(self, fileName):

        geneLocusTagForWriting = self.insertLineBreaksInList(self.__geneLocusTag)

        with open(self.__outputDirectory + fileName, "w") as output:
            output.writelines(geneLocusTagForWriting)


    def insertLineBreaksInList(self, list):

        res = []
        for item in list:
            res.append(item+"\n")

        return res

    def exportToCSV(self, fileName):

        faaData = self.getFaaContents()
        dataframeHeader = ["GeneIdentifier", "Product", "Sequence"]
        dataframeBody = []

        for gene in faaData:

            product = faaData[gene]["Product"]
            sequence = faaData[gene]["Sequence"]
            dataframeBody.append([gene, product, sequence])

        dataframe = pd.DataFrame(data = dataframeBody, columns = dataframeHeader)

        if not fileName.endswith(".csv"):
            dataframe.to_csv(fileName + ".csv", index = False)
        else:
            dataframe.to_csv(fileName, index = False)






    def getFaaContents(self):

        return self.__faaContents


    def getGeneLocusTag(self):

        return self.__geneLocusTag

    def getOutputDirectory(self):

        return self.__outputDirectory


    def setGeneLocusTag(self, value):

        self.__geneLocusTag = value


    def setFaaContents(self, faa):

        self.__faaContents = str(faa)


    def setOutputDirectory(self, value):

        self.__outputDirectory = str(value)





