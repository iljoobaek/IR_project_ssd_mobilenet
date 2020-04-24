# IR_project_ssd_mobilenet

Original Repo: https://github.com/qfgaohao/pytorch-ssd.git

Folder structure:
home/data/VOCdevkit2007/VOC2007/

    --ImageSets    (contains trainval.txt file with names of train and val images)
    
            --Main
                    
                    --trainval.txt
                    
                    --test.txt
    
    --JPEGImages   (contains all images for training and eval)
    
        --image.jpeg
    
    --Annotations  (contains all annotation files .xml)
    
        --annotation.xml
   
Requirements: Python 3, pytorch, opencv.

Copy over the data folder to your home directory and place the annotation xml files in Annotations folder and Images in JPEGImages folder.

Data Split : 1-8862 images from FLIR training and validation images and 1-3000 images from FLIR video images are used for training and validation of the model and 3001 to 4224 video images are used for testing the trained model and evaluating metrics.

To train: run the start_training.sh script.
