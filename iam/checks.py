import boto3
import time
import csv

from datetime import datetime, tzinfo


class IamChecks(object):

    def __init__(self, profile, region):
        self.session = boto3.Session(profile_name=profile, region_name=region)
        self.client = self.session.client("iam")

    def get_credentials_report(self):
        status = ""
        x = 0
        while self.client.generate_credential_report()['State'] != "COMPLETE":
            time.sleep(3)
            x += 1
            # After 30secs This will fail
            if x > 10:
                status = "Fail: rootUse - no CredentialReport available."
                break
        if "Fail" in status:
            return status
        response = self.client.get_credential_report()["Content"]
        report = []
        reader = csv.DictReader(str(response.splitlines()), delimiter=',')
        for row in reader:
            report.append(row)
        try:
            if report[0]['access_key_1_last_used_date']:
                pass
        except:
            report[0]['access_key_1_last_used_date'] = "N/A"
        try:
            if report[0]['access_key_2_last_used_date']:
                pass
        except:
            report[0]['access_key_2_last_used_date'] = "N/A"
        return report

    def list_users(self):
        all_users = self.client.list_users()
        users = []
        for user in all_users["Users"]:
            users.append(user["UserName"])
        return users

    def list_users_key_with_ages(self):
        users = self.list_users()
        users_keys = {}
        for user in users:
            key_details = self.client.list_access_keys(UserName=user)
            user_keys = {}
            for key in key_details["AccessKeyMetadata"]:
                if key["Status"] == "Active":
                    key_age = str(datetime.now(key["CreateDate"].tzinfo) - key["CreateDate"])
                    if "days" in key_age:
                        key_age = int(key_age.split(" ")[0])
                    else:
                        key_age = 0
                    user_keys[key["AccessKeyId"]] = key_age
            users_keys[user] = user_keys
        return users_keys

    ########################## CIS Checks for IAM ################
    def check_1(self):
        check_id = "1.1"
        description = "The root account has unrestricted access to all resources in the AWS account. It is highly " \
                      "recommended that the use of this account be avoided. "
        report = self.get_credentials_report()
        check = 0
        if report[0]["access_key_1_last_used_date"] == "N/A" or "no_information":
            pass
        else:
            fail_reason = "Used in Last 24Hrs"
            check = 1

        if report[0]["access_key_1_last_used_date"] == "N/A" or "no_information":
            pass
        else:
            fail_reason = "Used in Last 24Hrs"
            check = 1
        return {"CIS_Check_ID": check_id, "description": description, "check": check}

    # this functions is for calling a specific check
    def indirect(self, i):
        method_name = 'check_' + str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()
