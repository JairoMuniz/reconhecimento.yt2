import face_recognition as fr
from engine import reconhece_face, get_rostos

desconhecido = reconhece_face("desconhecido.jpg")
if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nomes_dos_rostos = get_rostos()
    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

    for i in range(len(rostos_conhecidos)):
        resultado = resultados[i]
        if(resultado):
            print("O rosto de", nomes_dos_rostos[i], "foi reconhecido")
            break

else:
    print("Não foi possível reconhecer rosto algum");