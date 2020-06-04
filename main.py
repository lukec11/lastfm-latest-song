import requests
from flask import Flask, request, Response
import json
from os import environ as env

app = Flask(__name__)

def queryLatest(user):
    res = json.loads(requests.get(
        f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={user}&api_key={env['API_KEY']}&format=json&limit=1"
        ).text
    )
    song = res['recenttracks']['track'][0]['name']
    artist = res['recenttracks']['track'][0]['artist']['#text']

    return [song, artist]


@app.route('/latest', methods=['GET'])
def latestSong():
    user = request.args.get('user')
    latestSong = queryLatest(user)
    
    songInfo =  {
        'song': latestSong[0],
        'artist': latestSong[1]
    }

    resp = Response(
        json.dumps(songInfo)
    )
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run(
    port=3000,
    debug=True,
    host='0.0.0.0'
)