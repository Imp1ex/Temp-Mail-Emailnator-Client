import time
from emailnator import emailnator, message_list, message_data

email, session = emailnator(["domain", "plusGmail", "dotGmail", "googleMail"])
print(email)
print('wait..')

while True:
    messages, session = message_list(email, session)
    msg_data = messages.get('messageData') or []
    if msg_data:
        message_id = msg_data[0]['messageID']
        print(message_id)
        break
    time.sleep(5)

result, session = message_data(email, session, message_id)
print("Name:", result["name"])
print("Email:", result["email"])
print("Subject:", result["subject"])
print("Time:", result["time"])
print("Body:", result["body"])
print("Raw Data:", result["raw_data"])
