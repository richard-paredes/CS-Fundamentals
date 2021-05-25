import sys, pathlib
sys.path.append(pathlib.Path().absolute().as_posix().replace("reduced_latent_space", ""))
from base.gan import Base_Generative_Adversarial_Network

class Reduced_Latent_Space_Generative_Adversarial_Network(Base_Generative_Adversarial_Network):

    def get_latent_dimensions(self):
        return 50
    
if __name__ == '__main__':
    gan = Reduced_Latent_Space_Generative_Adversarial_Network()
    gan.run()