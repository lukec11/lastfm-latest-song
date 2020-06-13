# lastfm-latest-song

This API is designed to return the last song that someone listened to, based on last.fm username.

It was designed for use on my site [lukec.me](https://lukec.me.me) - the code implementation of that is [here](https://github.com/lukec11/lukec.me/blame/86c9df5672e57f2c718d88f9a67ed45d432c072f/index.html#L53-59).

## Environment Variables
`API_KEY` - your last.fm API key


## Response
The response is sent as a JSON object with the following parameters:

`song` - This is the title of the song you were last listening to.

`artist` - This is the first artist or band listed on the label. The order is generally up to the publisher.

Generally it will look something like this:
```
{
    "artist": "Arcade Fire",
    "song": "Suburban war"
}
```

Please let me know if you have any questions! Feel free to reach out via email at [me@lukec.me](me@lukc.me).