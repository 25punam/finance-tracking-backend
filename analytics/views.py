from django.db.models import Sum
from django.db.models.functions import TruncMonth
from transactions.models import Transaction
from rest_framework.response import Response
from rest_framework.views import APIView


class FinanceSummary(APIView):

    def get(self, request):

        income = Transaction.objects.filter(type="income").aggregate(Sum("amount"))["amount__sum"] or 0

        expense = Transaction.objects.filter(type="expense").aggregate(Sum("amount"))["amount__sum"] or 0

        balance = income - expense

        return Response({

            "total_income": income,
            "total_expense": expense,
            "balance": balance

        })


class MonthlySummaryView(APIView):

    def get(self, request):

        data = (
            Transaction.objects
            .annotate(month=TruncMonth("date"))
            .values("month", "type")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )

        return Response(list(data))
    

class CategoryBreakdownView(APIView):

    def get(self, request):

        data = (
            Transaction.objects
            .values("category__name")
            .annotate(total=Sum("amount"))
            .order_by("-total")
        )

        return Response(list(data))
    
class RecentTransactionsView(APIView):

    def get(self, request):

        transactions = Transaction.objects.order_by("-date")[:5]

        data = []

        for t in transactions:
            data.append({
                "id": t.id,
                "amount": t.amount,
                "type": t.type,
                "category": t.category.name if t.category else None,
                "date": t.date
            })

        return Response(data)    