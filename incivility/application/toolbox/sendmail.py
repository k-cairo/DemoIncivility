import dataclasses
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from pathlib import Path

from application.toolbox.conf import Conf

BASE_DIR = Path(__file__).resolve().parent.parent
INCIVILITY_CSV_PATH = os.path.join(BASE_DIR / "incivility_csv")


# E5
@dataclasses.dataclass
class Sendmail:
    csv_list: set[str] = dataclasses.field(default_factory=list)

    # E5
    def send_mail_attachment(self) -> (bool, str):
        success: bool
        message: str
        conf: Conf = Conf()

        # Load conf
        success, message = conf.load(
            pathfile=os.path.join(BASE_DIR / "config.json"))
        if not success:
            print(message)

        # Check if csvlist not empty
        if success and len(self.csv_list) < 1:
            success = False
            message = "No csv to attach ! No mail to send"

        # Send mail
        if success:
            try:
                # Build msg
                msg = MIMEMultipart()
                msg["from"] = conf.mailconf_emailfrom
                msg["to"] = conf.mailconf_emailto
                msg["subject"] = conf.mailconf_subject

                # Join all csvs in attachment
                for csv in self.csv_list:
                    slash_index: int = csv.rfind('/')
                    if slash_index == -1:
                        slash_index: int = csv.rfind("\\")
                    csv_filename: str = csv[slash_index + 1:]
                    with open(file=csv, mode='rb') as file:
                        msg.attach(MIMEApplication(file.read(), Name=csv_filename))

                # Send email
                server = smtplib.SMTP(host=conf.mailconf_smtphost, port=conf.mailconf_smtpport)
                server.starttls()
                server.login(user=conf.mailconf_emailfrom, password=conf.mailconf_password)
                server.sendmail(conf.mailconf_emailfrom, conf.mailconf_emailto, msg.as_string())
                server.quit()

            except Exception as ex:
                success = False
                message = f"\nsend_mail_attachment error : {ex}"

            return success, message
