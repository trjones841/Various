#!/usr/bin/env python3
#
# Author: Terry Jones, tjones@a10networks.com
#
# Date:  MAY2018
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

Pulled from source of customers glm activation tab on glm server:

https://glm.a10networks.com/licenses/19727/activations/24397/revoke_activation


Page source for revoke buttons -

<a data-toggle="tooltip" data-placement="top" data-confirm="Are You Sure You Wish To Revoke This Activation?" title="" class="btn btn-danger" rel="nofollow" data-method="post" href="/activations/24397/revoke_activation" data-original-title="Revoke Activation"><i class="fa fa-trash-o fa-fw"></i></a>

<a data-toggle="tooltip" data-placement="top" data-confirm="Are You Sure You Wish To Revoke This Activation?" title="" class="btn btn-danger" rel="nofollow" data-method="post" href="/activations/24393/revoke_activation" data-original-title="Revoke Activation"><i class="fa fa-trash-o fa-fw"></i></a>

'''

__version__ = 0.1
__author__ = 'A10 Networks'

import argparse
import requests
import datetime
import logging
from pprint import pprint
from requests.auth import HTTPBasicAuth


# set the default logging format
logging.basicConfig(format="%(name)s: %(levelname)s: %(message)s")

start = datetime.datetime.now()

parser = argparse.ArgumentParser(description='This program will log into the GLM server and revoke the BW for a given vThunder.')
parser.add_argument('-p', '--password', default='a10', help='User password to access the GLM server (glm.a10networks.com)')
parser.add_argument('-u', '--username', default='admin', help='User email to access the GLM server '
                                                                               '(glm.a10networks.com)')

try:
    args = parser.parse_args()
    password = args.password
    username = args.username

except Exception as e:
    print(e)

#glm_revoke_url = 'https://api.github.com/user', auth=HTTPBasicAuth('tjones', 'A_aa0404')
#glm_revoke_url = 'https://glm.a10networks.com/licenses/19727/activations/24397/revoke_activation'
glm_revoke_url = 'https://192.168.0.43'


def main():

    requests.packages.urllib3.disable_warnings()

    print('username: ', username)
    print('password: ', password)

    try:

        r = requests.get(glm_revoke_url, auth=HTTPBasicAuth('username', 'password'), verify=False)
        print(r.content)
        #pprint(r.json())

    except Exception as e:
        print('Error in main: ', e)





if __name__ == '__main__':
    main()






