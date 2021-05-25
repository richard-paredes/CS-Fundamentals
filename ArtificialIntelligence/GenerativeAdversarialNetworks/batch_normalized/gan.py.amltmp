import sys, pathlib
sys.path.append(pathlib.Path().absolute().as_posix().replace("batch_normalized", ""))
from base.gan import Base_Generative_Adversarial_Network
from tensorflow.keras.layers import Dense, Conv2D, LeakyReLU, Reshape, Conv2DTranspose, BatchNormalization
from tensorflow.python.keras.models import Sequential

class Batch_Normalized_Generative_Adversarial_Network(Base_Generative_Adversarial_Network):

    def define_generator(self, latent_dim):
        model = Sequential()
        n_nodes = 128*7*7
        model.add(Dense(n_nodes, input_dim=latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Reshape((7,7,128)))
        model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Conv2D(1, (7,7), activation=self.get_activation_function(), padding='same'))
        return model

if __name__ == '__main__':
    gan = Batch_Normalized_Generative_Adversarial_Network()
    gan.run()