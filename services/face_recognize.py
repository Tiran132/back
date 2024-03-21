import face_recognition
import pickle
from PIL import Image, ImageDraw


def encoded_faces(files):
    encodings = []
    print(len(files))
    for file in files:
        face_img = face_recognition.load_image_file(file.file)
        face_encoding = face_recognition.face_encodings(face_img)
        if len(face_encoding) >  1:
            continue
        else:
            encodings.append(face_encoding)
    print(len(encodings))
    return pickle.dumps(encodings)

def encoded_face(file):
    encodings = []
    face_img = face_recognition.load_image_file(file.file)
    face_encoding = face_recognition.face_encodings(face_img)[0]
    encodings.append(face_encoding)
    return pickle.dumps(encodings)


def compare_faces(first_face, second_face):
    # photos = pickle.loads(second_face)
    # print(pickle.loads(first_face)[0])
    print(pickle.loads(second_face)[0])
    print(pickle.loads(first_face)[0])
    result = face_recognition.compare_faces([pickle.loads(second_face)[0]], pickle.loads(first_face)[0])
    print(result)
    return result
    # return True

    # pil_img = Image.fromarray(face_img)
    # draw_img = ImageDraw.Draw(pil_img)

    # for (top, right, bottom, left) in face_location:
    #     draw_img.rectangle(((left,top),(right,bottom)), outline=(255,255,0), width=4)
    # del draw_img
    # pil_img.save(f"img/{file.filename}")