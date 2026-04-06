from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from users.permissions import TransactionPermission


class TransactionViewSet(viewsets.ModelViewSet):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [TransactionPermission]

    def get_queryset(self):

        queryset = super().get_queryset()

        type_ = self.request.query_params.get("type")
        category = self.request.query_params.get("category")
        date = self.request.query_params.get("date")

        if type_:
            queryset = queryset.filter(type=type_)

        if category:
            queryset = queryset.filter(category_id=category)

        if date:
            queryset = queryset.filter(date=date)

        return queryset