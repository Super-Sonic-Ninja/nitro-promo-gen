# Nitro Promotion Link Generator
This Python Script Generates a Nitro Promotion Link Via Opera GX's Extremely exploitable API
To use Just simply change {your_webhook} to a discord webhook of your choice
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/5ebf7347-d791-4ec6-b2d5-09f2163ad00d)
## Usage
To use the script simply open Up CMD (Windows + R) then cmd and enter then navigate to the directory its in (Usually Downloads) So cd "Dir" then run py freenitro.py
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/19ab5fd0-91db-4cf1-aa5e-936d29a00eb6)
## How does it work?
It sends a Post Request to https://api.discord.gx.games/v1/direct-fulfillment as application/json and the body as partnerUserId as the key and a random uuid4 string (Which is basically a random pattern of letters and numbers sort of like an ID you'd usually find) as the value as this is what Opera GX does and grabs the ey promotion token
It then sends to the webhook https://discord.com/billing/partner-promotions/1180231712274387115/{token} https://discord.com/billing/partner-promotions/ is the link every promotion uses and 1180231712274387115 is the ID of the promotion which in our case is Opera GX's 
It then puts the ey promotion token after the link and then the process is complete
### I recommend you don't put anything below 1.5 timeout as you might get ratelimited and you won't ever use that much nitro
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/f0394bb3-678e-47e0-9698-56f7ba31982e)
## If you want to manually do this
Go to https://www.postman.com/grey-shuttle-185873/workspace/example-opera-gx/request/29228469-89b72296-003c-4546-993e-110f8fdf9f2a?tab=params and fork it then you can generate a random uuid4 string using https://www.uuidgenerator.net/version4 and send the request,
You then get the token value and paste it after https://discord.com/billing/partner-promotions/ and then you've got a fresh promotion link
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/11b1cdbb-0595-4d7b-9378-89465f63912b)
