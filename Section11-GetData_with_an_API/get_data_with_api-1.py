import requests

base_url = "https://api.yelp.com/v3/businesses/search"
params = {
    "term":"food",
    "location":"Newport Beach"
}

#authorization = {'Authorization': 'Bearer xoJUV8w-V9MjhCPlrGnNFQCVyovSmK_toRE3fU26mcIoaWA8W33OY9yQ62uTjw1NmCmxPTy-YzHfS0oh3uVxoehost8apKOlzFw8zuYTMFEmB5U6g-DaQS2uGrgEX3Yx'}

#r = requests.get(url, headers=authorization, params=params)

#print(r.status_code)
#print(r.text)

def do_search(term="Food", location="Newport Beach"):
    base_url = "https://api.yelp.com/v3/businesses/search"
    ### 2 WAYS OF CRAFTING A REQUEST USING API ###

    ## 1 - USING THE URL ##
    term = term.replace(" ", "+")
    location = location.replace(" ", "+")
    url = "{base_url}?term={term}&location={location}".format(
                                                     base_url=base_url,
                                                     term=term,
                                                     location=location)

    ## 2 - USING PARAMS (TO BE SEND ON THE BODY OF THE REQUEST USING POST OR GET) ##
    params = {
        "term": term,
        "location": location
    }

    authorization = {'Authorization': 'Bearer xoJUV8w-V9MjhCPlrGnNFQCVyovSmK_toRE3fU26mcIoaWA8W33OY9yQ62uTjw1NmCmxPTy-YzHfS0oh3uVxoehost8apKOlzFw8zuYTMFEmB5U6g-DaQS2uGrgEX3Yx'}

    r = requests.get(base_url, headers=authorization, params=params)
    return r.json()

search_1 = do_search()
#print(search_1)
for i in search_1['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"][0])
    print(i["location"]["city"])
    print(i.get('location').get('area')) # If we not sure whether a key exists in a dictionary, we can use .get method. If it does not exist, it will simply return None.
    print("\n")
