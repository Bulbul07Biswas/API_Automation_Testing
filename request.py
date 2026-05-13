import requests
import json
import string
import random


#base url
base_url = "https://gorest.co.in/"

#Testing Jenkins
#Auth token
token = "e95a4e29b2f93d1079d2d899f272ea59d0e1471da8c21099196ade90a17d321e"

#Randon email_generation

def random_email_generation():
    domain = "yopmail.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(email_length))
    email = random_string + "@" + domain
    return email

def get_request():
    url= base_url + "/public/v2/users"
    header= {"Authorization ": token}
    response = requests.get(url, headers= header)
    assert response.status_code== 200
    json_data = response.json()   
    json_str = json.dumps(json_data, indent= 4)  
    #json.dumps ek stuctired way mai json op dega
    print(json_str) 
    print("Get Response is done")
    print("============================================")



#diff bw 1.{"Authorization ": token} and 2.{"Authorization": f"Bearer {token}" }
# 1.Here you are directly passing token value only.
# 2.Here we are telling This is a Bearer Token authentication.(this is more commn)

def post_request():
    url= base_url+ "/public/v2/users"
    header= {"Authorization": f"Bearer {token}" }
    data = {"name":"Name:Rachit",
            "email":random_email_generation(),
            "gender":"male",
            "status":"active"}
    response = requests.post(url,json = data, headers= header)
    print("POST Response :")
    print(f"POST Status Code: {response.status_code}")
    print("Post url" + url)
    json_data = response.json()
    json_str = json.dumps(json_data, indent= 3) 
    user_id=json_data["id"]
    print(json_str)
    print("Post Response is done")
    print("==========================================")
    return user_id
   

def put_request(user_id):
    url = f"{base_url}/public/v2/users/{user_id}"
    header ={"Authorization": f"Bearer {token}"}
    data= {
    "name": "Rahul",
    "email": random_email_generation(),
    "gender": "female",
    "status": "inactive"
     }
    response = requests.put(url, json = data, headers= header)
    print(f"PUT Status Code:{response.status_code}")
    assert response.status_code==200
    json_data = response.json()
    assert json_data["id"]== user_id
    assert json_data["name"]== "Rahul"
    print(json.dumps(json_data, indent=3))
    print("PUT URL:" + url)
    print("PUT Response is Done:")
    print("======================================") 



#Delete Method

def delete_request(user_id):
    url= f"{base_url}/public/v2/users/{user_id}"
    print("Delete url:"+ url)
    header ={"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers= header)
    print("Delete url:"+ url)
    print(f"DELETE Status Code: {response.status_code}")
    assert response.status_code == 204
    print("DELETE USER IS DONE....")
    print("=======================================")




#Call
get_request()
user_id = post_request()   
put_request(user_id)
delete_request(user_id)