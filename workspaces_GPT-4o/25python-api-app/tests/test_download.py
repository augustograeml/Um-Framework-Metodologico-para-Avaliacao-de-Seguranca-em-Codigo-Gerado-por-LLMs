import pytest
from app.routes.download import download_file
from fastapi import HTTPException

def test_download_file_success(mocker):
    mock_url = "http://example.com/file.txt"
    mock_response = mocker.patch("app.services.downloader.Downloader.download", return_value=b"file content")
    mock_save = mocker.patch("app.services.downloader.Downloader.save_file", return_value="file.txt")

    response = download_file(mock_url)

    assert response == {"filename": "file.txt"}
    mock_response.assert_called_once_with(mock_url)
    mock_save.assert_called_once_with(b"file content")

def test_download_file_invalid_url():
    invalid_url = "invalid-url"

    with pytest.raises(HTTPException) as exc_info:
        download_file(invalid_url)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid URL provided."

def test_download_file_download_failure(mocker):
    mock_url = "http://example.com/file.txt"
    mocker.patch("app.services.downloader.Downloader.download", side_effect=Exception("Download failed"))

    with pytest.raises(HTTPException) as exc_info:
        download_file(mock_url)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Failed to download the file."