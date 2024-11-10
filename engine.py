import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if((len(rostos) > 0)):
        return True, rostos
    return False, []


def get_rostos():

    rostos_conhecidos = []
    nomes_dos_rostos = []


    jairo5 = reconhece_face("foto5.jpg")
    if(jairo5[0]):
        rostos_conhecidos.append(jairo5[1][0])
        nomes_dos_rostos.append("Jairo")

    galeguinho1 = reconhece_face("galeguinho.jpg")
    if(galeguinho1[0]):
        rostos_conhecidos.append(galeguinho1[1][0])
        nomes_dos_rostos.append("galeguinho")

    return rostos_conhecidos, nomes_dos_rostos