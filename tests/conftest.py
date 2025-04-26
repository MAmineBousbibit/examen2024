import pytest
from fastapi.testclient import TestClient
from app.main import app
def pytest_configure():
    # override database URL for tests if needed
    pass
def client():
    return TestClient(app)