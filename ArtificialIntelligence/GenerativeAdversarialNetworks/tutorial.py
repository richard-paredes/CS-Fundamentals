from keras.datasets.mnist import load_data
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.layers import Dense, Conv2D, Flatten, Dropout, LeakyReLU, Reshape, Conv2DTranspose
# from tensorflow.keras.utils.vis_utils import plot_model
from matplotlib.pyplot import imshow, subplot, axis, show, savefig, close
# import pydot
# import graphviz
from numpy.random import rand, randint, randn
from numpy import expand_dims, zeros, ones, vstack, asfarray
from time import perf_counter


def print_mnist(self):
    (trainX,trainY), (testX, testY) = load_data()
    print('Train', trainX.shape, trainY.shape)
    print('Test', testX.shape, testY.shape)

def plot_mnist(self, trainX):
    for i in range(25):
        subplot(5, 5, 1+i)
        axis('off')
        imshow(trainX[i], cmap='gray')
    show()

def define_discriminator(self, in_shape=(28,28,1)):
    model = Sequential()
    model.add(Conv2D(64, (3,3), strides=(2,2), padding='same', input_shape=in_shape))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.4))
    model.add(Conv2D(64, (3,3), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.4))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))

    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model

def summarize_descriminator(self):
    model = self.define_discriminator()
    model.summary()
    # having issue with keras dependency on graphviz and pydot
    # plot_model(model, to_file='discriminator_plot.png', show_shapes=True, show_layer_names=True)

def scale_pixel(self, pixel_value):
    current_min, new_min = 0, 0
    current_max, new_max = 255, 1

    return (new_max - new_min) * (pixel_value - current_min) / (current_max - current_min) + new_min
    
def load_real_samples(self):
    (trainX, _), (_, _) = load_data()
    X = expand_dims(trainX, axis=-1)
    X = X.astype('float32')
    X = self.scale_pixel(X)
    return X

def get_labels_for_real_samples(self, n_samples):
    return ones((n_samples, 1))

def generate_real_samples(self, dataset, n_samples):
    ix = randint(0, dataset.shape[0], n_samples)
    X = dataset[ix]
    y = self.get_labels_for_real_samples(n_samples)
    return X, y

def generate_fake_samples(self, n_samples):
    X = rand(28*28*n_samples)
    X = X.reshape((n_samples, 28, 28, 1))
    y = zeros((n_samples, 1))
    return X, y

def train_discriminator(self, model, dataset, n_iter=100, n_batch=256):
    half_batch = int(n_batch / 2)
    
    for i in range(n_iter):
        X_real, y_real = self.generate_real_samples(dataset, half_batch)
        _, real_acc = model.train_on_batch(X_real, y_real)
        X_fake, y_fake = self.generate_fake_samples(half_batch)
        _, fake_acc = model.train_on_batch(X_fake, y_fake)
        print('>%d real=%.0f%% fake=%.0f%%' % (i+1, real_acc*100, fake_acc*100))
        
def run_discriminator(self):
    model = self.define_discriminator()
    dataset = self.load_real_samples()
    self.train_discriminator(model, dataset)

def get_activation_function(self):
    return 'sigmoid'

def define_generator(self, latent_dim):
    model = Sequential()
    n_nodes = 128*7*7
    model.add(Dense(n_nodes, input_dim=latent_dim))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Reshape((7,7,128)))
    model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Conv2D(1, (7,7), activation=self.get_activation_function(), padding='same'))
    return model

def summarize_generator(self):
    latent_dim = self.get_latent_dimensions()
    model = self.define_generator(latent_dim)
    model.summary()
    # plot_model(model, to_file='generator_plot.png', show_shapes=True, show_layer_names=True)

def generate_latent_points(self, latent_dim, n_samples):
    x_input = randn(latent_dim * n_samples)
    x_input = x_input.reshape(n_samples, latent_dim)
    return x_input

def generate_fake_samples(self, g_model, latent_dim, n_samples):
    x_input = self.generate_latent_points(latent_dim, n_samples)
    X = g_model.predict(x_input)
    y = zeros((n_samples, 1))
    return X, y

def run_generator(self):
    latent_dim = self.get_latent_dimensions()
    model = self.define_generator(latent_dim)
    n_samples = 25
    X, _ = self.generate_fake_samples(model, latent_dim, n_samples)
    
    for i in range(n_samples):
        subplot(5, 5, 1+i)
        axis('off')
        imshow(X[i, :, :, 0], cmap='gray_r')
    show()

