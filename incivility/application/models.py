from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default="")

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Classroom(models.Model):
    name = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class IncivilityName(models.Model):
    name = models.CharField(max_length=400)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class JustifiedName(models.Model):
    name = models.CharField(max_length=400)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class AbsenceDurationName(models.Model):
    name = models.CharField(max_length=400)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Incivility(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Professeur")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name="Élève")
    incivility = models.ForeignKey(IncivilityName, on_delete=models.SET_NULL, null=True, verbose_name="Incivilité")
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, verbose_name="Classe")
    date = models.DateTimeField(auto_now=True)
    detail = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.incivility} - {self.date} - {self.student} - {self.teacher} - {self.classroom}"


class Delay(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Professeur")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name="Élève")
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, verbose_name="Classe")
    justified_name = models.ForeignKey(JustifiedName, on_delete=models.SET_NULL, null=True,
                                       verbose_name="Justifié - Non Justifié")
    date = models.DateTimeField(auto_now=True)
    detail = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        return f"Retard - {self.date} - {self.student} - {self.teacher} - {self.classroom}"


class Absence(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Professeur")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name="Élève")
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, verbose_name="Classe")
    justified_name = models.ForeignKey(JustifiedName, on_delete=models.SET_NULL, null=True,
                                       verbose_name="Justifiée - Non Justifiée")
    duration = models.ForeignKey(AbsenceDurationName, on_delete=models.SET_NULL, null=True, verbose_name="Durée")
    date = models.DateTimeField(auto_now=True)
    detail = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        return f"Absence - {self.date} - {self.student} - {self.teacher} - {self.classroom}"


class IncivilityArchived(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    incivility = models.ForeignKey(IncivilityName, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    detail = models.TextField()

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.incivility} - {self.date} - {self.student} - {self.teacher} - {self.classroom}"
