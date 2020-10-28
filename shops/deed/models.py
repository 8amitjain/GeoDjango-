from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Position(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    earning = models.CharField(max_length=3, default='NO')
    name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.gender} {self.name}'


class Person(models.Model):
    name = models.CharField(max_length=124)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
    married = models.BooleanField(default=False)
    income = models.FloatField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class FMW(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}:'


REPRESENTY_CHOICES =(
    ("Agent", "Agent"),
    ("Father", "Father"),
    ("Mother", "Mother"),
    ("Brother", "Brother"),
    ("Guardian", "Guardian"),
)


class SalesDeed(models.Model):
    name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    married = models.BooleanField(default=False)
    fwm = models.ForeignKey(FMW, on_delete=models.SET_NULL, blank=True, null=True)
    fwm_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    occupation = models.CharField(max_length=150)
    address = models.TextField()
    seller = models.BooleanField(default=True)
    representy = models.CharField(choices=REPRESENTY_CHOICES, max_length=8)
    unique_id = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.name


class SalesDeedRepresentative(models.Model):
    representative_name = models.CharField(max_length=200)
    representative_gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    representative_married = models.BooleanField(default=False)
    representative_fwm = models.ForeignKey(FMW, on_delete=models.SET_NULL, blank=True, null=True)
    representative_fwm_name = models.CharField(max_length=150)
    representative_birth_date = models.DateField()
    representative_occupation = models.CharField(max_length=150)
    representative_address = models.TextField()
    representative_seller = models.BooleanField(default=False)
    representative_unique_id = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.representative_name


class GiftDeed(models.Model):
    name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    married = models.BooleanField(default=False)
    fwm = models.ForeignKey(FMW, on_delete=models.SET_NULL, blank=True, null=True)
    fwm_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    occupation = models.CharField(max_length=150)
    address = models.TextField()
    unique_id = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class GiftDonorDeed(models.Model):
    representative_name = models.CharField(max_length=200)
    representative_gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    representative_married = models.BooleanField(default=False)
    representative_fwm = models.ForeignKey(FMW, on_delete=models.SET_NULL, blank=True, null=True)
    representative_fwm_name = models.CharField(max_length=150)
    representative_birth_date = models.DateField()
    representative_occupation = models.CharField(max_length=150)
    representative_address = models.TextField()
    representative_unique_id = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.representative_name


class PurchaseDeed(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    place = models.CharField(max_length=200)
    seller_name = models.CharField(max_length=200)
    seller_address = models.TextField()
    unique_id = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Deed(models.Model):
    name = models.CharField(max_length=200)
    deed = models.TextField()

    def __str__(self):
        return self.name
