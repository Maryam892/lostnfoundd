from django.db import models

class Item(models.Model):
    STATUS_CHOICES = (
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Claimed', 'Claimed'), # Added back here for Admin use
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True) # Image functionality restored!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title