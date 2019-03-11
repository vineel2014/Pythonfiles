import pickle
def LogIn():
    name=input("Please enter your name: ").lower()
    #data.pickle should be a list of dictionaries representing a user
    usernames= pickle.load('data.pickle')
    for userdata in usernames:
        if userdata['name']== name:
            return userdata
    #didn't find the name
     print('could not find '+ name+ ' in data.pickle')
return None
