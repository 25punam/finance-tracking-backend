from rest_framework.permissions import BasePermission


class TransactionPermission(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if not user.is_authenticated:
            return False

        # Viewer → sirf GET
        if user.role == "viewer":
            return request.method in ["GET"]

        # Analyst → GET only
        if user.role == "analyst":
            return request.method in ["GET"]

        # Admin → full access
        if user.role == "admin":
            return True

        return False