#!/usr/bin/env python3
#
# Author: Terry Jones, tjones@a10networks.com
#
# Date:  JUN2018
#
# This script will login into the GLM server (glm.a10networks.com) using the user
# credentials and revoke the bandwidth from an allocation to the vThunder that is offline.
#
# Note: The information required for this script should be completed before this script is
# run. I would also recommend testing the script with the information completed to verify
# functionality as well as ensure you are prepared for an emergency.
#
# REVISIONS
#   0 - Initial generation
#
'''
Example: vThunder configuration (ACOS v4.1.4-P1.69)

vThunder-Active-affinity-def-vMaster[4/1](config:2)#show run glm
!Section configuration: 94 bytes
!
glm use-mgmt-port
glm enable-requests
glm allocate-bandwidth 200
glm token vThd10516000
!
'''

__version__ = 0.1
__author__ = 'A10 Networks'

import json, argparse, requests, datetime, logging, pprint

# set the default logging format
logging.basicConfig(format="%(name)s: %(levelname)s: %(message)s")

start = datetime.datetime.now()

parser = argparse.ArgumentParser(description='This program will log into the GLM server and revoke the BW for a given vThunder.')
parser.add_argument('-p', '--password', default='a10', help='User password to access the GLM server (glm.a10networks.com)')
parser.add_argument('-u', '--username', default='admin', help='User email to access the GLM server (glm.a10networks.com)')
parser.add_argument('-z', '--uuid', default='3869D3001FD943DBA06B6A0E67F8B36D605C6360', help='show license uuid on vThunder')

try:
    args = parser.parse_args()
    password = args.password
    username = args.username
    uuid = args.uuid

except Exception as e:
    print('ArgParser Error: ', e)


#Globals - need better way to get this info
ID = '21225'


def glm_login():
    '''
    Description:

    '''
    requests.packages.urllib3.disable_warnings()

    json_header = {'Content-Type': 'application/json'}
    # Authenticate to GLM
    values = """
      {
        "user": {
          "email": "%s",
          "password": "%s"
        }
      }
    """ % (username, password)
    try:
        r = requests.post('https://glm.a10networks.com/users/sign_in.json', headers=json_header, data=values, verify=False)
        content = r.content
        parsed_json = json.loads(content)
        user_token = parsed_json['user_token']

        return user_token

    except Exception as e:
        print('Error in glm_login: ', e)


def get_lic_token(user_token):
    '''
        Description:

    '''
    requests.packages.urllib3.disable_warnings()

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }

    try:
        r = requests.get('https://glm.a10networks.com/licenses/' + ID + '.json', headers=glm_headers, verify=False)
        content = r.content
        parsed_json = json.loads(content)
        print('parsed_json: ', parsed_json)
        lic_token = parsed_json['billing_serials']

        print('lic_token: ', lic_token)
        return lic_token

    except Exception as e:
        print('Error in get_lic_token: ', e)


def get_uuid(user_token):
    '''
       Description:

       '''
    requests.packages.urllib3.disable_warnings()

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }
    try:
        r = requests.get('https://glm.a10networks.com/licenses/' + ID + '/activations.json', headers=glm_headers, verify=False)
        content = r.content.decode()
        parsed_json = json.loads(content)[0]
        uuid = parsed_json['appliance_uuid']

        return uuid

    except Exception as e:
        print('Error in get_uuid:', e)


def get_all_licences(user_token):
    '''
    Description: Will return a list of id/Entitlement token pairs

    '''
    # account_id needs to be changed to match username account.
    account_id = '472'

    requests.packages.urllib3.disable_warnings()

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }
    try:
        r = requests.get('https://glm.a10networks.com/licenses.json?account_id='+account_id, headers=glm_headers,
                         verify=False)
        content = r.content.decode()
        parsed_json = json.loads(content)

        Entitlement_tokens = []
        for i in parsed_json:
                    #id = id + i['id']
           Entitlement_tokens = Entitlement_tokens + [i['id'], i['billing_serials']]

        return Entitlement_tokens

    except Exception as e:
        print('Error in get_all_licenses:', e)


def activate_appliance(user_token):
    '''
    Description: Method will get the Entitlement token and will activate the appliance. The uuid must be included
    as argument to the script (else script will use the default, which will not be valid for your vThunder).
    '''
    requests.packages.urllib3.disable_warnings()

    lic_token = get_lic_token(user_token)[0]

    print('lic_token: ', lic_token[:-4])
    print('uuid: ', uuid)

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }

    # Activate an appliance
    values = """
      {
        "activation": {
          "appliance_uuid": "%s",
          "token": "%s",
          "version": "4.1 or newer"
        }
      }
    """ % (uuid, lic_token[:-4])
    try:
        r = requests.post('https://glm.a10networks.com/activations.json', headers=glm_headers, data=values, verify=False)
        content = r.content
        parsed_json = json.loads(content.decode())

        for i in parsed_json:
            if i['appliance_uuid'] == uuid:
                key = i['key']

        return key

    except Exception as e:
        print('Error in activate_appliance:', e)


def revoke_license(user_token):
    '''
    Description: Revoke License

    Output will print, {"message":"License has been archived."}, if successful
    '''
    requests.packages.urllib3.disable_warnings()

    # Revoke License
    glm_revoke_license_url = 'https://glm.a10networks.com/licenses/' + ID + '.json'

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }

    try:
        r = requests.delete(glm_revoke_license_url, headers=glm_headers, verify=False)
        content = r.content

        return content.decode()

    except Exception as e:
        print('Error in revoke_license: ', e)


def revoke_activation(user_token):
    '''
    Description: Revoke Activation method will revoke the activation for a given ID

    '''
    requests.packages.urllib3.disable_warnings()

    glm_revoke_activation_url = 'https://glm.a10networks.com/activations/revoke.json'

    glm_headers = {
        'Content-Type': 'application/json',
        'X-User-Email': username,
        'X-User-Token': user_token
    }

    try:
        r = requests.get('https://glm.a10networks.com/licenses/'+ID+'/activations.json',headers=glm_headers, verify=False)
        content = r.content.decode()
        parsed_json = json.loads(content)[0]

        license_id = parsed_json['license_id']
        ids = parsed_json['id']

        values = """
              {
                "license-id": "%d",
                "ids": ["%d"
                ]
              }
            """ % (license_id, ids)

        r = requests.patch(glm_revoke_activation_url, headers=glm_headers, data=values, verify=False)
        content = r.content.decode()
        parsed_json = json.loads(content)

        return r.status_code

    except Exception as e:
        print('Error in revoke_activation: ', e)


if __name__ == '__main__':

    glm_token=glm_login()
    print('Entitlement_tokens: ',get_all_licences(glm_token))
    #print('uuid: ',get_uuid(glm_token))
    #print('main::activate_appliance - key ==', activate_appliance(glm_token))
    #print(revoke_license(glm_token))
    #print('revoke_activation status_code: ', revoke_activation(glm_token))
