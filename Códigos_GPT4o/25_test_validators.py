import pytest
from app.utils.validators import validate_url

def test_valid_url():
    assert validate_url("https://www.example.com") == True

def test_invalid_url_scheme():
    assert validate_url("ftp://www.example.com") == False

def test_invalid_url_format():
    assert validate_url("htp://invalid-url") == False

def test_empty_url():
    assert validate_url("") == False

def test_url_without_domain():
    assert validate_url("http://") == False

def test_url_with_spaces():
    assert validate_url("https:// www.example.com") == False

def test_url_with_special_characters():
    assert validate_url("https://example.com/path?query=1&other=2") == True