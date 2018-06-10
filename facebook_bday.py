import facebook

graph = facebook.GraphAPI('EAACEdEose0cBAC2ZAydYWjFhV5wfiDXSYkqZAn5A2n8daC8O5mfkVElFCkVF0hHn6ZBmon2jVDwVLXTZCjccZAU6GflbZBxCZC61d4ZAtATDMoJa35AUPIXp3KDlWAYqLj2NY1lsaau7erCWseLsJ71ALBLQrQWjXJ3ZAKEeWYvBR5vc4pTc57DioxitnxYZCq1gZAsR1KrHPPzkAZDZD')
friends = graph.get_object("me/friends")
print friends
for friend in friends['data']:
    #print "{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id'])
    print friend['name']