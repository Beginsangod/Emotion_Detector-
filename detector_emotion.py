import csv

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

with open('FEEL.csv', '+r', encoding='utf-8') as f:
    data = csv.DictReader(f)

def detector_emotion(text):
    for i,word in enumerate(text):
        for ligne in data:
            pattern = ligne["word"].split(' ')
            n = len(pattern)
            if n > 1:
                for j in range(0, n-1):
                    if text[i+j] == pattern[j]:
            else:
                if


if __name__ == "__main__":
    text = input("Décrivez moi votre Feeling votre ressenti actuelle: \n ").split(' ')