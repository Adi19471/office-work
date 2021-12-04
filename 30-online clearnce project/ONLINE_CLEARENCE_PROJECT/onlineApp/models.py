from django.db import models

# Create your models here.


class Complaint(models.Model):
    dues_to_the_department               = models.CharField(max_length = 200)
    fees_for_the_hospital_and_bookshop   = models.FloatField()
    charges_for_damage                   = models.IntegerField()
    returns_all_athletic_gear            = models.BooleanField(default=True)
    Dues_to_the_student_union            = models.CharField(max_length = 200)
    Male_deal_approal                    = models.BooleanField(default=True)
    obtaining_secutity_chance            = models.CharField(max_length = 200)
    
    def __str__(self):
       return self.dues_to_the_department


class Examsrecord(models.Model):
    name            = models.CharField(max_length=120)
    passed           = models.BooleanField(default=True)
    year_of_gap      = models.CharField(max_length=50)
    message           = models.TextField()

    def __str__(self):
        return self.name
    


