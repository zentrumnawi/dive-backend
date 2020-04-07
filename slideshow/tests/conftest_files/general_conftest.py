import pytest
from slideshow.models import Slideshow


@pytest.fixture
def slideshow_model_class():
    return Slideshow
