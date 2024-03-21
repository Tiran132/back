import pickle
import face_recognition


encodings = []
face_img = face_recognition.load_image_file("img/45.jpg")
face_encoding1 = face_recognition.face_encodings(face_img)[0]

face_img = face_recognition.load_image_file("img/48.jpg")
face_encoding2 = face_recognition.face_encodings(face_img)[0]
# print([face_encoding1], face_encoding2)
print(face_recognition.compare_faces([face_encoding1], face_encoding2))
# print(pickle.dumps(encodings))

# a = ([1,2,3,4,5],[1,22,3,34,5])
# b = pickle.dumps(a)
# print(pickle.loads(b))
