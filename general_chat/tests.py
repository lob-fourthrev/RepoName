from django.test import Client
from django.urls import reverse


def test_question():
    client = Client()
    response = client.post(reverse(viewname='question'),
                           {"question": "HI!"})

    assert response.status_code == 200