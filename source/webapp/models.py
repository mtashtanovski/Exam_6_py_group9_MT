from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'Active'), ('blocked', 'Blocked')]


class Guest(models.Model):
    guest_name = models.CharField(max_length=40, null=False, blank=False, verbose_name='Name')
    guest_mail = models.EmailField(max_length=254, null=False, blank=False, verbose_name='E-mail')
    guest_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")
    status = models.CharField(max_length=20, default='active', choices=STATUS_CHOICES, verbose_name='Status')

    def __str__(self):
        return f"{self.pk}. {self.guest_name}, {self.guest_mail}. {self.guest_text}"

    class Meta:
        db_table = 'guestbook'
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'
