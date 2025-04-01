from twilio.rest import Client

account_sid = 'PUT ACTUAL ID HERE'
auth_token = 'PUT ACTUAL TOKEN HERE'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1000010101010',
    body='It is time to take hairspa.',
    to='+917778899789' # FAKE NUMBER
)

print(message.sid)
