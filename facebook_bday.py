import facebook
import access_token

graph = facebook.GraphAPI('EAAaheEkH0A0BAMkZAdCU4DuWgnQZCCwqzly0lMJa1mFznTsMwI18ttV8expVglyh8H23ehNDkZAO9ecgdXoqZBvgZBVZCdve6FlFkMUpqZA1DpK9ZBMA7EI37WxwJYCYoOAxFyhCKT20DWBDi4gsRwAjDygqjsX6qOU69poMimUdWgZDZD')

friends = graph.get_object("me/friends")
print friends
'''
for friend in friends['data']:
    #print "{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id'])
    print friend['name']
'''