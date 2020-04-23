import pytest
from slideshow.models import Slideshow, SlideshowPage, SlideshowImage


@pytest.fixture
def slideshow_model_class():
    return Slideshow


@pytest.fixture
def slideshow_page_model_class():
    return SlideshowPage


@pytest.fixture
def slideshow_image_model_class():
    return SlideshowImage
