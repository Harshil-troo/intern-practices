from django.db import models
from django.contrib.auth.models import User


AADHAR = "Aadhar"
PAN = "Pan"
VOTER = "Voter"
ID_TYPES= (
    (AADHAR,'AADHAR'),
    (PAN,'PAN'),
    (VOTER,'VOTER')
)

USER_TYPES = (
    ("admin", "ADMIN"),
    ("user","USER")
)

class User(models.Model):
    """
    This is about the user profile in which type of user, name,
    id_proof and id_number and address contains.
    """
    user = models.OneToOneField(User, choices=USER_TYPES,default="ADMIN",on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    id_proof = models.CharField(max_length=6, choices=ID_TYPES, default=AADHAR,null=True)
    id_number = models.CharField(max_length=12,null=True)
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Computer(models.Model):

    """
    This contains the info about the computer.
    """
    computer_id = models.IntegerField(null=True)
    computer_specification= models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Computer_id : {self.computer_id}"

class Reservation(models.Model):

    """
    This contains the user who has been assigned which computer for
    specific time and also contains the time period.

    """
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_id = models.ForeignKey(Computer, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.name.name} - Computer_id : {self.computer_id.computer_id}"

