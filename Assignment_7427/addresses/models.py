from django.db import models
import geocoder

# Create your models here.
access_token = 'pk.eyJ1Ijoia21raW0wMSIsImEiOiJja3YyNHZ6aDQzODE4MnJueW8xb2dreHN6In0.E4vmyvWw7zt-OKTZL-9gTw'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

