from django.db import models
import uuid


# Create your models here.
class Menu(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    menu_name = models.CharField(null=False, max_length=50)
    name_url = models.CharField(null=True, max_length=50,blank=True)

    def __str__(self):
        return self.menu_name


class Under_menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    under_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    mini_menu = models.CharField(max_length=50, null=True)
    info_menu = models.TextField()

    def __str__(self):
        return self.mini_menu
