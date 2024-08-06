import json
from pathlib import Path
from scanners.scanner import SecretScanner

class TruffleHog(SecretScanner):
    def __init__(self):
        super().__init__(cmd = ['trufflehog', '--json', '--regex', '.'], 
        url = 'https://github.com/dxa4481/truffleHog', 
        report_filename = 'TRUFFLEHOG.md')
    
    def parse_secret_count(self, stdout, stderr):
        finds = {}
        lines = stdout.split('\n')
        for line in lines:
            if len(line) == 0:
                # Skip empty lines
                continue
            obj = json.loads(line)
            finds[obj.get('path')] = len(obj.get('stringsFound'))
        return finds