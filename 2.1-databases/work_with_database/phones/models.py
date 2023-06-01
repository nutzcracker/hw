from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    custom_id = models.IntegerField(primary_key=True, editable=False, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
