# src/tests/conftest.py

import pytest
import requests

@pytest.fixture
def client():
    yield requests.Session()
