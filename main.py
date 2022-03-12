def send_sms():
    """ACfc44d25ff122584fc5b5679aeaea6de4"""
 auth_token = 'a2cb8ddb1fe73b4c57758bc3af2105c8'
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='your_from_num',
    body=text,
    to='your_to_num'
)
print(message.sid)
