from django.db import models
from django.utils import timezone

class book(models.Model):
    book_name = models.CharField(max_length = 100)
    book_summary = models.TextField()
    book_image = models.ImageField(upload_to='books', null=True, blank=True)
    def __str__(self):
        return self.book_name

class issuebook(models.Model):
    stud_name = models.CharField(max_length = 100)
    book_name = models.ForeignKey(book,on_delete = models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    book_image = models.ImageField(upload_to='issued_books', null=True, blank=True)
    def __str__(self):
        return self.stud_name #To easily understand the created objected with name
    
class returnbook(models.Model):
    stud_name = models.CharField(max_length = 100)
    book_name = models.ForeignKey(book,on_delete = models.CASCADE)
    return_date = models.DateField()
    def __str__(self):
        return f'{self.stud_name}-{self.book_name}'
    
class purchasebook(models.Model):
    stud_name = models.CharField(max_length = 100)
    book_name = models.ForeignKey(book, on_delete=models.CASCADE)
    purchase_date = models.DateField(default = timezone.now)
    def __str__(self):
        return f"{self.stud_name} - {self.book_name}"