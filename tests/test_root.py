import pytest

#@pytest.mark.django_db
#def test_hello_world(client):
#    response = client.get('/')
#    assert response.status_code == 302

@pytest.mark.django_db
def test_user():
    from assopy.models import User
    from django.conf import settings

    print(settings.DATABASES)
    print(User.objects.count())

