import spotipy

from http import HTTPStatus
from flask import Blueprint
from flask_restful import Resource, Api
from spotipy.oauth2 import SpotifyClientCredentials

spotify_api = Blueprint('api', __name__)
api = Api(spotify_api)


class Spotify(Resource):
    def get(self, id):
        """
        1 liner about the route
        A more detailed description of the endpoint
        ---
        """
        return {"tst":"test"}

api.add_resource(Spotify, '/<int:id>', methods=['GET'])


# @spotify_api.route('/<int:limit>', endpoint='spotify_get', methods=['GET'])
# @swag_from({
#     'responses': {
#         HTTPStatus.OK.value: {
#             'description': 'Welcome to the Flask Starter Kit',
#             'schema': SpotifySchema
#         }
#     }
# })
# def spotify_get(limit=50):
#     """
#     1 liner about the route
#     A more detailed description of the endpoint
#     ---
#     """

#     # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#     # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#     # results = spotify.artist_albums(birdy_uri, album_type='album')
#     # albums = results['items']
#     # while results['next']:
#     #     results = spotify.next(results)
#     #     albums.extend(results['items'])

#     # result = []
#     # for album in albums:
#     #     result.append(album['name'])
#     # # result = SpotifyModel()
#     # return {"hello":result}


#     spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#     results = spotify.current_user_recently_played(limit=limit)

#     return results