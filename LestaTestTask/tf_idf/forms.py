from django import forms
from .models import UploadFileModel, TFIDFData


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['file', 'name']


class TFIDFDataForm(forms.ModelForm):
    class Meta:
        model = TFIDFData
        fields = ['uploaded_file', 'words', 'tf', 'idf']
