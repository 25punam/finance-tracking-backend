from django.urls import path
from .views import *

urlpatterns = [

    path("summary/", FinanceSummary.as_view()),
    path("monthly-summary/", MonthlySummaryView.as_view()),
    path("category-breakdown/", CategoryBreakdownView.as_view()),
    path("recent-transactions/", RecentTransactionsView.as_view()),

]