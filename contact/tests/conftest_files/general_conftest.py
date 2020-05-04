import pytest
from contact.serializers import ContactSerializer


@pytest.fixture
def contact_serializer_field_dict():
    return ContactSerializer().get_fields()
