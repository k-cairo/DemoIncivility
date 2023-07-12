from django.contrib import admin

from .models import Incivility, Delay, Absence, IncivilityArchived, Teacher, Classroom, Student, IncivilityName, \
    JustifiedName, AbsenceDurationName


@admin.register(Incivility)
class IncivilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'teacher', 'incivility', 'student', 'detail')


@admin.register(Delay)
class DelayAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'teacher', 'justified_name', 'student', 'detail')


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'teacher', 'justified_name', 'student', 'detail')


@admin.register(IncivilityArchived)
class IncivilityArchivedAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'teacher', 'incivility', 'student', 'detail')


@admin.register(IncivilityName)
class IncivilityNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(JustifiedName)
class JustifiedNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AbsenceDurationName)
class AbsenceDurationNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Student)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'classroom')
    list_filter = ('classroom',)
