from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    # this is to function gives 100 char only
    def summary(self):
        return self.body[:100]

    # this function will show only date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Add the Blog app to the settings in INSTALLED_APPS

# Create a migration

# Migrate

# Add to the admin
