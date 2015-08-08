import requests
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
base_url = "http://ec2-54-174-36-237.compute-1.amazonaws.com:5000"

def send_name(name):
    url = "%s/player" % base_url
    data = {'player_name': name}
    res = requests.post(url, data=json.dumps(data), headers=headers)
    if res.status_code == 200:
        return json.loads(res.text)['pid']
    else:
        return 0


def send_update(pid, results):
    url = "%s/score" % base_url
    data = {'pid': pid, 'results': results}
    res = requests.post(url, data=json.dumps(data), headers=headers)
