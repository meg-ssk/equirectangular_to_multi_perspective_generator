# equirectangular_to_multi_perspective_generator
## Description
The code in this repository generates multiple perspective images from a single equirectangular image with a slightly different viewing direction.

**Input**

![EQR image](assets/images_for_README/equirectangular.png)

**Outputs**

![perspective images](assets/images_for_README/concat.png)


## Installation
Develop environment can be installed by:
```
make install_poetry
poetry install
```

I have also prepared `requirements.txt`,
so if you would like to use it, run the following command:
```
pip install -r requirements.txt
```

## Usage
```
make main
```
or
```
poetry run python src/main.py
```
or
```
python src/main.py
```

## Configulation
If you want to change the calculation conditions, edit the parameters described in　`./config/config.yaml`.
Each parameter is described below:

- input_image_file_path:
    - Path to input image under `./input`. 
- output_directory:
    - Name of the directory in which the output images will be saved under `./output/`.
- fov:
    - Field of view in degree.
- longitude_delta:
    - Step size of longitude (azimuthal angle) in degree.
- latitude_delta: 
    - Step size of latitude (polar angle) in degree.
- perspective_image_height / perspective_image_width:
    - Image size of generated perspective image.

## Motivations
When equirectangular images taken with a omnidirectional camera are used for technologies developed from perspective images, such as object detection, super-resolution and 3D reconstruction, it is common to use cube mapping.
However, cube mapping method is susceptible to image 'cuts' that occur at the edges of the cube.
If the issues of computational cost and time can be ignored, the author believe that the method of generating perspective images for various orientations generated from the code in this repository can to some extent address the ‘cuts’ at the edges of the cube.

## References
- https://github.com/sunset1995/py360convert

## Sample image data source
I used free image from the following URL as sample image:
- https://pixexid.com/image/oum1nug-a-boat-is-docked-next-to-a-body-of-water
