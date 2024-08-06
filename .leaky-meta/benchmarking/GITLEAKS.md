Tool: https://github.com/zricethezav/gitleaks  
Command Used: `/home/dylan/.local/bin/gitleaks detect --report-path=.leaky-meta/gitleaks.json --no-git`  
Files covered: 13/44 (29.55% coverage)  
Total finds: 25/175 (14.29% coverage)  
False Positives: 0  

File Name                              |  Found/Total   | False Positives |
---------------------------------------|----------------|-----------------|
.bash_profile                          | 4/11 | 0
cloud/.credentials                     | 4/4 | 0
web/ruby/secrets.yml                   | 3/3 | 0
.bashrc                                | 2/6 | 0
.docker/.dockercfg                     | 2/4 | 0
.docker/config.json                    | 2/4 | 0
cloud/.s3cfg                           | 2/3 | 0
.ssh/id_rsa                            | 1/1 | 0
cloud/.tugboat                         | 1/3 | 0
cloud/heroku.json                      | 1/2 | 0
misc-keys/cert-key.pem                 | 1/1 | 0
.npmrc                                 | 1/3 | 0
hub                                    | 1/2 | 0
.mozilla/firefox/logins.json           | 0/28 | 0
.ssh/id_rsa.pub                        | 0/1 | 0
db/dump.sql                            | 0/10 | 0
db/mongoid.yml                         | 0/1 | 0
etc/shadow                             | 0/1 | 0
filezilla/recentservers.xml            | 0/6 | 0
filezilla/filezilla.xml                | 0/3 | 0
high-entropy-misc.txt                  | 0/2 | 0
misc-keys/putty-example.ppk            | 0/2 | 0
proftpdpasswd                          | 0/1 | 0
web/ruby/config/master.key             | 0/1 | 0
web/var/www/.env                       | 0/10 | 0
web/var/www/public_html/wp-config.php  | 0/12 | 0
web/var/www/public_html/.htpasswd      | 0/1 | 0
.git-credentials                       | 0/1 | 0
db/robomongo.json                      | 0/7 | 0
web/js/salesforce.js                   | 0/1 | 0
.netrc                                 | 0/2 | 0
config                                 | 0/4 | 0
db/.pgpass                             | 0/1 | 0
ventrilo_srv.ini                       | 0/2 | 0
web/var/www/public_html/config.php     | 0/4 | 0
db/dbeaver-data-sources.xml            | 0/1 | 0
.esmtprc                               | 0/3 | 0
web/django/settings.py                 | 0/1 | 0
deployment-config.json                 | 0/4 | 0
.ftpconfig                             | 0/5 | 0
.remote-sync.json                      | 0/3 | 0
.vscode/sftp.json                      | 0/4 | 0
sftp-config.json                       | 0/4 | 0
.idea/WebServers.xml                   | 0/2 | 0
