from django.urls import path

from . import views
from .toolbox.utils import HtmlRoute

urlpatterns = [
    path(HtmlRoute.INDEX.value, views.index, name='application-index'),
    path(HtmlRoute.LOGIN.value, views.login_view, name='application-login'),
    path(HtmlRoute.INCIVILITIES.value, views.display_incivilities, name='application-display_incivilities'),
    path(HtmlRoute.DELAYS.value, views.display_delays, name='application-display_delays'),
    path(HtmlRoute.ABSENCES.value, views.display_absences, name='application-display_absences'),
    path(HtmlRoute.ADD_INCIVILITY.value, views.add_incivility, name='application-add_incivility'),
    path(HtmlRoute.ADD_DELAY.value, views.add_delay, name='application-add_delay'),
    path(HtmlRoute.ADD_ABSENCE.value, views.add_absence, name='application-add_absence'),
    path(HtmlRoute.UPDATE_INCIVILITY.value, views.update_incivility, name='application-update_incivility'),
    path(HtmlRoute.UPDATE_DELAY.value, views.update_delay, name='application-update_delay'),
    path(HtmlRoute.UPDATE_ABSENCE.value, views.update_absence, name='application-update_absence'),
    path(HtmlRoute.DELETE_INCIVILITY.value, views.delete_incivility, name='application-delete_incivility'),
    path(HtmlRoute.DELETE_DELAY.value, views.delete_delay, name='application-delete_delay'),
    path(HtmlRoute.DELETE_ABSENCE.value, views.delete_absence, name='application-delete_absence'),
    path(HtmlRoute.GENERATE_CSV.value, views.generate_csv, name='application-generate_csv'),
    path(HtmlRoute.LOAD_STUDENTS.value, views.load_students, name="application-ajax_load_students"),
    path(HtmlRoute.DOWNLOAD_SHEET.value, views.download_sheet, name="application-download_sheet")
]
