import os,sys
from options.test_options import TestOptions
from models import create_model
from util import util
from PIL import Image
import pygame
from data.base_dataset import get_transform
sys.path.append(os.getcwd())

try:
    import wandb
except ImportError:
    print('Warning: wandb package cannot be found. The option "--use_wandb" will result in error.')


if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 0
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
    ######################
    opt.model = 'test'
    opt.no_flip = True
    opt.dataset_mode = 'single'
    ##########################
    # dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers

    if opt.eval:
        model.eval()
    
    pygame.init()
    text = u"{0}".format('诺')
    font = pygame.font.Font("./msyh.ttf", 256)
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
    A_path = os.path.join(os.getcwd(), './results/output/H'+ str(text) +'.png')
    pygame.image.save(rtext, A_path)

    A_img = Image.open(A_path).convert('RGB')
    transform = get_transform(opt)
    A = transform(A_img)
    A = A.unsqueeze(0)
    data = {'A': A, 'A_paths': A_path}

    model.set_input(data)  # unpack data from data loader
    model.test()           # run inference
    visuals = model.get_current_visuals()  # get image results
    
    for label, im_data in visuals.items():
        if label == 'fake' :
            im = util.tensor2im(im_data)
            save_path = os.path.join(os.getcwd(), './results/output/J'+ str(text) +'.png')
            util.save_image(im, save_path)
        

