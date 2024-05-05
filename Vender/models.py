from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Vender(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField(max_length=50)
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def validate_positive_percentage(value):
        if value < 0 or value > 100:
            raise ValidationError("Value must be less than or equal to 100.")

    on_time_delivery_rate = models.FloatField(validators=[validate_positive_percentage])

    def validate_quality_rating_avg(value):
        if value < 0 or value > 10:  # Adjust the upper limit to 10 for quality rating
            raise ValidationError("Value must be less than or equal to 10.")

    quality_rating_avg = models.FloatField(validators=[validate_quality_rating_avg])

    def validate_positive_time_in_minutes(value):
        if value < 0:
            raise ValidationError("Value must be non-negative time in minutes.")

    average_response_time = models.FloatField(
        validators=[validate_positive_time_in_minutes]
    )
    fulfillment_rate = models.FloatField(validators=[validate_positive_percentage])

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Vender"


class Purchase(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vender, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    quality_rating = models.FloatField(
        null=True, validators=[Vender.validate_quality_rating_avg]
    )
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number

    class Meta:
        db_table = "Purchase"


class Historical(models.Model):
    vendor = models.ForeignKey(Vender, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(
        validators=[Vender.validate_positive_percentage]
    )
    quality_rating_avg = models.FloatField(
        validators=[Vender.validate_quality_rating_avg]
    )
    average_response_time = models.FloatField(
        validators=[Vender.validate_positive_time_in_minutes]
    )
    fulfillment_rate = models.FloatField(
        validators=[Vender.validate_positive_percentage]
    )

    def __str__(self):
        return self.date

    class Meta:
        db_table = "Historical"
