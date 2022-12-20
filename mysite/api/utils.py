import aiohttp


async def get_employees(session, url, request_id, club_id, method, login, password):

    basic = aiohttp.BasicAuth(login, password)

    body = {
        "Request_id": request_id,
        "ClubId": club_id,
        "Method": method,
        "Parameters": {"ServiceId": ""},
    }
    async with session.post(url, auth=basic, json=body) as response:

        return await response.json()


def get_emloyees_list(emp: list[dict]):
    ret_list = []
    for employee in emp:
        _id = employee.get("ID")
        name = employee.get("Name") or ""
        last_name = employee.get("Surname") or ""
        phone = employee.get("Phone") or ""
        image_url = employee.get("Photo") or ""
        ret_list.append(
            {
                "id": _id,
                "name": name,
                "last_name": last_name,
                "phone": phone,
                "image_url": image_url,
            }
        )
    return ret_list
