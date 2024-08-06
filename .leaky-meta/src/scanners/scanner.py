from typing import List, Dict

import os
import subprocess
from subprocess import PIPE
from abc import ABCMeta, abstractmethod

class SecretScanner(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, cmd: List[str], url: str, report_filename: str):
        self.cmd = cmd
        self.url = url
        self.report_filename = report_filename

    def _get_command_stdout(self, cmd, cwd='..'):
        os.path.abspath(cwd)
        p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=cwd)
        stdout, stderr = p.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8') if stderr else None
    
    @abstractmethod
    def parse_secret_count(self, stdout, stderr) -> Dict[str, int]:
        pass

    def scan(self) -> Dict[str, int]:
        return self.parse_secret_count(*self._get_command_stdout(self.cmd))