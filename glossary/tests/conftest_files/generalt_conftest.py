import pytest
from glossary.models import GlossaryEntry


@pytest.fixture
def glossary_entry_model_class():
    return GlossaryEntry
