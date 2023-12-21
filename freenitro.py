import requests
import json
import time
import uuid

def send_post_request():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {'Content-Type': 'application/json'}
    partner_user_id = str(uuid.uuid4())
    payload = {'partnerUserId': partner_user_id}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        token = data.get('token', '')

        message = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'

        webhook_url = '{your_webhook}'
        payload = {'content': message}

        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 204:
            print(f"Error sending to Discord: {response.status_code}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    while True:
        send_post_request()
        time.sleep(1.5)