from django.apps import AppConfig  # <--- Ye line missing hai

class DiseaseManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disease_management'
