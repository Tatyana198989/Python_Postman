import requests
import unittest
import json
from faker import Faker
from random import randint 


fake=Faker()

user_id = randint(1,1000)  
user_name = fake.user_name()
first_name =fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password()
phone_number = fake.phone_number()
userStatus = randint(1,100) 
update_first_name = fake.first_name()
update_last_name = fake.last_name()



headers = {'Content-Type': 'application/json'}


class TestPostman(unittest.TestCase):
    


    def test1_post_create_user(self):
        payload = json.dumps({'id': user_id, 'username': user_name, 'firstName': first_name, 'lastName': last_name, 'email': email, 'password': password, 'phone': phone_number, 'userStatus': userStatus})
        response = requests.post("https://petstore.swagger.io/v2/user", headers = headers , data=payload)
        if response.status_code==200:
            print(response.text)


    def test2_get_log_system(self):
        payload = json.dumps({'username': user_name, 'password': password}) 
        response = requests.get("https://petstore.swagger.io/v2/user/login", headers = headers , params=payload)
        if response.status_code==200:
            print(response.text)


    def test3_get_user(self):
        response = requests.get("https://petstore.swagger.io/v2/user/" + user_name, headers = headers)
        if response.status_code==200:
            print(response.text)


    def test4_put_update_user(self):
        payload = json.dumps({'id': user_id, 'username': user_name, 'firstName': update_first_name, 'lastName': update_last_name,  'email': email, 'password': password, 'phone': phone_number, 'userStatus': userStatus} ) 
        response = requests.put("https://petstore.swagger.io/v2/user/" + user_name, headers = headers , data=payload)
        if response.status_code==200:
            print(response.text)


    def test5_get_update_user(self):
        response = requests.get("https://petstore.swagger.io/v2/user/" + user_name, headers = headers)
        if response.status_code==200:
            print(response.text)


    def test6_delete_user(self):
        response = requests.delete("https://petstore.swagger.io/v2/user/" + user_name,  headers = headers)
        if response.status_code==200:
            print(response.text)


    def test7_get_delete_user(self):
        response = requests.get("https://petstore.swagger.io/v2/user/" + user_name, headers = headers)
        if response.status_code==200:
            print(response.text)



if __name__ == '__main__':
    unittest.main()