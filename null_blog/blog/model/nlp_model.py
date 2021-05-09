from joblib import load

from .preprocessing import TextTransformer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import os

# instanciate a transformer for preprocessing text
transformer = TextTransformer(stopwords=['and', 'for', 'in', 'about', 'for', 'as', 'the'], stemmer=PorterStemmer())

# unpacking the model
path_to_model = os.path.join(os.getcwd(), r'blog\model\model.pkl')
model = load(path_to_model)

# function used in views to check if text content is offensive
def is_offensive(text):
    text = transformer.transform([text])

    return model.predict(text)
