from django.db import models
from django.urls import reverse
import uuid
from django.conf import settings
from datetime import date

class Category(models.Model):

    type = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter the category of the UAV"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.type

    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])


class Uav(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    model = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand', on_delete=models.RESTRICT, null=True)
    weight = models.CharField('Weight', max_length=100,
                            unique=False,
                            help_text='The weight of the UAV')

    category = models.ManyToManyField(
        Category, help_text="Select the category for this UAV")

    def __str__(self):
        """String for representing the Model object."""
        return self.model

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this UAV."""
        return reverse('uav-detail', args=[str(self.id)])
    
    def display_category(self):
        return ', '.join(category.type for category in self.category.all()[:3])

    display_category.short_description = 'Category'

class UavInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="THe unique ID for the rental UAV")
    Uav = models.ForeignKey('UAV', on_delete=models.RESTRICT, null=True)

    renter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    return_date = models.DateField(null=True, blank=True)

    RENTAL_STATUS = (
        ('m', 'Maintenance'),
        ('r', 'Rented'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=RENTAL_STATUS,
        blank=True,
        default='m',
        help_text='UAV availability',
    )

    class Meta:
        ordering = ['return_date']
        permissions = (("can_mark_returned", "Set UAV as returned"),)

    def __str__(self):
        return f'{self.id} ({self.Uav.model})'
    
    @property
    def is_overdue(self):
        return bool(self.return_date and date.today() > self.return_date)

    
class Brand(models.Model):
    """Model representing an brand."""
    brand_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['brand_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular brand instance."""
        return reverse('brand-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.brand_name}'
