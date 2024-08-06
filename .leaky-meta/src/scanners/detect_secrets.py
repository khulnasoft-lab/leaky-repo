import json
from pathlib import Path
from scanners.scanner import SecretScanner

class DetectSecrets(SecretScanner):
    def __init__(self):
        super().__init__(cmd = ['detect-secrets', 'scan', '--all-files'], 
        url = 'https://github.com/Yelp/detect-secrets', 
        report_filename = 'DETECT-SECRETS.md')
    
    def parse_secret_count(self, stdout, stderr):
        finds = {}    
        results = json.loads(stdout).get('results')
        for key in results.keys():
            finds[key] = len(results.get(key))
        return finds