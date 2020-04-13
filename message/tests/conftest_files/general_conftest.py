import pytest
from message.models import Message


@pytest.fixture
def message_model_class():
    return Message
