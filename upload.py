import pysftp,glob
from jira import JIRA

srv = pysftp.Connection(host="vodafonealert.blueapple.mobi", username="roshans",password="Vuclip@808")
authed_jira = JIRA('https://vuclipdev.atlassian.net/', basic_auth=('roshan.sawant@vuclip.com', 'Welcome@1234'))

issue=raw_input('Enter jira ID::')
files=srv.listdir('/tmp/vodafone_modify_reconcile_test/outputstep1act/')
file=srv.listdir('/tmp/vodafone_modify_reconcile_test/outputstep1deact/')

for i,j in zip(files,file):
	srv.chdir('/tmp/vodafone_modify_reconcile_test/outputstep1act/')
	print i
	print srv.get(i)
	srv.chdir('/tmp/vodafone_modify_reconcile_test/outputstep1deact/')
	print j
	print srv.get(j)

for opfiles in glob.glob('/home/roshans/testing/v*.csv'):
	authed_jira.add_attachment(issue,opfiles)

authed_jira.add_comment(i.key,'Base reccon completed')


#print srv.get('/tmp/vodafone_modify_reconcile_test/outputstep1act/*', '/home/roshans/testing/' )