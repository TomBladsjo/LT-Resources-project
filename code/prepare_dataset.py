import os
from pathlib import Path
import shutil
import glob
import argparse
import pandas as pd


def copy_images(csv_file, storage_dir, outdir):
    '''Takes as argument a csv file with information about the image paths
    and a directory where the original datasets are stored, and copies the 
    relevant images to a specific folder.
    '''
    if not Path(outdir).is_dir():
        os.mkdir(outdir)
        
    df = pd.read_csv(csv_file)
    for i in range(len(df)):
        imgpath = os.path.join(storage_dir, df['3'][i], df['2'][i])
        destpath = os.path.join(outdir, df['2'][i])
        shutil.copy(imgpath, destpath)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prepare folder with all dataset images.')
    parser.add_argument("storage_dir", type=str, help="Path to directory containing the original datasets (in this case MS COCO and Flickr8k), which should be downloaded and unzipped.")
    parser.add_argument("--image_dir", dest='image_dir', type=str, default='../datasets/images/', help="Path where the resulting images will be stored. If unspecified, will default to '../datasets/images/'")
    args = parser.parse_args()
    
    storage_dir = args.storage_dir
    datadir = '../datasets/'
    imgdir = args.image_dir

    print(f'Copying images from {storage_dir} to {imgdir}...\n')
    for file in glob.glob(os.path.join(datadir, '*_no_mention.csv')):
        print(f'Working on {file}')
        copy_images(file, storage_dir, imgdir)
        
    print('\nDone!')
    


    
    















