import sys
import os
import shutil

emozioni_corrisponenti = dict([(0, "neutrale"), (1, "rabbia"), (2, "disprezzo"), (3, "disgusto"), (4, "paura"), (5, "felicità"), (6, "tristezza"), (7, "sorpresa")])

path_dataset_labbelled = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/dataset_labbelled"
path_foto = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/CK+-20210310T155959Z-001/CK+/cohn-kanade-images/cohn-kanade-images/"
path_emo = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/CK+-20210310T155959Z-001/CK+/Emotion_labels/Emotion/"

def crea_cartelle(path: str):
    os.chdir(path)
    for emozione in emozioni_corrisponenti.values():
        os.mkdir(emozione)

def recupera_cose(path: str):
    os.chdir(path)
    for c in os.listdir("."):
        for c_interna in os.listdir(c):
            if len(os.listdir(c + "/" + c_interna)) > 0:
                nome_file = os.listdir(c + "/" + c_interna)[0]
                contenuto = open(c + "/" + c_interna + "/" + nome_file, "r")
                emozione = restituisci_emozione(contenuto)
                print(nome_file, emozione)
                riempi_cartelle(path_foto, nome_file, emozione, path_dataset_labbelled)

def riempi_cartelle(path_img:str, nome_file:str, emozione:str, path_labe:str):
    lista_split = nome_file.split(sep="_")
    path_completo = path_img + "/" + lista_split[0] + "/" + lista_split[1] + "/"
    nome_immagine = lista_split[0] + "_" + lista_split[1] + "_" + lista_split[2] + ".png"
    shutil.copy(path_completo + nome_immagine, path_labe + "/" + emozione)

def restituisci_emozione(file):
    etichetta = file.read()
    etichetta = int(float(etichetta))
    return emozioni_corrisponenti[etichetta]


if __name__ == "__main__":
    recupera_cose(path_emo)