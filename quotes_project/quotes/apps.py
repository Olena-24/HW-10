from django.apps import AppConfig



class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'

    def ready(self) -> None:
        from .scheduler.scheduler import start_command
        start_command.handle()
        
        
