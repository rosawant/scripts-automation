import facebook
import access_token

graph = facebook.GraphAPI('api_key')

friends = graph.get_object("/me/friends")

conn = graph.get_connections("me", "friends")['data']

print conn

