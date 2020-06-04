import requests
from flask import Flask, request
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
    
    return {
        'song': latestSong[0],
        'artist': latestSong[1]
    }

app.run(
    port=3000,
    debug=False,
    host='0.0.0.0'
)