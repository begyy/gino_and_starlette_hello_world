class BasePermission:
    """
    A base class from which all permission classes should inherit.
    """

    async def has_permission(self, request, view=None):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    async def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class AllowAny(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    async def has_permission(self, request, view=None):
        return True


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    async def has_permission(self, request, view=None):
        return bool(request.user and request.user.is_authenticated)


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    async def has_permission(self, request, view=None):
        return bool(request.user and request.user.is_superuser)
