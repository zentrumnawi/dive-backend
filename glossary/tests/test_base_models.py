import pytest
from django.db import models


class TestGlossaryEntryModelExists:
    def test_model_existence(self):
        """
        This Test tests if an Object GlossaryEntry can be imported.
        :return:
        """

        from glossary.models import GlossaryEntry

    def test_model_is_model(self):
        """
        Test if the GlossaryEntry Object is a Django Model
        :return:
        """
        from glossary.models import GlossaryEntry

        assert issubclass(GlossaryEntry, models.Model)


class TestGlossaryEntry:
    """
    This Testsuit summerizes the basic field tests:
    1. Do all fields exist
    2. Do all fields have the correct format/class instance
    """

    def test_model_has_term_field(self, glossary_entry_model_class):
        assert hasattr(glossary_entry_model_class, "term")

    def test_model_has_text_field(self, glossary_entry_model_class):
        assert hasattr(glossary_entry_model_class, "text")

    def test_model_has_links_field(self, glossary_entry_model_class):
        assert hasattr(glossary_entry_model_class, "links")

    def test_field_type_term(self, glossary_entry_model_class):
        assert isinstance(
            glossary_entry_model_class._meta.get_field("term"), models.CharField
        )

    def test_field_type_text(self, glossary_entry_model_class):
        assert isinstance(
            glossary_entry_model_class._meta.get_field("text"), models.TextField
        )

    def test_field_type_links(self, glossary_entry_model_class):
        assert isinstance(
            glossary_entry_model_class._meta.get_field("links"), models.ManyToManyField
        )
