from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"

    # Amount validation
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value

    # Type validation
    def validate_type(self, value):
        if value not in ["income", "expense"]:
            raise serializers.ValidationError("Type must be either 'income' or 'expense'")
        return value