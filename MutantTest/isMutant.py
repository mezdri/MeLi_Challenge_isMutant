import pandas as pd

class IsMutant:
    def __init__(self):
        self.charactersAllowed = ['A', 'T', 'C', 'G']
        self.sequences = ['AAAA', 'TTTT', 'CCCC', 'GGGG']
        self.characterValidate = 'X'
        self.mutantFlag = 0

    def isMutant(self, dna):
        dnaNew = [[y if y in self.charactersAllowed else self.characterValidate for y in x] for x in dna]
        pdDataFrame = pd.DataFrame(dnaNew)
        checkCharacters = pdDataFrame[(pdDataFrame == self.characterValidate).any(1)].stack()[
            lambda x: x == self.characterValidate].unique()

        if len(checkCharacters) > 0:
            raise Exception('Input data have some characters incorrect, please only use A,T,C or G')

        isMutant = self.checkRows(dnaNew)
        if not isMutant:
            isMutant = self.checkDiagonals(dnaNew)
        if not isMutant:
            isMutant = self.checkColumns(pdDataFrame)

        return isMutant

    def checkRows(self, dna):
        for row in dna:
            rowJoin = ''.join(row)
            self.searchSequence(rowJoin)
        return True if self.mutantFlag > 0 else False

    def checkDiagonals(self, dna):
        for diagonal in self.get_diagonals(dna):
            if len(diagonal) > 3:
                diagonal = ''.join(diagonal)
                self.searchSequence(diagonal)
        return True if self.mutantFlag > 0 else False

    def checkColumns(self, df):
        for i in range(0, len(df)):
            columnJoin = ''.join(df[i].to_list())
            self.searchSequence(columnJoin)
        return True if self.mutantFlag > 0 else False

    def searchSequence(self, joinData):
        for sequence in self.sequences:
            self.mutantFlag += joinData.find(sequence) != -1 or 0
            if self.sequences == 0:
                self.mutantFlag += ''.join(reversed(joinData)).find(sequence) != -1 or 0

    def get_diagonals(self, matrix):
        n = len(matrix)
        for p in range(2 * n - 1):
            yield [matrix[p - q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)]
            yield [matrix[n - p + q - 1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)]




