import csv
import dataclasses
from enum import Enum


######################################################### ENUMS ########################################################
@dataclasses.dataclass
class HtmlFile(Enum):
    INDEX = "application/index.html"
    LOGIN = "application/login.html"
    INCIVILITIES = "application/incivilities.html"
    DELAYS = "application/delays.html"
    ABSENCES = "application/absences.html"
    ADD_INCIVILITY = "application/add_incivility.html"
    ADD_DELAY = "application/add_delay.html"
    ADD_ABSENCE = "application/add_absence.html"
    UPDATE_INCIVILITY = "application/update_incivility.html"
    UPDATE_DELAY = "application/update_delay.html"
    UPDATE_ABSENCE = "application/update_absence.html"
    DOWNLOAD_SHEET = "application/download_sheet.html"


@dataclasses.dataclass
class HtmlRoute(Enum):
    INDEX = ""
    LOGIN = "login/"
    INCIVILITIES = "incivilities/"
    DELAYS = "delays/"
    ABSENCES = "absences/"
    ADD_INCIVILITY = "add_incivility/"
    ADD_DELAY = "add_delay/"
    ADD_ABSENCE = "add_absence/"
    UPDATE_INCIVILITY = "update_incivility/<int:id>/"
    UPDATE_DELAY = "update_delay/<int:id>/"
    UPDATE_ABSENCE = "update_absence/<int:id>/"
    DELETE_INCIVILITY = "delete_incivility/<int:id>/"
    DELETE_DELAY = "delete_delay/<int:id>/"
    DELETE_ABSENCE = "delete_absence/<int:id>/"
    GENERATE_CSV = "generate_csv/"
    LOAD_STUDENTS = "ajax/load-students/"
    DOWNLOAD_SHEET = "download_sheet/"


@dataclasses.dataclass
class RequestMethod(Enum):
    POST = "POST"
    GET = "GET"


####################################################### SEND MAILS #####################################################

SUPER_HEADER = ["Registre des incivilités"]
HEADER = ["Date", "Nom de l'élève", "N° et type d'incivilité", "Détail"]


# E5
def get_header_and_incivilitys_from_file(file: str) -> (list[list]):
    datas_read = []

    f = open(file=file, mode="r", encoding="utf8", newline="")

    datareader = csv.reader(f)
    datas_read.extend(iter(datareader))

    return datas_read[1:]


# E5
def write_in_file(file: str, incivilitys: list) -> (bool, str):
    message: str = ""
    success: bool = True
    f = open(file=file, mode="w", encoding="utf-8", newline="")

    try:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        writer.writerows(incivilitys)
    except Exception as ex:
        message = f"write_in_file Error : {ex}"
        success = False

    return success, message
