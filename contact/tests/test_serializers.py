from rest_framework import serializers


class TestContactSerializerFields:
    """
    Test suite with basic field tests whether all fields of the Contact object exist and
    have the correct class instance.
    """

    def test_serializer_has_field_name(self, contact_serializer_field_dict):
        assert contact_serializer_field_dict.get("name")

    def test_serializer_has_field_email(self, contact_serializer_field_dict):
        assert contact_serializer_field_dict.get("email")

    def test_serializer_has_field_subject(self, contact_serializer_field_dict):
        assert contact_serializer_field_dict.get("subject")

    def test_serializer_has_field_message(self, contact_serializer_field_dict):
        assert contact_serializer_field_dict.get("message")

    def test_field_type_name(self, contact_serializer_field_dict):
        assert isinstance(
            contact_serializer_field_dict.get("name"), serializers.CharField
        )

    def test_field_type_email(self, contact_serializer_field_dict):
        assert isinstance(
            contact_serializer_field_dict.get("email"), serializers.EmailField
        )

    def test_field_type_subject(self, contact_serializer_field_dict):
        assert isinstance(
            contact_serializer_field_dict.get("subject"), serializers.CharField
        )

    def test_field_type_message(self, contact_serializer_field_dict):
        assert isinstance(
            contact_serializer_field_dict.get("message"), serializers.CharField
        )
