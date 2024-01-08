# MMERB:  Multimodal Dataset for Measuring Marginalized Ethnicity Reporting Bias.

## General information

This dataset was created as part of a project in the course LT2314. The images and original captions are taken from the Flickr8k and MS COCO datasets, and contrasting examples were created using regular expressions. The code used when creating the dataset can be found in [`notebooks/dataset_creation.ipynb`](https://github.com/TomBladsjo/LT-Resources-project/blob/main/notebooks/dataset_creation.ipynb). More details can be found in [the paper](https://github.com/TomBladsjo/LT-Resources-project/blob/main/paper/lt_resources_paper.pdf).

## Download and usage

Using this dataset requires access to images from the Flickr8k and MS COCO datasets. If you have access to the MLTGPU server, a folder with the relevant images can be found at `/srv/data/gussodato/images/`. Otherwise, download the Flickr8k and MS COCO datasets to the same directory and unzip them. Then run the [`code/prepare_dataset.py`](https://github.com/TomBladsjo/LT-Resources-project/blob/main/code/prepare_dataset.py) script with the directory name as first argument to create a new directory with only the relevant images. By default, this directory will end up as `LT-Resources-project/datasets/images/`, but an optional argument `--image_dir` can be provided if you want to change this. 

Alternatively, the dataset can be used without moving the relevant images to a specific directory. In this case, column 3 of the csv files contains the path to the image within its original folder (Flickr8k or MS COCO). 

## Dataset structure

The dataset contains a total of 1313 images, of which 680 depict non-white people and 633 depict white people. Each image has two contrasting captions; one that mentions the ethnicity of the person or people in the image, and one that does not. 
The captions are divided into four separate csv files, found in `./datasets/`: 

- norm_mention.csv (white people described as white) (633 examples)
- norm_no_mention.csv (white people with no mention of ethnicity) (633 examples)
- test_mention.csv (non-white people described with ethnicity) (680 examples)
- test_no_mention.csv (non-white people with no mention of ethnicity) (680 examples)

## Testing a model on MMERB

In order to test a multimodal model on MMERB, test the model on each of the datasets (using a metric of your choice), keeping track of the order of the examples. Compare the model's performance pairwise for the two captions on each image (that is, from the `mention` and `no_mention` sets). Then compare these differences across groups (norm group and test group). For a completely unbiased model, the results would be identical for both groups. In reality, however, most models would probably be more surprised at seeing a white person described as white than at seeing e.g. a Black person being described as Black.  

An example of a project testing a model on MMERB, using perplexity as the test metric, can be found [here](https://github.com/TomBladsjo/aics-project).
