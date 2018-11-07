# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ParkingLot(models.Model):
    lot_id = models.IntegerField()
    label = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images')
    capacity = models.IntegerField()

class Building(models.Model):
    building_id = models.IntegerField()
    label = models.CharField(max_length = 255)

class PLotBuildingConn(models.Model):
    parking_lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
    building = models.ForeignKey('Building', on_delete=models.CASCADE)
    weight = models.IntegerField();