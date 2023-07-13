import datetime
import locale
import os
from pathlib import Path

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from .form import IncivilityPostForm, DelayPostForm, AbsencePostForm, StudentSheetPostForm
from .models import Incivility, IncivilityArchived, Teacher, Student, Delay, Absence
from .toolbox.sendmail import Sendmail
from .toolbox.utils import HtmlFile, RequestMethod, HtmlRoute, get_header_and_incivilitys_from_file, write_in_file

BASE_DIR = Path(__file__).resolve().parent.parent
INCIVILITY_CSV_PATH = os.path.join(BASE_DIR / "incivility_csv")

locale.setlocale(locale.LC_TIME, '')


######################################################## INDEX #########################################################
def index(request):
    return (
        render(request, HtmlFile.INDEX.value) if request.user.is_authenticated else redirect(
            f"/{HtmlRoute.LOGIN.value}")
    )


######################################################## LOGIN #########################################################
def login_view(request):
    if request.method == RequestMethod.POST.value:
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"/{HtmlRoute.INDEX.value}")
    return render(request, HtmlFile.LOGIN.value)


####################################################### DISPLAY ########################################################
def display_incivilities(request):
    incivilities: QuerySet = Incivility.objects.all().order_by('-date')
    return render(request, HtmlFile.INCIVILITIES.value, context={'incivilities': incivilities})


def display_delays(request):
    delays: QuerySet = Delay.objects.all().order_by('-date')
    return render(request, HtmlFile.DELAYS.value, context={'delays': delays})


def display_absences(request):
    absences: QuerySet = Absence.objects.all().order_by('-date')
    return render(request, HtmlFile.ABSENCES.value, context={'absences': absences})


######################################################### ADD ##########################################################
def add_incivility(request):
    if request.method == RequestMethod.POST.value:
        form: IncivilityPostForm = IncivilityPostForm(request.POST)
        if form.is_valid():
            incivility = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=incivility.teacher)
            incivility.background_color = target_teacher.color
            incivility.date = datetime.datetime.now()
            incivility.save()
            return redirect(f"/{HtmlRoute.INCIVILITIES.value}")
    else:
        form = IncivilityPostForm()
    return render(request, HtmlFile.ADD_INCIVILITY.value, context={'form': form})


def add_delay(request):
    if request.method == RequestMethod.POST.value:
        form = DelayPostForm(request.POST)
        if form.is_valid():
            delay = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=delay.teacher)
            delay.background_color = target_teacher.color
            delay.date = datetime.datetime.now()
            delay.save()
            return redirect(f"/{HtmlRoute.DELAYS.value}")
    else:
        form = DelayPostForm()
    return render(request, HtmlFile.ADD_DELAY.value, context={'form': form})


def add_absence(request):
    if request.method == RequestMethod.POST.value:
        form = AbsencePostForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=absence.teacher)
            absence.background_color = target_teacher.color
            absence.date = datetime.datetime.now()
            absence.save()
            return redirect(f"/{HtmlRoute.ABSENCES.value}")
    else:
        form = AbsencePostForm()
    return render(request, HtmlFile.ADD_ABSENCE.value, context={'form': form})


####################################################### UPDATE #########################################################
def update_incivility(request, id):
    target_incivility = get_object_or_404(Incivility, id=id)
    if request.method == RequestMethod.POST.value:
        form = IncivilityPostForm(request.POST)
        if form.is_valid():
            incivility = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=incivility.teacher)
            incivility.background_color = target_teacher.color
            incivility.date = datetime.datetime.now()
            incivility.save()
            target_incivility.delete()
            return redirect(f"/{HtmlRoute.INCIVILITIES.value}")
    else:
        form = IncivilityPostForm(instance=target_incivility)
        return render(request, HtmlFile.UPDATE_INCIVILITY.value,
                      context={'form': form, 'target_incivility': target_incivility})


def update_delay(request, id):
    target_delay = get_object_or_404(Delay, id=id)
    if request.method == RequestMethod.POST.value:
        form = DelayPostForm(request.POST)
        if form.is_valid():
            delay = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=delay.teacher)
            delay.background_color = target_teacher.color
            delay.date = datetime.datetime.now()
            delay.save()
            target_delay.delete()
            return redirect(f"/{HtmlRoute.DELAYS.value}")
    else:
        form = DelayPostForm(instance=target_delay)
        return render(request, HtmlFile.UPDATE_DELAY.value, context={'form': form, 'target_delay': target_delay})


