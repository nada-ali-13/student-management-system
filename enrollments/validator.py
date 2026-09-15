from datetime import datetime


def validate_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if end < start:
        raise ValueError("End date cannot be before start date")


def validate_fees(fees):
    if fees < 0:
        raise ValueError("Fees cannot be negative")
