import sys, pathlib
sys.path.append(pathlib.Path().absolute().as_posix().replace("tanh_activated", ""))
from base.gan import Base_Generative_Adversarial_Network

class Tanh_Activated_Generative_Adversarial_Network(Base_Generative_Adversarial_Network):
    
    def get_scaled_pixel_range(self):
        return (-1, 1)

    def get_activation_function(self):
        return 'tanh'

if __name__ == '__main__':
    gan = Tanh_Activated_Generative_Adversarial_Network()
    gan.run()