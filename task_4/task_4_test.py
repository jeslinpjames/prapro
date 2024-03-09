from task_4 import file_path, download_image, df
import pytest
import os
from pathlib import Path
import pandas as pd


@pytest.fixture
def get_urls():
    return [
        "https://t2.ftcdn.net/jpg/00/58/35/35/240_F_58353522_3plS29kylx1KZQ0lU6pYHuCAhUINvCSp.jpg",
        "http://cdn.pastemagazine.com/www/articles/2011/02/04/benaffleck.jpg?635339351410282708",
        "https://images.halloweencostumes.co.uk/products/30611/1-21/womens-princess-little-deer-native-american-costume.jpg",
    ]


def test_file_saving(get_urls):
    i = 0
    for url in get_urls:
        path = download_image(url, i)
        i += 1
        assert os.path.exists(path) == True or path == "Download Failed"


def test_pq_file():
    assert os.path.exists(file_path) == True and Path(file_path).suffix == ".parquet"


def test_df():
    assert isinstance(df, pd.DataFrame)
