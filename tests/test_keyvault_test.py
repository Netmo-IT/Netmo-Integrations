import pytest
import requests

# Test: Function works with a valid secret name
def test_main_with_valid_secret():
    url = "http://localhost:7071/api/keyvault_test?secret=API-Pax8-Client-ID"
    
    # Sending a GET request to the local function endpoint
    response = requests.get(url)
    
    assert response.status_code == 200
    assert "rltxn3Sl7WCMPxzFnOLkzgIaXM8N2K9v" in response.text

# Test: Function returns error when 'secret' parameter is missing
def test_main_without_secret():
    url = "http://localhost:7071/api/keyvault_test"
    
    # Sending a GET request to the local function endpoint
    response = requests.get(url)
    
    assert response.status_code == 400
    assert "Please provide a 'secret' query parameter." in response.text
