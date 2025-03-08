from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


# advanced_features_and_security/apps.py

class AdvancedFeaturesAndSecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advanced_features_and_security'
