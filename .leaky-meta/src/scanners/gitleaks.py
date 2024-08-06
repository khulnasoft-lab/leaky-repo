import os
import json
from pathlib import Path
from scanners.scanner import SecretScanner

class Gitleaks(SecretScanner):
    def __init__(self):
        super().__init__(cmd = [str(Path.home() / ".local" / "bin" / 'gitleaks'), 'detect', '--report-path=.leaky-meta/gitleaks.json', '--no-git'], 
        url = 'https://github.com/zricethezav/gitleaks', 
        report_filename = 'GITLEAKS.md')
    
    def parse_secret_count(self, stdout, stderr):
        finds = {}
        with open('gitleaks.json') as f:
            data = json.load(f)
        for obj in  data:
            filename = obj.get('File')
            if not filename in finds:
                finds[filename] = 0
            finds[filename] += 1
        os.remove('gitleaks.json')
        return finds