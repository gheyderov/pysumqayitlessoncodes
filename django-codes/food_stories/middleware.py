from django.utils.deprecation import MiddlewareMixin
from accounts.models import BlockedIps

class GetUsersIpsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            print(request.META.get('REMOTE_ADDR'))
            ip = request.META.get('REMOTE_ADDR')
            if not request.user.ips:
                request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
                request.user.save()


class BlockUsersIpsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        x = BlockedIps.objects.filter(ip_address = ip)
        if x:
            raise PermissionError
        