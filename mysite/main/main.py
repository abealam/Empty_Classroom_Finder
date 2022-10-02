import os
from twilio.rest import Client

account_sid = "AC3b39582751e67fbebc1e5b615240882d"
auth_token = "089d037729295ff86d71fa8502f1d9a8"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+14432394656",
    from_="+19292543961",
    body="UMBC Room availability: This is a reminder that the room is available."

)