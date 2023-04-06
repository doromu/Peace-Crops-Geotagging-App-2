from django.db import models

# Create your models here.

class Farmer(models.Model):
    farmerID = models.CharField(max_length=255)
    farmerName = models.CharField(max_length=255)
    birthDate = models.DateField()
    gender = models.CharField(max_length=255)
    numWorkers = models.IntegerField()
    # OKAY THERE'S TOO MANY FIELDS LET'S ADD THEM ONCE WE GET THE BASIC STUFF WORKING

class Plant(models.Model):
    plantID = models.CharField(max_length=255)
    farmerID = models.ForeignKey(Farmer, on_delete=models.CASCADE, default = '')
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    datePlanted = models.DateField()
    # will add other values once it's working already

class Record(models.Model):
    recordID = models.CharField(max_length=255)
    plantID = models.ForeignKey(Plant, on_delete=models.CASCADE, default = '')
    date = models.DateField()
    time = models.TimeField()
    



# FarmerID (primary key)
# -Farmer Name
# -Age
# -Gender
# -Number of farm workers
# -Location
# -Size of Farm
# -Number of Subdivision Lots
# -GPS KML-generated map of lots (okay this is a bit much)
# -Type of crops/trees planted
# -Number of years grown to different types of crops/trees (this needs an entire table)
# -Estimated size of farm/lot allocated to trees

# Plant
# -Plant ID (primary key, will be used for QR code)
# -Farmer ID (foreign key)
# -GPS tag
# -Date of Planting (changed from age to this)
# -Variety

# Record
# -Record ID (primary key)
# -Plant ID (foreign key)
# -Date
# -Name of inspector
# -Time
# -Soil moisture
# -Temperature
# -Humidity
# -Light exposure
# -Nutrient Levels
# -Pest and disease outbreaks (might not do this for now)
# -Harvest time