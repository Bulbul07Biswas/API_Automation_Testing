import requests
import json
import string
import random


#base url
base_url = "https://gorest.co.in/"

#Testing Jenkins
#Auth token
token = "e95a4e29b2f93d1079d2d899f272ea59d0e1471da8c21099196ade90a17d321e"

# def rest():
#     url= base_url + "/public/v2/users"
#     header= {"Authorization ": token}
#     response = requests.get(url, headers= header)
#     assert response.status_code== 200
#     json_data = response.json()   
#     json_str = json.dumps(json_data, indent= 4)  
#     #json.dumps ek stuctired way mai json op dega
#     print(json_str) 

# #call    
# rest()

#diff bw 1.{"Authorization ": token} and 2.{"Authorization": f"Bearer {token}" }
# 1.Here you are directly passing token value only.
# 2.Here we are telling This is a Bearer Token authentication.(this is more commn)

def post_request():
    url= base_url+ "/public/v2/users"
    header= {"Authorization": f"Bearer {token}" }
    data = {"name":"Poornima","email":"poornima09@gmail.com","gender":"female","status":"inactive"}
    response = requests.post(url,json = data, headers= header)
    print("POST Response :")
    print(f"POST Status Code: {response.status_code}")
    json_data = response.json()
    json_str = json.dumps(json_data, indent= 3) 
    print(json_str)
    return json_data.get("id")

def put_request(user_id):
    url = f"{base_url}/public/v2/users/{user_id}"
    header ={"Authorization": f"Bearer {token}"}
    data= {
    "name": "Poornima",
    "email": "Poornima09@gmail.com",
    "gender": "female",
    "status": "inactive"
     }
    response = requests.put(url, json = data, headers= header)
    print(f"PUT Status Code:{response.status_code}")
    json_data = response.json()
    print("PUT Response:")
    print(json.dumps(json_data, indent=3))
      
user_id=post_request()   
put_request(user_id)
