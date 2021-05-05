from joblib import load

filename = '/content/drive/MyDrive/Programarea-mea/NLP/Project/Toxic_model.pk'
model = load(filename)

def is_offensive(text):
    return model.predict(text)