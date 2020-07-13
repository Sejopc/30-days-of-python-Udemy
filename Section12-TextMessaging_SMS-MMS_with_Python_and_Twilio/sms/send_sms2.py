import requests
from twilio.rest import Client

account_sid = "AC1af1eeaece0dcc1b49aa2b6ed6605e24" # Account SID
password = "6d5165c0f5879bdf38e0969c231ae05e"   # Auth Token

client = Client(account_sid, password)

twilio_number = "+12057367752"
number_to_text = "+50671031989"
message_body = "Hi. I am using Twilio RestAPI Client to send this message"
media_url = "https://i.ibb.co/9ZTKxPw/IMG-7996.jpg"

"""
Create / Send -- POST METHOD
"""

message = client.messages.create(
    body = message_body,
    from_ = twilio_number,
    to = number_to_text,
    media_url = media_url,
    #status_callback = ""
)

print(message.sid)
print(message.body)
print(message.media.list())
print(message.num_media)
print(message.subresource_uris)
print(message.uri)
print(message.status)

message_data = client.messages.get(
    sid="MMe73cf6ae7c4041f79911da30cd47adfc"
)

print(message_data.fetch())

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)
