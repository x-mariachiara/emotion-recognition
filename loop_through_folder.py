import cv2
import os
from mask import create_mask


#folder_path = "./001"
def loop_cartelle(folder_path, pathdatasetoutput):
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f != ".DS_Store"]
    for i in range(len(images)):
        print("the path of the image is", images[i])
        #image = cv2.imread(images[i])
        #c = c + 1
        create_mask(images[i], pathdatasetoutput)

def main():
    pathdatasetoutput = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/datasetConMascherine"
    try:
        os.mkdir(pathdatasetoutput)
    except FileExistsError:
        pass
    pathdatasetinput = "/media/mariachiara/307EE13523D10A66/TERZO_ANNO/TESI/CK+-20210310T155959Z-001/CK+/cohn-kanade-images/cohn-kanade-images/"
    cartelle_dataset = os.listdir(pathdatasetinput)
    cartelle_dataset.remove(".DS_Store")
    #print(cartelle_dataset)
    #per ogni cartella dobbiamo prenderci tutte le cartelle con le immagini e per ogni cartella con le immagini dobbiamo mettere la mascherina
    for cartella in cartelle_dataset:
        imageDirs = os.listdir(pathdatasetinput + cartella)
        try:
            imageDirs.remove(".DS_Store")
        except ValueError:
            pass
        #print(imageDirs)

        for cartellaImg in imageDirs:
            loop_cartelle(pathdatasetinput + cartella + "/" + cartellaImg, pathdatasetoutput)



if __name__ == '__main__':
    main()

