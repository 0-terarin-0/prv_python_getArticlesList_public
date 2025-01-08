import functions_framework
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = 'YOUR SPREADSHEET ID'
RANGE_NAME = "Data" # Do not enter any range to get all data with array.

SERVICE_ACCOUNT_KEY = {'YOUR SERVICE ACCOUNT TOKEN OF JSON'}


def hello_http(request):
    creds = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_KEY)
    scoped_creds = creds.with_scopes([
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ])
    service = build("sheets", "v4", credentials=scoped_creds)
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
        .execute()
    )
    values = result.get("values")
    return values


if __name__ == '__main__':
    hello_http("test")
