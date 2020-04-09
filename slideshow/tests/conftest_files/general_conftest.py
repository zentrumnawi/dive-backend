import pytest
from slideshow.models import Slideshow, SlideshowPage


@pytest.fixture
def slideshow_model_class():
    return Slideshow


@pytest.fixture
def slideshow_page_model_class():
    return SlideshowPage

