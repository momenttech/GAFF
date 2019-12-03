# from textAnalyser import spacy

# nlp = spacy.load('fr_fasttext_lg')

def checkWordInDic(nlp, word1, word2):

    if nlp.vocab.has_vector(word2):
        # print("RAS")
        if word1 != word2:
            dicoPath = "dictionnaire/wordrow.txt"
            file = open(dicoPath, "a")
            file.write("'" + word1 + "': '" + word2 + "'")
            file.write("\n")
        return True

    else:
        # print("real error generate")
        return False