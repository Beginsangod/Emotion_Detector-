import json
import re

with open('emotion.json', '+r', encoding='utf-8') as f:
    emotion = json.load(f)

happy   = emotion['Happy']
sad     = emotion['Sad']
angry   = emotion['Angry']
fear    = emotion['Fear']
neutral = emotion['Neutral']

subjet_score =  {
    "happy"   : 0,
    "sad"     : 0,
    "angry"   : 0,
    "fear"    : 0,
    "neutral" : 0,
}

def deduct_emotion(s):
    # Trouve la clé qui a la plus grande valeur dans le dictionnaire
    dominant_emotion = max(s, key=subjet_score.get)
    max_score = s[dominant_emotion]

    # (Optionnel) Vérifier si toutes les émotions ont le même score ou si le score est nul
    if list(s.values()).count(max_score) > 1 and max_score != 0:
        print("Soit tu traverses une tempête émotionnelle, soit tes émotions sont mélangées !")
    elif max_score == 0 or dominant_emotion == 'neutral':
        print("Ton propos semble plutôt neutre.")
    elif dominant_emotion == 'happy':
        print("Je sens que votre phrase a une tonalité particulièrement joyeuse !")
    elif dominant_emotion == 'angry':
        print("Je sens une tonalité colérique dans vos propos, en colère je suppose.")
    elif dominant_emotion == 'fear':
        print("Je sens de la peur, ça va ?")
    elif dominant_emotion == 'sad':
        print("Je ressens de la tristesse dans vos mots.")

def parser_word(text):
    words = text
    for w in words:
        if w in ['', '.', '/', '_']:
            words.remove(w)
        else:
            w.lower()
    return words

def Detect_Emotion(text):
    words = parser_word(text)
    isnegate = False
    for word in words:
        if word == "ne" and re.match("n'.", word) or word == "pas":
            isnegate = True    

        if word in happy:
            if isnegate:
                subjet_score['angry'] += 1
                isnegate = False    
            else:
                subjet_score['happy'] += 1
        elif word in sad:
            if isnegate:
                subjet_score['sad'] -= 1
                isnegate = False    
            else:
                subjet_score['sad'] += 1
        elif word in angry:
            if isnegate:
                subjet_score['happy'] += 1
                isnegate = False    
            else:
                subjet_score['angry'] += 1
        elif word in fear:
            if isnegate:
                subjet_score['fear'] -= 1
                isnegate = False    
            else: 
                subjet_score['fear'] += 1
        elif word in neutral:
            subjet_score['neutral'] += 1

    print("\n",subjet_score)
    deduct_emotion(subjet_score)
    subjet_score.clear()
        
        
if __name__ == "__main__":
    text = input("entrer une phrase: \n").split(' ')
    while(1):
        Detect_Emotion(text)
        text = input("\n entrer une autre phrase ou q pour quitter: \n").split(' ')
        if text[0].lower() == 'q':
            break
    print("\n Merci d'avoir testé notre détecteur d'émotion")
