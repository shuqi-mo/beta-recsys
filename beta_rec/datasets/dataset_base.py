import os
import shutil
import pandas as pd
import numpy as np

from beta_rec.utils.constants import *
from beta_rec.utils.download import download_file, get_format


# download_url
ML_100K_URL = r'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
ML_1M_URL = r'http://files.grouplens.org/datasets/movielens/ml-1m.zip'
ML_25M_URL = r'http://files.grouplens.org/datasets/movielens/ml-25m.zip'
EPINIONS_URL = r'http://www.trustlet.org/datasets/downloaded_epinions/ratings_data.txt.bz2'
TAFENG_URL = r'https://www.kaggle.com/chiranjivdas09/ta-feng-grocery-dataset/download'
LAST_FM_URL = r'http://files.grouplens.org/datasets/hetrec2011/hetrec2011-lastfm-2k.zip'


class DatasetBase(object):
    def __init__(self, dataset_name, url=None, manual_download_url=None):
        """Dataset base that any other datasets need to inherit from

        This is an beta dataset which can derive to other dataset.
        Several directory that store the dataset file would be created in the initial process.
        Args:
            dataset_name: the dataset name that a folder can be created with.
            url: the url that can be downloaded the dataset file.
        """
        self.url = url
        self.manual_download_url = manual_download_url if manual_download_url else url

        self.dataset_name = dataset_name

        # create the root datasets directory
        self.dataset_dir = os.path.join(os.path.abspath('.'), 'datasets')
        if not os.path.exists(self.dataset_dir):
            os.mkdir(self.dataset_dir)

        # create the dataset directory
        self.dataset_dir = os.path.join(self.dataset_dir, dataset_name)
        if not os.path.exists(self.dataset_dir):
            os.mkdir(self.dataset_dir)

        self.raw_path = os.path.join(self.dataset_dir, 'raw')
        if not os.path.exists(self.raw_path):
            os.mkdir(self.raw_path)

        self.processed_path = os.path.join(self.dataset_dir, 'processed')
        if not os.path.exists(self.processed_path):
            os.mkdir(self.processed_path)

        if not url:
            print(f'please download the dataset by your self via {self.manual_download_url} and put it into {self.raw_path} after decompression')

    def download(self):
        """Download the raw dataset

        Download the dataset with the given url and unpack the file
        """
        if not self.url:
            raise RuntimeError(f'please download the dataset by your self via {self.manual_download_url} and put it into {self.raw_path} after decompression')

        download_file_name = os.path.join(self.raw_path, os.path.splitext(os.path.basename(self.url))[0])
        print(f'get {download_file_name}')
        file_format = self.url.split('.')[-1]
        raw_file_path = os.path.join(self.raw_path, f'{self.dataset_name}.{file_format}')

        if not os.path.exists(raw_file_path):
            download_file(self.url, raw_file_path)
            shutil.unpack_archive(raw_file_path, self.raw_path, format=get_format(file_format))
            if not os.path.exists(download_file_name):
                return
            elif os.path.isdir(download_file_name):
                os.rename(download_file_name, os.path.join(self.raw_path, self.dataset_name))
            else:
                os.rename(download_file_name, os.path.join(self.raw_path, f'{self.dataset_name}.{download_file_name.split(".")[-1]}'))

    def preprocess(self):
        '''Preprocess the raw file

        A virtual function that needs to be implement in the dervied class.
        Preprocess the file downloaded via the url,
        convert it to a dataframe consist of the user-item interaction
        and save in the processed directory
        '''
        pass

    def load_interaction(self):
        """Load the user-item interaction

        Load the interaction from the processed file(Need to preprocess the raw file before loading)
        """
        processed_file_path = os.path.join(self.processed_path, f'{self.dataset_name}_interaction.npz')
        if not os.path.exists(os.path.join(processed_file_path)):
            self.preprocess()
        data = self.get_dataframe_from_npz(processed_file_path)
        return data

    def save_dataframe_as_npz(self, data, data_file):
        """Save dataframe

        Save and convert the dataframe to npz file.
        """
        user_ids = data[DEFAULT_USER_COL].to_numpy(dtype=np.long)
        item_ids = data[DEFAULT_ITEM_COL].to_numpy(dtype=np.long)
        if DEFAULT_TIMESTAMP_COL in data.columns:
            timestamps = data[DEFAULT_TIMESTAMP_COL].to_numpy(dtype=np.long)
        ratings = data[DEFAULT_RATING_COL].to_numpy(dtype=np.float32)
        if DEFAULT_TIMESTAMP_COL in data.columns:
            np.savez_compressed(
                data_file,
                user_ids=user_ids,
                item_ids=item_ids,
                timestamp=timestamps,
                ratings=ratings,
            )
        else:
            np.savez_compressed(
                data_file,
                user_ids=user_ids,
                item_ids=item_ids,
                ratings=ratings,
            )

    def get_dataframe_from_npz(self, data_file):
        """Get the dataframe from npz file

        Get the dataframe from npz file
        """
        np_data = np.load(data_file)
        if "timestamp" in np_data:
            data = pd.DataFrame(
                data={
                    DEFAULT_USER_COL: np_data["user_ids"],
                    DEFAULT_ITEM_COL: np_data["item_ids"],
                    DEFAULT_RATING_COL: np_data["ratings"],
                    DEFAULT_TIMESTAMP_COL: np_data["timestamp"],
                }
            )
        else:
            data = pd.DataFrame(
                data={
                    DEFAULT_USER_COL: np_data["user_ids"],
                    DEFAULT_ITEM_COL: np_data["item_ids"],
                    DEFAULT_RATING_COL: np_data["ratings"],
                }
            )
        return data
