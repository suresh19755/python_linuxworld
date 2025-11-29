from twilio.rest import Client
ACCOUNT_SID = "------------"
AUTH_TOKEN = "----------"
TWILIO_NUMBER = "----------"
RECEIVER_NUMBER = "-----------"
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = Client.messages.create(
   body = "Heloo i am suresh",
   from_ = TWILIO_NUMBER,to = RECEIVER_NUMBER)