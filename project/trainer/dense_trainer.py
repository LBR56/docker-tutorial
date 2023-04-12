import tensorflow as tf

class DenseTrainer():
    def __init__(self, data, model:tf.keras.Model):
        self.data = data
        self.model = model

    def fit(self):
        self.model.fit(self.data[0], self.data[1])