def update_absence(request, id):
    target_absence = get_object_or_404(Absence, id=id)
    if request.method == RequestMethod.POST.value:
        form = AbsencePostForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            target_teacher = Teacher.objects.get(name=absence.teacher)
            absence.background_color = target_teacher.color
            absence.date = datetime.datetime.now()
            absence.save()
            target_absence.delete()
            return redirect(f"/{HtmlRoute.ABSENCES.value}")
    else:
        form = AbsencePostForm(instance=target_absence)
        return render(request, HtmlFile.UPDATE_ABSENCE.value, context={'form': form, 'target_absence': target_absence})


####################################################### DELETE #########################################################
def delete_incivility(request, id):
    incivility = get_object_or_404(Incivility, id=id)
    incivility.delete()
    return redirect(f"/{HtmlRoute.INCIVILITIES.value}")


def delete_delay(request, id):
    delay = get_object_or_404(Delay, id=id)
    delay.delete()
    return redirect(f"/{HtmlRoute.DELAYS.value}")


def delete_absence(request, id):
    absence = get_object_or_404(Absence, id=id)
    absence.delete()
    return redirect(f"/{HtmlRoute.ABSENCES.value}")


############################################### DOWNLOAD STUDENT SHEET #################################################
def download_sheet(request):
    if request.method == RequestMethod.POST.value:
        form: StudentSheetPostForm = StudentSheetPostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            classroom = form.cleaned_data["classroom"]
            student = form.cleaned_data["student"]
            csv_filename: str = f"{student}_{classroom}.csv"
            csv_full_path = os.path.join(INCIVILITY_CSV_PATH, csv_filename)
            if os.path.exists(path=csv_full_path):
                data = open(file=csv_full_path, mode='rb').read()
                response = HttpResponse(data, content_type='application/csv')
                response["Content-Disposition"] = u"attachment; filename={0}".format(csv_filename)
                return response
            else:
                form = StudentSheetPostForm()
                messages.add_message(request, messages.INFO,
                                     f"L'élève {student} de la classe {classroom} ne possède pas de fiche !")
                return render(request, HtmlFile.DOWNLOAD_SHEET.value, context={"form": form})
    else:
        form = StudentSheetPostForm()
    return render(request, HtmlFile.DOWNLOAD_SHEET.value, context={"form": form})


####################################################### UTILS ##########################################################
def generate_csv(request):
    success: bool = True
    message: str
    student_first_name: str
    student_last_name: str
    csv_list: list = []
    incivilities: QuerySet = Incivility.objects.all().order_by('-date')

    # Create csv folder if not exists
    if not os.path.exists(INCIVILITY_CSV_PATH):
        os.mkdir(INCIVILITY_CSV_PATH)

    for incivility in incivilities:
        detail = "RAS" if incivility.detail == "" else incivility.detail
        incivility_format = [
            [incivility.date.strftime('%d %B %Y %H:%M'), incivility.student, incivility.incivility, detail]]

        # Build csv and write in csv
        if success:
            csv_file: str = f"{incivility.student}_{incivility.classroom}.csv"
            full_path_csv_file = os.path.join(BASE_DIR / "incivility_csv" / csv_file)
            if os.path.exists(path=full_path_csv_file):
                incivility_read: list[list] = get_header_and_incivilitys_from_file(file=full_path_csv_file)
                incivility_read += incivility_format
                success, message = write_in_file(file=full_path_csv_file, incivilitys=incivility_read)
            else:
                success, message = write_in_file(file=full_path_csv_file, incivilitys=incivility_format)

            # Add csv to csv_list
            if success:
                csv_list.append(full_path_csv_file)
            if not success:
                print(message)

        # Delete incivility if success | Else do something else
        if success:
            target_incivility = get_object_or_404(Incivility, id=incivility.id)

            archived_incivility = IncivilityArchived(
                teacher=target_incivility.teacher,
                date=target_incivility.date,
                student=target_incivility.student,
                detail=target_incivility.detail,
                incivility=target_incivility.incivility,
                classroom=target_incivility.classroom
            )
            archived_incivility.save()

            target_incivility.delete()

    # Send mail
    if success:
        email: Sendmail = Sendmail(csv_list=set(csv_list))
        success, message = email.send_mail_attachment()
        if not success:
            print(message)

    return redirect('/')


def load_students(request):
    classroom_id = request.GET.get('classroom_id')
    students = Student.objects.filter(classroom_id=classroom_id).order_by('name').all()
    return render(request, 'application/student_dropdown_list_options.html', context={'students': students})
