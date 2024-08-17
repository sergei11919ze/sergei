from django.db import models

class Seq(models.Model):
    id = models.BigAutoField(primary_key=True)
    stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seq'