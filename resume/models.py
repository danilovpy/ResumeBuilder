from django.db import models

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=30, null=True)
    about = models.CharField(max_length=1000, null=True)
    skills = models.CharField(max_length=1000, null=True)
    university = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=2000, null=True)
    experience_title = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name or ""

    def skills_as_list(self):
        return self.skills.split("||")

    def skills_gen(self):
        for skill in self.skills_as_list():
            yield skill

    def experience_as_list(self):
        return self.experience.split("||")

    def experience_title_as_list(self):
        return self.experience_title.split("||")

    def experience_gen(self):
        for exp in self.experience_as_list():
            yield exp

    def experience_title_gen(self):
        for exp_t in self.experience_title_as_list():
            yield exp_t

