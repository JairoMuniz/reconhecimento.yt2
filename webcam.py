import numpy as np
import face_recognition as fr
import cv2
import pyttsx3
from engine import get_rostos

rostos_conhecidos, nomes_dos_rostos = get_rostos()

engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PT-BR_MARIA_11.0')  # Ajuste para a voz feminina em português

video_capture = cv2.VideoCapture(0)
mensagem_falada = False  # Variável de controle

while True:
    ret, frame = video_capture.read()

    # Converta o frame para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtenha as localizações dos rostos
    localizacao_dos_rostos = fr.face_locations(rgb_frame)
    rosto_desconhecido = fr.face_encodings(rgb_frame, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecido):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print(resultados)

        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)

        melhor_id = np.argmin(face_distances)
        if resultados[melhor_id]:
            nome = nomes_dos_rostos[melhor_id]
        else:
            nome = "Desconhecido"

        # Desenhe um retângulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Desenhe um retângulo abaixo do rosto
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Adicione o nome abaixo do rosto
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        print(f"Nome reconhecido: {nome}")  # Mensagem de depuração

        if nome == "Jairo" and not mensagem_falada:
            print("Falando mensagem de boas-vindas...")  # Mensagem de depuração
            engine.say("Bem-vindo ao seu ambiente de trabalho, Jairo")
            engine.runAndWait()
            mensagem_falada = True  # Atualize a variável de controle

    cv2.imshow('webcam_facerecognition', frame)

    # Verifique se a tecla 'q' ou 'p' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('p')]:
        break

video_capture.release()
cv2.destroyAllWindows()
