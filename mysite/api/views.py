from django.http import JsonResponse
from .utils import get_employees, get_emloyees_list
from .models import Integration
import aiohttp


async def get_employees_view(request):

    integration = await Integration.objects.all().afirst()
    request_id = str(integration.request_id)
    club_id = str(integration.club_id)
    method = integration.method
    url = integration.url
    login = integration.login
    password = integration.password

    async with aiohttp.ClientSession() as session:
        data = await get_employees(
            session, url, request_id, club_id, method, login, password
        )
        # print(data.status)
    employee_list = get_emloyees_list(data.get("Parameters"))
    return JsonResponse(
        {
            "Request_id": request_id,
            "ClubId": club_id,
            "Method": method,
            "Url": url,
            "Employees": employee_list,
        }
    )
