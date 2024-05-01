from django.db import models


class UploadFileModel(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = 'Без имени'

        super().save(*args, **kwargs)


class TFIDFData(models.Model):
    uploaded_file = models.ForeignKey(UploadFileModel, on_delete=models.CASCADE)
    words = models.CharField(max_length=10000)
    tf = models.FloatField()
    idf = models.FloatField()
