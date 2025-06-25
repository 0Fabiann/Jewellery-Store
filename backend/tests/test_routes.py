import pytest
from app import create_app

@pytest.fixture
def app():
    """Create application for the tests."""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_hello_endpoint(client):
    """Test the hello endpoint."""
    response = client.get('/api/hello')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['message'] == 'Hello from Flask backend!'

def test_app_creation():
    """Test that the app can be created."""
    app = create_app()
    assert app is not None