import os
import glob
import gzip
from tqdm import tqdm

# set the path to your .gz files
path_to_files = 'A:\PDB'

# create a list of all .gz files in the path
gz_files = glob.glob(os.path.join(path_to_files, '*.gz'))

# loop through each file and extract its contents
for gz_file in tqdm(gz_files):
    with gzip.open(gz_file, 'rb') as f_in:
        # set the output file name
        out_file = os.path.splitext(gz_file)[0]
        with open(out_file, 'wb') as f_out:
            # copy the contents from the input to the output file
            while True:
                chunk = f_in.read(1024 * 1024)
                if not chunk:
                    break
                f_out.write(chunk)