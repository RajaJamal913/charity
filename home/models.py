from django.db import models

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('Religious Center', 'Religious Center'),
        ('Education', 'Education'),
        ('Community Center', 'Community Center'),
        ('Charity & Donations', 'Charity & Donations'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True,
        help_text="Select the department or program related to this complaint",
    )
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} — {self.name} ({self.submitted_at:%Y-%m-%d %H:%M})"
