import pytest
from app.services.download_service import DownloadService

@pytest.fixture
def download_service():
    return DownloadService()

def test_download_valid_url(download_service):
    url = "https://example.com/sample.txt"
    result = download_service.download(url)
    assert result is True  # Assuming the download method returns True on success

def test_download_invalid_url(download_service):
    url = "https://invalid-url"
    result = download_service.download(url)
    assert result is False  # Assuming the download method returns False on failure

def test_download_empty_url(download_service):
    url = ""
    result = download_service.download(url)
    assert result is False  # Assuming the download method returns False for empty URL