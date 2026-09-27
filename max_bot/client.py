import os
import requests

'''MAX_API_URL = "https://platform-api2.max.ru"
MAX_CA_CERT = "/etc/ssl/certs/ca-certificates.crt"

def get_bot_info():
    token = os.getenv("MAX_BOT_TOKEN")
    response = requests.get(
        f"{MAX_API_URL}/me",
        headers={
            "Authorization": token,
        },
        verify=MAX_CA_CERT,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()

def send_message(user_id, text):
    token = os.getenv("MAX_BOT_TOKEN")
    response = requests.post(
        f"{MAX_API_URL}/messages",
        params={
            "user_id": user_id,
        },
        headers={
            "Authorization": token,
            "Content-Type": "application/json",
        },
        json={
            #"user_id": user_id,
            "text": text,
        },
        verify=MAX_CA_CERT,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()

def get_updates(timeout=30):
    token = os.getenv("MAX_BOT_TOKEN")
    response = requests.get(
        f"{MAX_API_URL}/updates",
        headers={
            "Authorization": token,
        },
        params={
            "timeout": timeout,
        },
        verify=MAX_CA_CERT,
        timeout=timeout + 5,
    )
    response.raise_for_status()
    return response.json()'''

class MaxClient:
    API_URL = "https://platform-api2.max.ru"
    CA_CERT = "/etc/ssl/certs/ca-certificates.crt"

    def __init__(self):
        self.token = os.getenv("MAX_BOT_TOKEN")

    def get_bot_info(self):
        response = requests.get(
            f"{self.API_URL}/me",
            headers={
                "Authorization": self.token,
            },
            verify=self.CA_CERT,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def upload_image(self, file_path):
        response = requests.post(
            f"{self.API_URL}/uploads",
            params={
                "type": "image",
            },
            headers={
                "Authorization": self.token,
            },
            verify=self.CA_CERT,
            timeout=30,
        )
        response.raise_for_status()
        upload_data = response.json()
        upload_url = upload_data["url"]
        with open(file_path, "rb") as file:
            upload_response = requests.post(
                upload_url,
                headers={
                    "Authorization": self.token,
                },
                files={
                    "data": file,
                },
                verify=self.CA_CERT,
                timeout=60,
            )
        upload_response.raise_for_status()
        result = upload_response.json()
        return result["photos"]["photoIds"]["token"]

    #def send_message(self, user_id, text):
    def send_message(self, user_id, text, attachments=None):
        data = {"text": text,}
        if attachments is not None:
            data["attachments"] = attachments
        print("MAX REQUEST:", data)
        response = requests.post(
            f"{self.API_URL}/messages",
            params={"user_id": user_id,},
            headers={"Authorization": self.token,"Content-Type": "application/json",},
            #json={"text": text,},
            json=data,
            verify=self.CA_CERT,
            timeout=10,
        )
        if not response.ok:
            print("MAX ERROR STATUS:", response.status_code)
            print("MAX ERROR BODY:", response.text)
        response.raise_for_status()
        return response.json()

    def get_updates(self, timeout=30, marker=None):
        params = {
            "timeout": timeout,
        }
        if marker is not None:
            params["marker"] = marker
        response = requests.get(
            f"{self.API_URL}/updates",
            headers={
                "Authorization": self.token,
            },
            params=params,
            verify=self.CA_CERT,
            timeout=timeout + 5,
        )
        response.raise_for_status()
        return response.json()