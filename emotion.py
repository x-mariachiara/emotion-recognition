import face_recognition

img = face_recognition.load_image_file("001/S005_001_00000001.png")
img_mask = face_recognition.load_image_file("001-with-mask/S005_001_00000001.png")
print(img)
img_encoding = face_recognition.face_encoding(img)
img_mask_encoding = face_recognition.face_encoding(img_mask)