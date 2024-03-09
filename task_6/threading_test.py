from task_6_p1 import Downloader, file_path
import pytest
import os


@pytest.mark.parametrize("index", [10, 12, 16])
def test_download_index(index):
    d = Downloader(file_path)
    image_path = d[index]
    assert os.path.exists(image_path) == True or image_path == "Download Failed!"


@pytest.mark.parametrize("indexes", [slice(10, 15), slice(20, 25), slice(30, 40)])
def test_download_slice(indexes):
    d = Downloader(file_path)
    start = indexes.start
    stop = indexes.stop
    image_paths = d[start:stop]
    for path in image_paths:
        assert os.path.exists(path) == True or path == "Download Failed!"
