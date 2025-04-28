import pytest
from app.admin.parameter_handler import handle_parameters

def test_handle_parameters_valid():
    params = {'color': 'blue', 'size': 'large'}
    expected_output = {'color': 'blue', 'size': 'large'}
    assert handle_parameters(params) == expected_output

def test_handle_parameters_empty():
    params = {}
    expected_output = {}
    assert handle_parameters(params) == expected_output

def test_handle_parameters_invalid_key():
    params = {'invalid_key': 'value'}
    expected_output = {}
    assert handle_parameters(params) == expected_output

def test_handle_parameters_multiple_valid():
    params = {'color': 'red', 'size': 'medium', 'shape': 'circle'}
    expected_output = {'color': 'red', 'size': 'medium', 'shape': 'circle'}
    assert handle_parameters(params) == expected_output

def test_handle_parameters_none():
    params = None
    expected_output = {}
    assert handle_parameters(params) == expected_output