import requests
import json
from requests.auth import HTTPBasicAuth


email = 'tjones@a10networks.com'
glm_password = 'Third3Eye3Blind#'
json_header = {'Content-Type': 'application/json'}
#s = requests.Session()

#r = s.get('https://glm.a10networks.com/users/sign_in', verify=False, auth=HTTPBasicAuth('tjones@a10networks.com', 'Third3Eye3Blind#'))
#print(r.text)
#print("Done")
# '{"cookies": {"from-my": "browser"}}'

#from requests.auth import HTTPBasicAuth
#requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))

# Authenticate to GLM
values = """
  {
    "user": {
      "email": "%s",
      "password": "%s"
    }
  }
""" % (email, glm_password)


glm_server = 'https://glm.a10networks.com'

try:
    r = requests.post(glm_server+'/users/sign_in.json', headers=json_header, data=values, verify=False)
    r.raise_for_status()
    content = r.content.decode()
    parsed_json = json.loads(content)
    user_token = parsed_json['user_token']
    print('user_token: ', user_token)

except Exception as exc:
    print('There was a problem: %s' % (exc))

revoke_uri_adc01 = '/activations/23508/revoke_activation'
revoke_uri_adc02 = '/activations/23509/revoke_activation'

#Common headers for each request
glm_headers = {
  'Content-Type': 'application/json',
  'X-User-Email': email,
  'X-User-Token': user_token
}

try:
    r = requests.post(glm_server+revoke_uri_adc01, headers=glm_headers, verify=False)
    r.raise_for_status()
    print('Status Code: ',r.status_code)
    content = r.content
    print('GLM server response to revoke: ', content)
    #parsed_json = json.loads(content)
    #print('GLM server response to revoke: ',parsed_json)

except Exception as exc:
    print('There was a problem: %s' % (exc))


#Unrevoke Actions
# unrevoke_uri_adc01 = '/licenses/19507/activations/23508/unrevoke_activation'
# unrevoke_uri_adc01 = '/licenses/19507/activations/23509/unrevoke_activation'
