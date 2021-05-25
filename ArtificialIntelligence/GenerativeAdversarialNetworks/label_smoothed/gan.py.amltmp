import sys, pathlib
sys.path.append(pathlib.Path().absolute().as_posix().replace("label_smoothed", ""))
from base.gan import Base_Generative_Adversarial_Network
from numpy import full

class Label_Smoothed_Generative_Adversarial_Network(Base_Generative_Adversarial_Network):

    def get_labels_for_real_samples(self, n_samples):
        return full((n_samples, 1), 0.9)

if __name__ == '__main__':
    gan = Label_Smoothed_Generative_Adversarial_Network()
    gan.run()