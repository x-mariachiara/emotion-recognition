import sys

emozioni_corrisponenti = dict([(0, "neutrale"), (1, "rabbia"), (2, "disprezzo"), (3, "disgusto"), (4, "paura"), (5, "felicità"), (6, "tristezza"), (7, "sorpresa")])

path = "emozioni/S005_001_00000011_emotion.txt"
path_foto = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/CK+-20210310T155959Z-001/CK+/cohn-kanade-images/cohn-kanade-images/"
path_emo = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/CK+-20210310T155959Z-001/CK+/Emotion_labels/Emotion"

def restituisci_emozione(path: str):
    file = open(path, "r")
    etichetta = file.read()
    etichetta = int(float(etichetta))
    print(emozioni_corrisponenti[etichetta])

def organizza_cartelle():
    print("ciao")

if __name__ == "__main__":
    restituisci_emozione(path)