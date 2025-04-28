import pytest
from app.downloaders.url_downloader import URLDownloader

@pytest.fixture
def url_downloader():
    return URLDownloader()

def test_download_valid_url(url_downloader):
    url = "https://example.com/sample.txt"
    content = url_downloader.download(url)
    assert content is not None
    assert isinstance(content, bytes)

def test_download_invalid_url(url_downloader):
    url = "https://invalid-url.com/sample.txt"
    with pytest.raises(Exception):
        url_downloader.download(url)

def test_download_empty_url(url_downloader):
    url = ""
    with pytest.raises(ValueError):
        url_downloader.download(url)