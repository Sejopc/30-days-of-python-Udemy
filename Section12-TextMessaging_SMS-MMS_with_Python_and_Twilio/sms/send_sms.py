import requests
#from twilio.rest import Client

account_sid = "AC1af1eeaece0dcc1b49aa2b6ed6605e24" # Account SID
password = "6d5165c0f5879bdf38e0969c231ae05e"   # Auth Token

twilio_number = "+12057367752"
number_to_text = "+50671031989"

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

base_url = "https://api.twilio.com/2010-04-01/Accounts"
message_url = f"{base_url}/{account_sid}/Messages"

auth = (account_sid, password)
post_data = {
    "From": twilio_number,
    "To": number_to_text,
    "Body": "This is just a text message.",
    "MediaUrl": "https://i.ibb.co/9ZTKxPw/IMG-7996.jpg" #Image
}

r = requests.get(base_url, auth=auth) # Works fine with get, but we need a POST for sending messages.

#print(r.status_code)
#print(r.text)
xml_pretty(r.text)

# SEND MESSAGE
r2 = requests.post(message_url, data=post_data, auth=auth)
print(r2.status_code)
xml_pretty(r2.text)

# GET MESSAGE INFO
message_url_ind = message_url + "/AC1af1eeaece0dcc1b49aa2b6ed6605e24" # SID is generated when the msg is sent.
get_r = requests.get(message_url_ind, auth=auth)
xml_pretty(get_r.text)
