import dataclasses

from application.toolbox.file import File


@dataclasses.dataclass
class Conf:
    confjson: any = None

    # mailconf section
    mailconf_emailfrom: str = ""
    mailconf_emailto: str = ""
    mailconf_password: str = ""
    mailconf_subject: str = ""
    mailconf_smtphost: str = ""
    mailconf_smtpport: int = 0

    # E5
    def load(self, pathfile: str) -> (bool, str):
        success: bool
        message: str

        try:
            if File.is_valid_path(isdir=False, path=pathfile):
                success, message, self.confjson = File.load_json(fullpath=pathfile)
                if success:
                    success, message = self.parse_json()
            else:
                success = False
                message = f"Invalid json file : {pathfile}"
        except Exception as ex:
            success = False
            message = f"\nLoad conf error : {ex}"

        return success, message

    # E5
    def parse_json(self) -> (bool, str):
        success: bool = True
        message: str = ""

        try:
            # mailconf section
            if success and "mailconf" in self.confjson.keys():
                mailconf: dict = self.confjson["mailconf"]

                if "emailfrom" in mailconf:
                    self.mailconf_emailfrom = mailconf["emailfrom"]
                else:
                    success = False
                    message = "Invalid mailconf emailfrom"

                if "emailto" in mailconf:
                    self.mailconf_emailto = mailconf["emailto"]
                else:
                    success = False
                    message = "Invalid mailconf emailto"

                if "password" in mailconf:
                    self.mailconf_password = mailconf["password"]
                else:
                    success = False
                    message = "Invalid mailconf password"

                if "subject" in mailconf:
                    self.mailconf_subject = mailconf["subject"]
                else:
                    success = False
                    message = "Invalid mailconf subject"

                if "smtphost" in mailconf:
                    self.mailconf_smtphost = mailconf["smtphost"]
                else:
                    success = False
                    message = "Invalid mailconf smtphost"

                if "smtpport" in mailconf:
                    self.mailconf_smtpport = mailconf["smtpport"]
                else:
                    success = False
                    message = "Invalid mailconf smtpport"

            else:
                success = False
                message = "mailconf must be present"

        except Exception as ex:
            success = False
            message = f"\nParse json error : {ex}"

        return success, message
