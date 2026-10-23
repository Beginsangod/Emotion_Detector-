import csv
import spacy

nlp = spacy.load('fr_core_news_sm')

subjet_score =  {
    "positif"  : 0,
    "negatif"  : 0,
    "happy"    : 0,
    "sad"      : 0,
    "angry"    : 0,
    "fear"     : 0,
    "neutral"  : 0,
    "disgust"  : 0,
    "surprise" : 0 
}

def infinitif_verbe(text):
    doc = nlp(text)

    mots_normalize = []
    for e in doc:
        mots_normalize.append(e.lemma_)

    return mots_normalize

def parse_expression(text, pattern):
    val = False
    for i,word in enumerate(pattern):
        if word == text[i]:
            val = True 
        else:
            return False
    return val


def detector_emotion(text):
    isnegative = 1

    for i, word in enumerate(text):
        with open('FEEL.csv', '+r', encoding='utf-8') as f:
            data = csv.DictReader(f, delimiter=";")

            for ligne in data:
                pattern = ligne["word"].split(' ')
                n = len(pattern)
                test = text[i: i+n]  #valeur à tester pour vérifier la présence de l'expression
                if i + n <= len(text):
                    test = text[i : i + n]
                    if parse_expression(test, pattern):
                        if ligne ["polarity"] == "positive":
                            subjet_score["positif"] += 1 * isnegative
                        else: 
                            subjet_score["negatif"] += 1 * isnegative

                        #remplissage du tableau du sujet
                        subjet_score["sad"] += int(ligne["sadness"]) * isnegative
                        subjet_score["happy"] += int(ligne["joy"]) * isnegative
                        subjet_score["fear"] += int(ligne["fear"]) * isnegative
                        subjet_score["disgust"] += int(ligne["disgust"]) * isnegative
                        subjet_score["angry"] += int(ligne["anger"]) * isnegative
                        subjet_score["surprise"] += int(ligne["surprise"]) * isnegative
                        isnegative = 1
                        i = i+n-1
                    elif word == "ne":
                        isnegative = -1

            if subjet_score["positif"] < 0:
               subjet_score["negatif"] += -subjet_score["positif"]
               subjet_score["positif"] = 0

            if subjet_score["negatif"] < 0:
                subjet_score["positif"] += -subjet_score["negatif"]
                subjet_score["negatif"] = 0

            if subjet_score["sad"] < 0:
                subjet_score["happy"] += -subjet_score["sad"]
                subjet_score["sad"] = 0  

            if subjet_score["angry"] < 0:
                subjet_score["neutral"] += -subjet_score["angry"]
                subjet_score["angry"] = 0

            if subjet_score["fear"] < 0:
                subjet_score["neutral"] += subjet_score["fear"] 
                subjet_score["fear"] = 0

            if subjet_score["disgust"] < 0:
                subjet_score["neutral"] += subjet_score["angry"]
                subjet_score["disgust"] = 0

            if subjet_score["happy"] < 0:
                dominant_emotion = max(subjet_score, subjet_score.get)
                if dominant_emotion == "sad":
                    subjet_score["sad"] = -subjet_score["happy"]
                if dominant_emotion == "angry":
                    subjet_score["angry"] = -subjet_score["happy"]
                if dominant_emotion == "fear":
                    subjet_score["fear"] = -subjet_score["happy"]
                subjet_score["happy"] = 0

            if subjet_score["surprise"] < 0:
                subjet_score["surprise"] = 0

if __name__ == "__main__":
    text = input("Décrivez moi votre Feeling votre ressenti actuelle: \n ").lower()
    text_normalize = infinitif_verbe(text)
    detector_emotion(text_normalize)
    print(subjet_score)