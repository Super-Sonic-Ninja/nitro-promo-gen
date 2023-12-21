# Nitro Promotion Link Generator
This Python Script Generates a Nitro Promotion Link Via Opera GX's Extremely exploitable API
To use Just simply change {your_webhook} to a discord webhook of your choice
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/5ebf7347-d791-4ec6-b2d5-09f2163ad00d)
## How does it work?
It sends a Post Request to https://api.discord.gx.games/v1/direct-fulfillment as application/json and the body as partnerUserId as the key and a random uuint4 string as the value as this is what Opera GX does and grabs the ey promotion token
It then sends to the webhook https://discord.com/billing/partner-promotions/1180231712274387115/{token} https://discord.com/billing/partner-promotions/ is the link every promotion uses and 1180231712274387115 is the ID of the promotion which in our case is Opera GX's 
It then puts the ey promotion token after the link and then the process is complete
### I recommend you don't put anything below 1.5 timeout as you might get ratelimited and you won't ever use that much nitro
![image](https://github.com/Super-Sonic-Ninja/nitro-promo-gen/assets/114087198/f0394bb3-678e-47e0-9698-56f7ba31982e)
