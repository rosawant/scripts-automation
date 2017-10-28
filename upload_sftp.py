import pysftp,glob
from jira import JIRA

srv = pysftp.Connection(host="", username="roshan",password="XXXXXXX")
authed_jira = JIRA('jira url', basic_auth=('username', 'password'))

issue=raw_input('Enter jira ID::')
files=srv.listdir('path1')
file=srv.listdir('path2')

for i,j in zip(files,file):
	srv.chdir('path1')
	print i
	print srv.get(i)
	srv.chdir('path2')
	print j
	print srv.get(j)

for opfiles in glob.glob('/'):
	authed_jira.add_attachment(issue,opfiles)

authed_jira.add_comment(i.key,'Base reccon completed')


#print srv.get('/tmp/vodafone_modify_reconcile_test/outputstep1act/*', '/home/roshans/testing/' )