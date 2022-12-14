from django.db import models

# Create your models here.
class storage_history(models.Model):
    visceral_level = models.IntegerField(null=True, blank=True)
    body_fat = models.FloatField(null=True, blank=True)
    basal_metabolism = models.FloatField(null=True, blank=True)
    skeletal_muscle = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=100,null=True, blank=True)
    quantity_activity = models.IntegerField(null=True, blank=True)
    diet = models.CharField(max_length=100,null=True, blank=True)
    high_blood = models.IntegerField(null=True, blank=True)
    diabetes = models.CharField(max_length=100,null=True, blank=True)
    drink = models.CharField(max_length=100,null=True, blank=True)

    
    def __str__(self):
        return str('age = ') + str(self.age) + str(' , ') + str('visceral level = ') + str(self.visceral_level) + str(' , ')  +str('bmi = ') + str(self.bmi) + str(' , ')  + str('gender = ') + str(self.gender)