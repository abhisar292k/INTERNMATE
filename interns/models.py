from django.db import models

class RegisteredUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class InterestForm(models.Model):
    DOMAIN_CHOICES = [
        ('Full Stack Web Dev', 'Full Stack Web Dev'),
        ('Web Dev', 'Web Dev'),
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('Bootstrap', 'Bootstrap'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.domain}"
