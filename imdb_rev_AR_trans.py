import numpy as np
#from translate import Translator
#import tensorflow as tf
import tensorflow_datasets as tfds
from googletrans import Translator

tr = Translator()
word = "This is a very good dog"
tr.translate( word,  src="en", dest="ar").text


# Collecting corpus from imdb
imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
train_data, test_data = imdb['train'], imdb['test']


# train_data, test_data = imdb['train'], imdb['test']
training_sentences = []
training_labels = []
testing_sentences = []
testing_labels = []


# str(s.tonumpy()) is needed in Python3 instead of just s.numpy()
for s,l in train_data:
  training_sentences.append(str(s.numpy()))
  training_labels.append(l.numpy())


for s,l in test_data:
  testing_sentences.append(str(s.numpy()))
  testing_labels.append(l.numpy())


# Refixing data
training_labels_final = np.array(training_labels)
testing_labels_final = np.array(testing_labels)

# Appending the trnslated corpus
train_x = []
train_label = []
test_x = []
test_label = []
data_label = train_x, train_label, test_x, test_label

# for training
import pickle
for i in range( len(training_sentences)):
    try:
        train_x.append(tr.translate(training_sentences[i][2:-1],  src="en", dest="ar").text)
        train_label.append(training_labels_final[i])
        test_x.append(tr.translate(testing_sentences[i][2:-1],  src="en", dest="ar").text)
        test_label.append(testing_labels_final[i])
        pickle.dump( data_label, open( "imdb_arabized.p", "wb" ) )
        print(i)
    except:
        pass
