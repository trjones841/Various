

import pprint
from urllib.request import urlopen
from requests.auth import HTTPBasicAuth

'''
requests.get(glm_revoke_activation_url, auth=HTTPBasicAuth('username', 'password'), verify=False)
'''
username = 'tjones@a10networks.com'
password = 'Third3Eye3Blind#'

'''
with urlopen('https://glm.a10networks.com/licenses/19057/activations.json', auth=HTTPBasicAuth('username', 'password'), verify=False) as url:
    http_info = url.info()
    raw_data = url.read().decode(http_info.get_content_charset())
'''

try:
   '''
   raw_data = [{"id": 23509, "license_id": 19057, "appliance_uuid": "D7C51F706CF9161F2907DB79AA9DFCADF7D239B7",
                  "key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0eXBlIjoiY2Z3X2NhcF9zdWJfdHJpYWwiLCJjcmVhdGVkX2F0IjoxNTIxMTYyNDU2LCJjcmVhdGVkX2J5X2lkIjo1MzksInRyaWFsIjp0cnVlLCJyZXBvcnRpbmciOnRydWUsInRydXN0ZWQiOmZhbHNlLCJhY2NvdW50Ijo0NzIsImJpbGxpbmdfc2VyaWFsIjoiQTEwMDMwYzc0ZDc3MDAwMCIsImFjdGl2YXRpb25fdXVpZCI6IkQ3QzUxRjcwNkNGOTE2MUYyOTA3REI3OUFBOURGQ0FERjdEMjM5QjciLCJsaWNlbnNlX3Rva2VuIjoiQTEwMDMwYzc0ZDc3IiwiZXhwaXJlc19hdCI6MTUyMzc1MDQwMCwiZW50aXRsZW1lbnRzIjp7ImNyZWF0ZWRfYXQiOjE1MjExNjI0NTYsInRydXN0ZWQiOnsiZW5hYmxlZCI6ZmFsc2V9LCJ0cmlhbCI6eyJlbmFibGVkIjpmYWxzZX0sImV4cGlyZXNfYXQiOjE1MjM3NTA0MDAsIkFBTSI6dHJ1ZSwiQ0dOIjp0cnVlLCJEQUYiOnRydWUsIkRDRlciOnRydWUsIkdJRlciOnRydWUsIklQU0VDIjp0cnVlLCJTTEIiOnRydWUsIlNTTEkiOnRydWUsIkZQIjp0cnVlLCJVUkxGIjp0cnVlLCJXQUYiOnRydWUsIlJDIjp0cnVlLCJHU0xCIjp0cnVlLCJ2dGh1bmRlcl9wZXJwZXR1YWwiOnsiYmFuZHdpZHRoIjoyLCJjcmVhdGVkX2F0IjoxNTIxMTYyNDU2LCJleHBpcmVzX2F0IjoxNTIzNzUwNDAwfSwic3Vic2NyaXB0aW9uX21hbmFnZW1lbnRfYWdlbnQiOnsibWVzc2FnaW5nIjp7InR5cGUiOiJHTE0iLCJlbmRwb2ludCI6Imh0dHBzOi8vZ2xtLmExMG5ldHdvcmtzLmNvbS9hcHBsaWFuY2VfbWVzc2FnZXMuanNvbiJ9LCJoZWFydGJlYXRfaW50ZXJ2YWwiOjMwMH0sImJhcmVfbWV0YWwiOnsiYmFuZHdpZHRoIjoyLCJjcHVfY291bnQiOjQsImV4cGlyZXNfYXQiOjE1MjM3NTA0MDB9LCJwcm9kdWN0IjoiVHJpYWwifSwiY3VzdG9tZXJfY29udGFjdCI6eyJuYW1lIjoiVGVycnkgSm9uZXMiLCJlbWFpbCI6InRqb25lc0BhMTBuZXR3b3Jrcy5jb20ifSwicmVtYWluaW5nX2JhbmR3aWR0aCI6NiwibWluaW11bV9hbGxvY2F0ZWRfYmFuZHdpZHRoIjoyLCJtYXhpbXVtX2FsbG9jYXRlZF9iYW5kd2lkdGgiOjYsImN1cnJlbnRfdGltZSI6MTUyNjUwNzY5N30.R5yY37DjecEbZuLgqM-1M6do8hknQ5VjCFBhPTIW0iI1o2rnGSeC8hLyv3PnQZjAyLF_HJgsBKAuW5M4oezMaOhm02bL8Iwe6tGb2ZDtbZResP1ZD5oqLdvAmwt5FMy-8_iGY1Ppgo8-ysbRYLUPQ2zNV6EuT43eycJJsZ-5pPrJ_kOGoHemb-FevpTwhxM-AUEEEYTXYy5IDDFFPtFNeM_h3jGInswVXDrVHv-WMRgAYMfE6WbiU7qtncJm-UXv82-U2dMVdogD3kv621rFlRDOQSbVAam5HM9zvE9X2PCW-bcjLBhUS_lnMRUVDA72GUF-TfKUasCQRQgrYMgG8pC9n1jDUymKDaRq9MSbC7mFAPEHed8xtAOCufGPLjxbClnVKlmPypYqeZgUoeSE_6sMD8rQbVcKDTbn8WPF8uylJXWUjydUw-75Mvl41CuGI_wx9jiM7bPsELg3FqBbVtFdyJaY68jcb4CgmDYfqykMeOa2AiAb74wMdYOZN3DVIfb5hCuPRUDzofXy6Wje3yPnU-UbpK7odB4aYLcUoqiz6LJk1WTcj6ye9Dy5VieYnzVU8A5h68Cs8P-LLeKz0MpMhCSf2T5OU0fqqHsOxpD5hu1TiYCi87ARbNGmdTuwL0LG3NoXPyvq6mzmx0Yvt-y7yW88FcZoN4T_dE1u3bQ",
                  "version": "v3", "created_at": 1521162682, "updated_at": 1526507697, "pending_rma_request": 'false'},
                 {"id": 23508, "license_id": 19057, "appliance_uuid": "1DA6DE06D170F85F643EFD648E24BF7329165AFF",
                  "key": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0eXBlIjoiY2Z3X2NhcF9zdWJfdHJpYWwiLCJjcmVhdGVkX2F0IjoxNTIxMTYyNDU2LCJjcmVhdGVkX2J5X2lkIjo1MzksInRyaWFsIjp0cnVlLCJyZXBvcnRpbmciOnRydWUsInRydXN0ZWQiOmZhbHNlLCJhY2NvdW50Ijo0NzIsImJpbGxpbmdfc2VyaWFsIjoiQTEwMDMwYzc0ZDc3MDAwMCIsImFjdGl2YXRpb25fdXVpZCI6IjFEQTZERTA2RDE3MEY4NUY2NDNFRkQ2NDhFMjRCRjczMjkxNjVBRkYiLCJsaWNlbnNlX3Rva2VuIjoiQTEwMDMwYzc0ZDc3IiwiZXhwaXJlc19hdCI6MTUyMzc1MDQwMCwiZW50aXRsZW1lbnRzIjp7ImNyZWF0ZWRfYXQiOjE1MjExNjI0NTYsInRydXN0ZWQiOnsiZW5hYmxlZCI6ZmFsc2V9LCJ0cmlhbCI6eyJlbmFibGVkIjpmYWxzZX0sImV4cGlyZXNfYXQiOjE1MjM3NTA0MDAsIkFBTSI6dHJ1ZSwiQ0dOIjp0cnVlLCJEQUYiOnRydWUsIkRDRlciOnRydWUsIkdJRlciOnRydWUsIklQU0VDIjp0cnVlLCJTTEIiOnRydWUsIlNTTEkiOnRydWUsIkZQIjp0cnVlLCJVUkxGIjp0cnVlLCJXQUYiOnRydWUsIlJDIjp0cnVlLCJHU0xCIjp0cnVlLCJ2dGh1bmRlcl9wZXJwZXR1YWwiOnsiYmFuZHdpZHRoIjoyLCJjcmVhdGVkX2F0IjoxNTIxMTYyNDU2LCJleHBpcmVzX2F0IjoxNTIzNzUwNDAwfSwic3Vic2NyaXB0aW9uX21hbmFnZW1lbnRfYWdlbnQiOnsibWVzc2FnaW5nIjp7InR5cGUiOiJHTE0iLCJlbmRwb2ludCI6Imh0dHBzOi8vZ2xtLmExMG5ldHdvcmtzLmNvbS9hcHBsaWFuY2VfbWVzc2FnZXMuanNvbiJ9LCJoZWFydGJlYXRfaW50ZXJ2YWwiOjMwMH0sImJhcmVfbWV0YWwiOnsiYmFuZHdpZHRoIjoyLCJjcHVfY291bnQiOjQsImV4cGlyZXNfYXQiOjE1MjM3NTA0MDB9LCJwcm9kdWN0IjoiVHJpYWwifSwiY3VzdG9tZXJfY29udGFjdCI6eyJuYW1lIjoiVGVycnkgSm9uZXMiLCJlbWFpbCI6InRqb25lc0BhMTBuZXR3b3Jrcy5jb20ifSwicmVtYWluaW5nX2JhbmR3aWR0aCI6NiwibWluaW11bV9hbGxvY2F0ZWRfYmFuZHdpZHRoIjoyLCJtYXhpbXVtX2FsbG9jYXRlZF9iYW5kd2lkdGgiOjYsImN1cnJlbnRfdGltZSI6MTUyNjUwNTA2N30.qv8xpNKQG0K-3QQgrEFTbWr4ccLFs8YDo-G1KzHkaWmzvIS9DlA2bJxu66ITb9-NsqxyUjgp-27LpL14__ruNLawc4s7euWp6vpWVNvaTLJ0JqIswcWlqR4c4UuApuC8zKzWkwnZErxBOaPOyj1DIg4WsVCHNnTqaba4j3bqoZZor0Kt5fnd0Ini8z3pkVZZPvi-LM1V2MtSqU6akZqens0AijMyeueK1h1gKTI-XU23y03At3WmiaJvQTNMQaMlJx7Wq-eSPSO5j64JdnFHDkx1CElocRQODL6JU5Nt4MSHn1FJqzEWCiTSem9EIbl2XA6PpKs68PlLmBxnBTMFqilyM6rFuHBTSnXW5v9wFAQ8IHY1lrkHSJ_WMx6Mk4KjQpzZ82ojqdcDUwIe20oCTKaGVZPU3jblQ2x0Z1sO46qE1e7GLyyZMkvi7PzLzLkORx0-Ddt46mWAHG8phXsZee3DCF1zVqT6Oq4zI_oyMXi6dJ_rDPdKADBIIYZUQM_DEzixWe6-wfq6YXblpT8g3TY-66wr41ZMdQkjFPKut_1VJLMzaOA9srXIz_hwl5huf5GA3CUu0z5ukys9VNk48kTtb7RxYYaZHEMOvrP4wK2f-SBTEV7f5BPasOAmx8El51MpU27WFsHtoveCTA0gce8lQxjdsAAEdPx-9J4lA70",
                  "version": "v3", "created_at": 1521162679, "updated_at": 1526505067, "pending_rma_request": 'false'}]
   '''
   raw_data = [{'id': 26318, 'license_id': 21225, 'appliance_uuid': '3869D3001FD943DBA06B6A0E67F8B36D605C6360',
     'key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0eXBlIjoibGFiIiwiY3JlYXRlZF9hdCI6MTUyODgzODgyMiwiY3JlYXRlZF9ieV9pZCI6NTM5LCJ0cmlhbCI6ZmFsc2UsInJlcG9ydGluZyI6dHJ1ZSwidHJ1c3RlZCI6ZmFsc2UsImFjY291bnQiOjQ3MiwiYmlsbGluZ19zZXJpYWwiOiJ2VGhiNGQ4MjhlNWQwMDAwIiwiYWN0aXZhdGlvbl91dWlkIjoiMzg2OUQzMDAxRkQ5NDNEQkEwNkI2QTBFNjdGOEIzNkQ2MDVDNjM2MCIsImV4cGlyZXNfYXQiOjE1MzEzNTM2MDAsImVudGl0bGVtZW50cyI6eyJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJ0cnVzdGVkIjp7ImVuYWJsZWQiOmZhbHNlfSwidHJpYWwiOnsiZW5hYmxlZCI6ZmFsc2V9LCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwLCJBQU0iOnRydWUsIkNHTiI6dHJ1ZSwiREFGIjp0cnVlLCJHU0xCIjp0cnVlLCJSQyI6dHJ1ZSwiU0xCIjp0cnVlLCJGUCI6dHJ1ZSwiV0FGIjp0cnVlLCJ2dGh1bmRlcl9wZXJwZXR1YWwiOnsiYmFuZHdpZHRoIjoyLCJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwfSwicHJvZHVjdCI6IkFEQyJ9LCJjdXN0b21lcl9jb250YWN0Ijp7Im5hbWUiOiJUZXJyeSBKb25lcyIsImVtYWlsIjoidGpvbmVzQGExMG5ldHdvcmtzLmNvbSJ9LCJjdXJyZW50X3RpbWUiOjE1Mjg4Mzg5MDR9.0-Yqf29cOKoOiAfJoK-sRt7HtheLS_93edQvZzyo8UCOXqCMT0DkHaeqyUbZq_77P-GfiJqH6gpcmjRdbUKFWwYIChp10zbn9F1FXsog9b6k5dDgwxe3idzbOau2kp8lwzDeQfqkV-C1c4c28jjUlTFBZu_iIReMoPi6MxuOSu625xiTaN4Yuo5WlexLIIehKqWjqOxyR81J_tXWRTeJEX7mI_MNnEVyW8MA1OgfcMWU3eDvd4OGc0ES6d-ibKhX6bzY_sCCNbLIDN0Yoo2zo5YjK5iWRj2srAqqrTMh8r0CMkSnrq3ZvlSvnlNJ5Nk-QPfrYanPTWA2KwUYbSl4h4Z3q13_zsl4uPHwAivECJfGzwI8qMEAPGSUsdtgIGkuVGd5janpsNaYYj2NCnCtDJeybMkvAHFUjeMZYkXfIip3PL2vp_WgHNQ-df-LmqMa6DqBPzQ0toQiOJybGX1x3fEE3yHx36K4TbvVCwVwT-jiJqVoT8LqUkLtldc7KW_phvhYrYm0ZTA5Ez51RwTbE2rrN0ZL9Z9CF5ilAXLA6GeNnEcP2D0RpWA0qyQe0s61G7SZlsvMo4LqJpejgQcGHaTMGqwSwmmTs4XB3WFquD5rumgMjFmjAiRS_SGJ7PVJzm6PW9zTljakLHU-QtR8xSaP-8WjTUhKXdod1h85D6g',
     'version': '4.1 or newer', 'created_at': 1528838904, 'updated_at': 1528839153, 'pending_rma_request': False},
    {'id': 26323, 'license_id': 21225, 'appliance_uuid': '3869D3001FD943DBA06B6A0E67F8B36D605C6360',
     'key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0eXBlIjoibGFiIiwiY3JlYXRlZF9hdCI6MTUyODgzODgyMiwiY3JlYXRlZF9ieV9pZCI6NTM5LCJ0cmlhbCI6ZmFsc2UsInJlcG9ydGluZyI6dHJ1ZSwidHJ1c3RlZCI6ZmFsc2UsImFjY291bnQiOjQ3MiwiYmlsbGluZ19zZXJpYWwiOiJ2VGhiNGQ4MjhlNWQwMDAwIiwiYWN0aXZhdGlvbl91dWlkIjoiMzg2OUQzMDAxRkQ5NDNEQkEwNkI2QTBFNjdGOEIzNkQ2MDVDNjM2MCIsImV4cGlyZXNfYXQiOjE1MzEzNTM2MDAsImVudGl0bGVtZW50cyI6eyJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJ0cnVzdGVkIjp7ImVuYWJsZWQiOmZhbHNlfSwidHJpYWwiOnsiZW5hYmxlZCI6ZmFsc2V9LCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwLCJBQU0iOnRydWUsIkNHTiI6dHJ1ZSwiREFGIjp0cnVlLCJHU0xCIjp0cnVlLCJSQyI6dHJ1ZSwiU0xCIjp0cnVlLCJGUCI6dHJ1ZSwiV0FGIjp0cnVlLCJ2dGh1bmRlcl9wZXJwZXR1YWwiOnsiYmFuZHdpZHRoIjoyLCJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwfSwicHJvZHVjdCI6IkFEQyJ9LCJjdXN0b21lcl9jb250YWN0Ijp7Im5hbWUiOiJUZXJyeSBKb25lcyIsImVtYWlsIjoidGpvbmVzQGExMG5ldHdvcmtzLmNvbSJ9LCJjdXJyZW50X3RpbWUiOjE1Mjg4NDg0NzZ9.Demo-hepFBmAFP7GDH9kAO4rKJHK7306nWKbRqFl1EWxZsN3ScITqXIH2Ay1ExdZY2mDQ43e2wgwJVRBK9BB0pNfZWmZOH7fWc5Nd9ms4A_cg0LYfP2oK0u6AoCKmmglwrzHKUZorhUtpT57ixmsvzygo9pKh8RmFeO3kclqaPKihTBpNv_VOE97FCR8owaQvd-aiM9bizShplomA7p96oGSYUEOaz0KB42jjqBALmyMjtvJJt1vk22SNucNPXlFDsVRpKhQTwGyV4PeqeCNVjCGEtIXXRsToI1MXRi_ePfqkj9xIJtYO4pXoBRye00m9274tkN1N1Rx-y9HLMjcqOOxyxZ-xC9E-McvaJSVQcawmsZV40tPCrAEtscvWnVlBcbSAqyBDkQiDMAtsVKFE0Qce7p6D7uvXZcGgGhstPuhnxppCa_UYvAHIzf5-wrPOEHt4Xqx7RruvRxNerz9MTfJrvsQBhBGY-05iEKa8bHaC4maZ9l9gcuvJj1NjtQvF6cNTSTEEWBHVKYPggLAPi9ZssEsM7VAGCMn4BnNMd9NFjZzOvoczez5NTgFOQkMzg7HRyJ3nxavRwTYlOQTipiy-InL_MjL1PylxqUnD_62mlNEPnYABE1qulF2rqRlyz93OC0OuL4LhVzj4upmXhSrgwnmFEybHuiV4oVgYCk',
     'version': '4.1 or newer', 'created_at': 1528848476, 'updated_at': 1528848476, 'pending_rma_request': False},
    {'id': 26319, 'license_id': 21225, 'appliance_uuid': '3869D3001FD943DBA06B6A0E67F8B36D605C6360',
     'key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0eXBlIjoibGFiIiwiY3JlYXRlZF9hdCI6MTUyODgzODgyMiwiY3JlYXRlZF9ieV9pZCI6NTM5LCJ0cmlhbCI6ZmFsc2UsInJlcG9ydGluZyI6dHJ1ZSwidHJ1c3RlZCI6ZmFsc2UsImFjY291bnQiOjQ3MiwiYmlsbGluZ19zZXJpYWwiOiJ2VGhiNGQ4MjhlNWQwMDAwIiwiYWN0aXZhdGlvbl91dWlkIjoiMzg2OUQzMDAxRkQ5NDNEQkEwNkI2QTBFNjdGOEIzNkQ2MDVDNjM2MCIsImV4cGlyZXNfYXQiOjE1MzEzNTM2MDAsImVudGl0bGVtZW50cyI6eyJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJ0cnVzdGVkIjp7ImVuYWJsZWQiOmZhbHNlfSwidHJpYWwiOnsiZW5hYmxlZCI6ZmFsc2V9LCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwLCJBQU0iOnRydWUsIkNHTiI6dHJ1ZSwiREFGIjp0cnVlLCJHU0xCIjp0cnVlLCJSQyI6dHJ1ZSwiU0xCIjp0cnVlLCJGUCI6dHJ1ZSwiV0FGIjp0cnVlLCJ2dGh1bmRlcl9wZXJwZXR1YWwiOnsiYmFuZHdpZHRoIjoyLCJjcmVhdGVkX2F0IjoxNTI4ODM4ODIyLCJleHBpcmVzX2F0IjoxNTMxMzUzNjAwfSwicHJvZHVjdCI6IkFEQyJ9LCJjdXN0b21lcl9jb250YWN0Ijp7Im5hbWUiOiJUZXJyeSBKb25lcyIsImVtYWlsIjoidGpvbmVzQGExMG5ldHdvcmtzLmNvbSJ9LCJjdXJyZW50X3RpbWUiOjE1Mjg4MzkyNjV9.SmVvXLV6QbVjN2homGFE5s5qYq0rRrFidOX5XXrseL1YuQq8iD36wl94B6pXFhlsUgL-IPweLwwFLV1aUb9B5GeVBqLT76jwGkAgTSfdLBTpkzOGApqTcDHoQ0I84va_a_zRZ11KVYL83MPAxLIouVetv4mjGMFqn-oIRcNaqPmaAZdamGRFSoKu4F49ihE6Rm25bZiSklCvmjg-zWnjvtrAqyhw1cJOWJMxg8Tq1e8zdo06vDI9FwLfYipqZ5j1uuBnky9hlbEhaoOwaqEzY5g2he5B1DZJog1ysMycQ34v51G9YwKET0uBCpijwigtpOAo0VMUPIc6zmW70q9HczTT3lIeZ-F2VsOUfn2AFzsmYtRXnL_WjRnccb3VF91DLz0FQJNwxq1z00639e9Aq-iq-_SoyyXB-aOwa-fWYSagmv8SZkm4FsxGv9tWoOmwLdfYI7Ei_EMlwJbOMJN4pdddQfl66K6Bj_zbzGZTAOuAbyAoHKga5N78iUoL8H35HnLVSyyqceHXbxClqHiRk_JkHt3XLh9rExjpAsTLRP52qgAv9Eb1NQXhY3FuvADyO5HuVEiPol0uqF9sgjJc0Jl5HRsG5P4Ewfmit_FVLQEXGUj7vUcP0nyGNM2X-19tJHPcWrrCcUd__ycqeOJmg8a_gnH7oFSuoQhebBwhpEQ',
     'version': '4.1 or newer', 'created_at': 1528839265, 'updated_at': 1528848411, 'pending_rma_request': False}]


   print(pprint.pprint(raw_data))

except Exception as e:
    print('Error in main: ', e)