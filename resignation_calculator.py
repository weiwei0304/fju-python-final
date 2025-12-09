from datetime import date, datetime, timedelta

class ResignationCalculator:
    def __init__(self):
        pass

# 計算從到職日到目前的工作月數
    def _calculate_work_months(self, start_date):
        today = date.today()
        days_diff = (today - start_date).days
        months = days_diff / 30.0
        return months

# 計算最快可以離職日
    def calculate_earliest_effective_date(self, start_date):
        today = date.today()
        
        if start_date > today:
            return start_date
        
        work_months = self._calculate_work_months(start_date)
        notice_days = self._get_notice_days(work_months)
        return today + timedelta(days=notice_days)

# 計算提前幾天要通知
    def _get_notice_days(self, work_months):
        if work_months < 3:
            return 0
        elif work_months < 12:
            return 10
        elif work_months < 36:
            return 20
        else:
            return 30

# 計算到職日到離職日的工作月數
    def _calculate_work_months_until_quit(self, start_date, quit_date):
        days_diff = (quit_date - start_date).days
        months = days_diff / 30.0
        return months

    def calculate_resignation_details(self, start_date, quit_date):
        work_months = self._calculate_work_months_until_quit(start_date, quit_date)
        notice_days = self._get_notice_days(work_months)
        notice_date = quit_date - timedelta(days=notice_days)
        today = date.today()
        countdown = (quit_date - today).days
        return {
            "quit_date": quit_date,
            "notice_date": notice_date,
            "notice_days": notice_days,
            "today": today,
            "countdown": countdown,
        }
