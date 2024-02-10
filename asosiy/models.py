from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    narx = models.BigIntegerField()


class Xona(models.Model):
    nom = models.CharField(max_length=30)
    raqam = models.PositiveSmallIntegerField()


class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    tel_raqam = models.CharField(max_length=30)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=30)


class Guruh(models.Model):
    nom = models.CharField(max_length=30)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    ustoz = models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    ochilgan_sana = models.DateField()
    dars_vaqti = models.CharField(max_length=30)


class Oquvchi(models.Model):
    ism = models.CharField(max_length=30)
    tel_raqam = models.CharField(max_length=30)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)


class Tolov(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    tolov_summasi = models.FloatField()
    qarz = models.FloatField()
    chegirma = models.PositiveSmallIntegerField()
