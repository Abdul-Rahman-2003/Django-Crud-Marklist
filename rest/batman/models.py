from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Student(models.Model):
    sid = models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    stamil = models.IntegerField()
    senglish = models.IntegerField()
    smaths = models.IntegerField()
    sscience = models.IntegerField()
    ssocial = models.IntegerField()
    stotal = models.IntegerField(blank=True, null=True)
    sgrade = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.stotal = self.stamil + self.senglish + self.smaths + self.sscience + self.ssocial
        average = self.stotal / 5

        if average >= 90:
            self.sgrade = "A+"
        elif average >= 75:
            self.sgrade = "A"
        elif average >= 60:
            self.sgrade = "B"
        elif average >= 50:
            self.sgrade = "C"
        else:
            self.sgrade = "F"

        super().save(*args, **kwargs)

    class Meta:
        db_table = "gotham"

