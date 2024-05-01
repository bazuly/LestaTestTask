from django.shortcuts import render, redirect
from collections import Counter
from django.urls import reverse

from .models import UploadFileModel
from .forms import UploadFileForm

import math
import re
import string


def calculate_tf(file_content):
    file_content_lower = file_content.lower()
    words = file_content_lower.split()
    words = [re.sub(r'[^\w\s]', '', word) for word in words]
    words_count = Counter(words)
    sorted_words_count = dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True))

    return sorted_words_count


def calculate_idf(file_content, all_files_content):
    file_content_lower = file_content.lower()
    punc = string.punctuation
    content_without_punc = '[' + re.escape(punc) + ']'

    file_content_without_punctuation = re.sub(content_without_punc, '', file_content_lower)

    words_count = Counter(file_content_without_punctuation.split())

    num_documents_containing_word = {}
    for word in words_count.keys():
        num_documents_containing_word[word] = sum(1 for document in all_files_content if word in document)
    num_documents = len(all_files_content)
    idf = {word: math.log(num_documents / (num_documents_containing_word[word] + 1)) for word in words_count.keys()}
    sorted_idf = dict(sorted(idf.items(), key=lambda item: item[1]))

    return sorted_idf


def calculate_tf_idf_view(request, file_id):
    uploaded_file = UploadFileModel.objects.get(id=file_id)

    file_content = uploaded_file.file.read().decode()

    # высчитываем idf для всех загруженных файлов
    all_files_content = [file.file.read().decode() for file in UploadFileModel.objects.all()]
    tf_result = calculate_tf(file_content)
    idf_result = calculate_idf(file_content, all_files_content)

    return render(request, 'tf_idf_result.html', {
        'tf_result': tf_result,
        'idf_result': idf_result
    })


def upload_text_file(request):
    if request.method == "POST":
        file_form = UploadFileForm(request.POST, request.FILES, prefix='file')
        if file_form.is_valid():
            file_form.save()
            print('Data file txt saved successfully')
            return redirect(reverse('tf_idf:list_files'))
        else:
            print('No file uploaded or file extension is not .txt')

    else:
        file_form = UploadFileForm(prefix='file')

    return render(request, 'upload_text_file.html', {'file_form': file_form})


def list_files(request):
    uploaded_files = UploadFileModel.objects.all()
    return render(request, 'list_files.html', {'uploaded_files': uploaded_files})
