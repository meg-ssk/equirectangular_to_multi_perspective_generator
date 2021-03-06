import os
import numpy as np
import cv2
import yaml
import tqdm
import py360convert


def main():
    # read parameters in config file
    with open('./config/config.yaml') as file:
        cfg = yaml.safe_load(file)
    
    # read equirectangular
    eqr_img = cv2.imread("./input/" + cfg['input_image_file_path'])
    
    # make output directory
    output_directory = "./output/" + cfg['output_directory'] + "/"
    os.makedirs(output_directory, exist_ok=True)
    
    #longitude_degree, latitude_degree = 0, 0
    longitude_delta, latitude_delta = cfg['longitude_delta'], cfg['latitude_delta']
    fov_degree = (cfg['fov'], cfg['fov'])
    perspective_image_shape = (cfg['perspective_image_height'], cfg['perspective_image_width'])
    
    # generate perspective images by iteration with different longitude and latitude
    for longitude_degree in tqdm.tqdm(np.arange(0, 360, longitude_delta)):
        for latitude_degree in tqdm.tqdm(np.arange(0, 360, latitude_delta)):
            perspec_image = generate_perpective_from_equirectangular(eqr_img, fov_degree, longitude_degree, latitude_degree, perspective_image_shape)
            cv2.imwrite(output_directory + "lat-" + str(latitude_degree) + "_lon-" + str(longitude_degree) + ".png", perspec_image)
            
    print("finish.")
    
    return

def generate_perpective_from_equirectangular(eqr_img, fov_degree, longitude_degree, latitude_degree, perspective_image_shape):
    """_summary_

    Args:
        eqr_img (ndarray): equirectangular image in numpy array
        fov_degree (float): field of view in degree for geneating perspective image
        longitude_degree (float): longitude (azimuthal angle) in degree
        latitude_degree (float): latitude (polar angle) in degree
        perspective_image_shape (tuple): shape of the generated perspective image with (height, width)

    Returns:
        ndarray: perspective image in numpy array
    """
    return py360convert.e2p(eqr_img, fov_degree, longitude_degree, latitude_degree, perspective_image_shape)

if __name__ == "__main__":
    main()
    