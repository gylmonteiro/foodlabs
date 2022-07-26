from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    complement =  models.CharField(max_length=40, null=True)

    user = models.OneToOneField("users.User",on_delete = models.CASCADE, null=True)

    def __repr__(self) -> str:
        return f"Address {self.id} | Street: {self.street} / Nº {self.number}"