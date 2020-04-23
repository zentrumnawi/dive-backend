import pytest
from django.db import models


class TestSlideshowModelExists:
    """
    Test whether an object Slideshow can be imported and is a Django model.
    """
    
    def test_model_exists(self):
        from slideshow.models import Slideshow
        
    def test_model_is_django_model(self):
        from slideshow.models import Slideshow
        
        assert issubclass(Slideshow, models.Model)


class TestSlideshowPageModelExists:
    """
    Test whether an object SlideshowPage can be imported and is a Django model.
    """
    
    def test_model_exists(self):
        from slideshow.models import SlideshowPage
        
    def test_model_is_django_model(self):
        from slideshow.models import SlideshowPage
        
        assert issubclass(SlideshowPage, models.Model)


class TestSlideshowImageModelExists:
    """
    Test whether an object SlideshowImage can be imported and is a Django model.
    """
    
    def test_model_exists(self):
        from slideshow.models import SlideshowImage
        
    def test_model_is_django_model(self):
        from slideshow.models import SlideshowImage
        
        assert issubclass(SlideshowImage, models.Model)


class TestSlideshowModelFields:
    """
    Test suite with basic field tests whether all fields of the Slideshow
    object exist and have the correct class instance.
    """
    
    def test_model_has_field_titel(self, slideshow_model_class):
        assert hasattr(slideshow_model_class, "title")
        
    def test_field_type_title(self, slideshow_model_class):
        assert isinstance(
            slideshow_model_class._meta.get_field("title"), models.CharField
        )


class TestSlideshowPageModelFields:
    """
    Test suite with basic field tests whether all fields of the SlideshowPage
    object exist and have the correct class instance.
    """
    
    def test_model_has_field_show(self, slideshow_page_model_class):
        assert hasattr(slideshow_page_model_class, "show")
        
    def test_model_has_field_position(self, slideshow_page_model_class):
        assert hasattr(slideshow_page_model_class, "position")
        
    def test_model_has_field_title(self, slideshow_page_model_class):
        assert hasattr(slideshow_page_model_class, "title")
        
    def test_model_has_field_text(self, slideshow_page_model_class):
        assert hasattr(slideshow_page_model_class, "text")
        
    def test_field_type_show(self, slideshow_page_model_class):
        assert isinstance(
            slideshow_page_model_class._meta.get_field("show"), models.ForeignKey
        )
        
    def test_field_type_position(self, slideshow_page_model_class):
        assert isinstance(
            slideshow_page_model_class._meta.get_field("position"), models.PositiveSmallIntegerField
        )
        
    def test_field_type_title(self, slideshow_page_model_class):
        assert isinstance(
            slideshow_page_model_class._meta.get_field("title"), models.CharField
        )
        
    def test_field_type_text(self, slideshow_page_model_class):
        assert isinstance(
            slideshow_page_model_class._meta.get_field("text"), models.TextField
        )


class TestSlideshowImageModelFields:
    """
    Test suite with basic field tests whether all fields of the SlideshowImage
    object exist and have the correct class instance.
    """
    
    def test_model_has_field_page(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "page")
        
    def test_model_has_field_position(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "position")
        
    def test_model_has_field_title(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "title")
        
    def test_model_has_field_img(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "img")
        
    def test_model_has_field_img_alt(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "img_alt")
        
    def test_model_has_field_caption(self, slideshow_image_model_class):
        assert hasattr(slideshow_image_model_class, "caption")
    
    def test_field_type_page(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("page"), models.ForeignKey
        )
        
    def test_field_type_position(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("position"), models.PositiveSmallIntegerField
        )
        
    def test_field_type_title(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("title"), models.CharField
        )
        
    def test_field_type_img(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("img"), models.ImageField
        )
        
    def test_field_type_img_alt(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("img_alt"), models.CharField
        )
        
    def test_field_type_caption(self, slideshow_image_model_class):
        assert isinstance(
            slideshow_image_model_class._meta.get_field("caption"), models.TextField
        )
