from django.db import models
import uuid


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.genre


class BookData(models.Model):
    bk_name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=200, null=True, blank=True)
    publication = models.CharField(max_length=200, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.bk_name


# class Membership(models.Model):
#     mem_stat = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.mem_stat


class UserData(models.Model):
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=True, blank=True)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=300)
    # membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    membership = models.BooleanField(default=True)

    def __str__(self):
        return self.fname + " " + self.lname + " [ " + str(self.contact) + " ]"


# class BookStatus(models.Model):
#     bkst_cat = models.CharField(max_length=50, null=False)
#
#     def __str__(self):
#         return self.bkst_cat


class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    book = models.ForeignKey(BookData, on_delete=models.CASCADE)
    dt_taken = models.DateField()
    dt_returned = models.DateField(null=True, default=None)
    # bk_status = models.ForeignKey(BookStatus, on_delete=models.CASCADE)
    bk_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + str(self.book) + str(self.dt_taken)
