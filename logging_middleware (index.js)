import requests

TOKEN = "QkbpxH"

def Log(stack, level, package, message):
    url = "http://20.207.122.201/evaluation-service/logs"

    headers = {
        "Authorization": f"Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJjZDg4ODRAc3JtaXN0LmVkdS5pbiIsImV4cCI6MTc3NzcwMTQ3NCwiaWF0IjoxNzc3NzAwNTc0LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiN2MwZTFmOGMtYzg5Ni00YTdlLTk2ZjUtMDk1MjI1ZTg4MTAxIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiY2hldGFuIGQiLCJzdWIiOiI3NjkzODE2MC00YmE4LTQwMTgtODIwMi04ZjFmNjA0MDNjM2MifSwiZW1haWwiOiJjZDg4ODRAc3JtaXN0LmVkdS5pbiIsIm5hbWUiOiJjaGV0YW4gZCIsInJvbGxObyI6InJhMjMxMTAzMDAyMDA1MCIsImFjY2Vzc0NvZGUiOiJRa2JweEgiLCJjbGllbnRJRCI6Ijc2OTM4MTYwLTRiYTgtNDAxOC04MjAyLThmMWY2MDQwM2MzYyIsImNsaWVudFNlY3JldCI6InpFeU11UVFTSE1nakN5U3cifQ.-BBmllzARqZMGtDMjUlOuk1cy0omS5MqgtJlnSSP5E0}",
        "Content-Type": "application/json"
    }

    data = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())
