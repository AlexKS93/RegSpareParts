from rest_framework import permissions

from users.models import MODERATOR, USER


class IsAuthenticatedOrDeny(permissions.IsAuthenticated):
    def has_object_permission(self,
                              request,
                              view,
                              obj):
        return (request.user.is_authenticated)

class AuthorStaffOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self,
                              request,
                              view,
                              obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_active
                and (request.user == obj.author
                     or request.user.is_staff))


class OwnerUserOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self,
                              request,
                              view,
                              obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_active
                and request.user == obj.author
                or request.user.is_staff)


class AdminOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self,
                              request,
                              view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_active
                and request.user.is_staff)


class IsAdminRole(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        return (request.user.is_authenticated
                and request.user.is_admin())


class IsAdminOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin())


class IsAdminModeratorOwnerOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self,
                              request,
                              view,
                              obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin()
                or request.user.is_moderator()
                or obj.author == request.user)


class IsAuthOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        return (request.user.is_authenticated or request.method
                in permissions.SAFE_METHODS)

    def has_object_permission(self,
                              request,
                              view,
                              obj):
        return (obj.author == request.user or request.method
                in permissions.SAFE_METHODS)


class ReadOnly(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        return (request.method in permissions.SAFE_METHODS)


class IsUserRole(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        if request.user.is_authenticated:
            return request.user.role == USER
        return False


class IsModeratorRole(permissions.IsAuthenticated):
    def has_permission(self,
                       request,
                       view):
        if request.user.is_authenticated:
            return request.user.role == MODERATOR
        return False