def define_gan(self, g_model, d_model):
    d_model.trainable = False
    model = Sequential()
    model.add(g_model)
    model.add(d_model)
    opt = Adam(lr=0.0002, beta_1=0.5)
    model.compile(loss='binary_crossentropy', optimizer=opt)
    return model

def get_latent_dimensions(self):
    return 100

def summarize_gan(self):
    latent_dim = self.get_latent_dimensions()
    d_model = self.define_discriminator()
    g_model = self.define_generator(latent_dim)
    gan_model = self.define_gan(g_model, d_model)
    gan_model.summary()
    # plot_model(gan_model, to_file='gan_plot.png', show_shapes=True, show_layer_names=True)

def train_gan(self, gan_model, latent_dim, n_epochs=100, n_batch=256):
    for i in range(n_epochs):
        x_gan = self.generate_latent_points(latent_dim, n_batch)
        y_gan = ones((n_batch,1))
        gan_model.train_on_batch(x_gan, y_gan)

def print_formatted_time(self, start, end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

def train(self, g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=256):
    bat_per_epo = int(dataset.shape[0] / n_batch)
    half_batch = int(n_batch / 2)
    total_start = perf_counter()
    decade_start = perf_counter()
    
    for i in range(n_epochs):
        for j in range(bat_per_epo):
            X_real, y_real = self.generate_real_samples(dataset, half_batch)
            X_fake, y_fake = self.generate_fake_samples(g_model, latent_dim, half_batch)
            X, y = vstack((X_real, X_fake)), vstack((y_real, y_fake))
            d_loss, _ = d_model.train_on_batch(X, y)
            X_gan = self.generate_latent_points(latent_dim, n_batch)
            y_gan = ones((n_batch, 1))
            g_loss = gan_model.train_on_batch(X_gan, y_gan)
            print('>%d, %d/%d, d=%.3f, g=%.3f' % (i+1, j+1, bat_per_epo, d_loss, g_loss))
        
        if (i+1) % 10 == 0:
            decade_end = perf_counter()
            self.summarize_performance(i, g_model, d_model, dataset, latent_dim)
            self.print_formatted_time(decade_start, decade_end)
            decade_start = perf_counter()
    
    total_end = perf_counter()
    self.print_formatted_time(total_start, total_end)
        
def summarize_performance(self, epoch, g_model, d_model, dataset, latent_dim, n_samples=100):
    X_real, y_real = self.generate_real_samples(dataset, n_samples)
    _, acc_real = d_model.evaluate(X_real, y_real, verbose=0)
    X_fake, y_fake = self.generate_fake_samples(g_model, latent_dim, n_samples)
    _, acc_fake = d_model.evaluate(X_fake, y_fake, verbose=0)
    print('>Accuracy real: %.0f%%, fake: %.0f%%' % (acc_real*100, acc_fake*100))
    save_plot(X_fake, epoch)
    filename = 'generator_model%03d.h5' % (epoch+1)
    g_model.save(filename)

def save_plot(self, examples, epoch, n=10):
    for i in range(n*n):
        subplot(n, n, 1+i)
        axis('off')
        imshow(examples[i, :, :, 0], cmap='gray_r')
    filename = 'generated_plot_e%03d.png' % (epoch+1)
    savefig(filename)
    close()

def run_gan(self):
    latent_dim = self.get_latent_dimensions()
    d_model = self.define_discriminator()
    g_model = self.define_generator(latent_dim)
    gan_model = self.define_gan(g_model, d_model)
    dataset = self.load_real_samples()
    self.train(g_model, d_model, gan_model, dataset, latent_dim)

def generate_latent_points(latent_dim, n_samples):
    x_input = randn(latent_dim*n_samples)
    x_input = x_input.reshape(n_samples, latent_dim)
    return x_input

def show_plot(examples, n):
    for i in range(n*n):
        subplot(n, n, 1+i)
        axis('off')
        imshow(examples[i, :, :, 0], cmap='gray_r')
    show()

def generate_multiple_images():
    try:
        epochs_trained = 100
        model = load_model(f'generator_model_{epochs_trained}.h5')
        latent_points = generate_latent_points(100, 25)
        X = model.predict(latent_points)
        show_plot(X, 5)
    except IOError as e:
        print("File with the generator model doesn't exist.")
    except Exception as e:
        print(e.message)

def generate_single_image():
    try:
        epochs_trained = 100
        model = load_model(f'generator_model_{epochs_trained}.h5')
        vector = asfarray([[0.0 for _ in range(100)]])
        X = model.predict(vector)
        imshow(X[0, :, :, 0], cmap='gray_r')
        show()
    except IOError as e:
        print("File with the generator model doesn't exist.")
    except Exception as e:
        print(e.message)