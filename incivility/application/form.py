from django import forms
from django.forms import ModelForm

from application.models import Incivility, Student, Delay, Absence


class IncivilityPostForm(ModelForm):
    detail = forms.CharField(required=False, label="Détail")

    class Meta:
        model = Incivility
        fields = ['teacher', 'classroom', 'student', 'incivility', 'detail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

        if 'classroom' in self.data:
            try:
                classroom_id = int(self.data.get('classroom'))
                self.fields['student'].queryset = Student.objects.filter(classroom_id=classroom_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('name')


class DelayPostForm(ModelForm):
    detail = forms.CharField(required=False, label="Détail")

    class Meta:
        model = Delay
        fields = ['teacher', 'classroom', 'student', 'justified_name', 'detail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

        if 'classroom' in self.data:
            try:
                classroom_id = int(self.data.get('classroom'))
                self.fields['student'].queryset = Student.objects.filter(classroom_id=classroom_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('name')


class AbsencePostForm(ModelForm):
    detail = forms.CharField(required=False, label="Détail")

    class Meta:
        model = Absence
        fields = ['teacher', 'classroom', 'student', 'duration', 'justified_name', 'detail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

        if 'classroom' in self.data:
            try:
                classroom_id = int(self.data.get('classroom'))
                self.fields['student'].queryset = Student.objects.filter(classroom_id=classroom_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('name')


class StudentSheetPostForm(ModelForm):
    class Meta:
        model = Incivility
        fields = ['classroom', 'student']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

        if 'classroom' in self.data:
            try:
                classroom_id = int(self.data.get('classroom'))
                self.fields['student'].queryset = Student.objects.filter(classroom_id=classroom_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.classroom.student_set.order_by('name')
