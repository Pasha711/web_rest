import pytest
from rest_framework.test import APIClient
from rest_framework import status
from users.models import CustomUser

# Используем маркер для доступа к БД во всех тестах этого модуля
pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user_data():
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
        "password_check": "testpassword123"
    }

@pytest.fixture
def test_user(test_user_data):
    data = test_user_data.copy()
    data.pop('password_check')
    return CustomUser.objects.create_user(**data)



def test_register_user_success(api_client, test_user_data):
    url = '/auth/register/'
    response = api_client.post(url, test_user_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert CustomUser.objects.filter(email=test_user_data['email']).exists()


def test_register_user_password_mismatch(api_client, test_user_data):
    data = test_user_data.copy()
    data['password_check'] = 'wrongpassword'
    
    url = '/auth/register/'
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'non_field_errors' in response.data


def test_register_user_email_exists(api_client, test_user, test_user_data):
    url = '/auth/register/'
    response = api_client.post(url, test_user_data, format='json')
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data



def test_login_user_success(api_client, test_user):
    url = '/auth/token/'
    data = {"email": test_user.email, "password": "testpassword123"}
    response = api_client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


def test_login_user_wrong_password(api_client, test_user):
    url = '/auth/token/'
    data = {"email": test_user.email, "password": "wrongpassword"}
    response = api_client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED




def test_get_profile_success(api_client, test_user):
    url = '/auth/profile/'
    api_client.force_authenticate(user=test_user)
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == test_user.email


def test_get_profile_unauthorized(api_client):
    url = '/auth/profile/'
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_update_profile_success(api_client, test_user):
    url = '/auth/profile/'
    api_client.force_authenticate(user=test_user)
    new_data = {'first_name': 'Updated Name'}
    response = api_client.put(url, new_data, format='json')
    
    test_user.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response.data['first_name'] == 'Updated Name'
    assert test_user.first_name == 'Updated Name'


def test_delete_profile_success(api_client, test_user):
    user_id = test_user.id
    url = '/auth/profile/'
    api_client.force_authenticate(user=test_user)
    response = api_client.delete(url)
    
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not CustomUser.objects.filter(id=user_id).exists()