from django import forms


class IssueForm(forms.Form):
    name = forms.CharField(label="Название задачи", max_length=128)
