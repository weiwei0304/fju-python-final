from datetime import date, datetime, timedelta
import calendar


class ResignationCalculator:
    def __init__(self):
        pass

    # 計算從到職日到目前的工作月數
    def _calculate_work_months(self, start_date):
        today = date.today()
        return self._calculate_work_months_between(start_date, today)

    # 計算兩個日期之間的精確工作月數
    def _calculate_work_months_between(self, start_date, end_date):
        years_diff = end_date.year - start_date.year
        months_diff = end_date.month - start_date.month
        days_diff = end_date.day - start_date.day

        total_months = years_diff * 12 + months_diff

        if days_diff < 0:
            # 獲得上個月的天數來計算比例
            if end_date.month == 1:
                prev_month = 12
                prev_year = end_date.year - 1
            else:
                prev_month = end_date.month - 1
                prev_year = end_date.year

            days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]

            days_ratio = abs(days_diff) / days_in_prev_month
            total_months -= days_ratio
        else:
            days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[
                1
            ]

            days_ratio = days_diff / days_in_current_month
            total_months += days_ratio

        return total_months

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
        return self._calculate_work_months_between(start_date, quit_date)

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
