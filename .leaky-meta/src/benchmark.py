# For py2 compat
from __future__ import division
import csv
from io import StringIO
from pathlib import Path
from scanners.scanner import SecretScanner
from scanners.gitleaks import Gitleaks
from scanners.trufflehog import TruffleHog
from scanners.detect_secrets import DetectSecrets

def get_secret_counts():
    '''
    A generator for secrets in default files.
    :returns: filepath, risk_count, informative_count
    '''
    raw_csv = None
    with open('secrets.csv') as f:
        raw_csv = [l for l in f.readlines() 
                            if len(l.strip()) != 0 and not l.startswith('#')]
    # Parse array to CSV
    csv_reader = csv.reader(raw_csv, delimiter=',')
    for row in csv_reader:
        # Yield str, int, int.
        yield [row[0], int(row[1]), int(row[2])]


def build_markdown_rows(scanner: SecretScanner, expected_counts):
    dat = {}
    secrets = scanner.scan()
    for row in expected_counts:
        name = row[0]
        expected = row[1] + row[2]
        if not name in secrets:
            dat[name] = {'name': name, 'found': 0, 'expected': expected, 'false_positives' :0 }
            continue

        found = secrets[name]
        # If found > expected, we have false positives. This will be negative or zero of there's no false positives.
        false_positives = found - expected
        # This will be zero or positive.
        false_positives = max(false_positives, 0)
        dat[name] = {'name': name, 'found': found, 'expected': expected, 'false_positives' :false_positives }
    return dat

def build_table_header(filename_cols):
    template = 'File Name{}|  Found/Total   | False Positives |\n{}|----------------|-----------------|\n'
    # 9 = len('File Name')
    return template.format(' ' * (filename_cols - 9), '-' * filename_cols)

def build_md_table(scanner: SecretScanner):
    # {name}{padding}| {found}/{total} |{false positives}
    print_template = '{}{}| {}/{} | {}\n'

    expected_counts = [x for x in get_secret_counts()]
    # Get the max length of a filename, so we can put a column seperator after it
    sep_col = max([len(val[0]) for val in expected_counts]) + 2
    out = build_table_header(sep_col)
    total_files = len(expected_counts)
    
    md_rows = build_markdown_rows(scanner, expected_counts)
    md_rows = sorted(md_rows.items(), key=lambda val: -val[1]['found'])
    total_finds = 0
    total_expected = 0
    total_false_positives = 0
    files_covered = 0
    for dat in md_rows:
        obj = dat[1]
        name = obj.get('name')
        found = obj.get('found')
        expected = obj.get('expected')
        false_positives = obj.get('false_positives')

        # Determine right padding for name column
        right_padding = sep_col - len(name)
        right_padding_str = (' ' * right_padding)

        # For metrics we exclude false positives.
        total_finds += found - false_positives
        total_expected += expected
        total_false_positives += false_positives
        if found != 0:
            files_covered += 1

        out += print_template.format(name, right_padding_str, found, expected, false_positives)
    return total_files, files_covered, total_finds, total_expected, total_false_positives, out

def build_md(scanner: SecretScanner):
    header_fmt = 'Tool: {}  ' \
                 '\nCommand Used: `{}`  ' \
                 '\nFiles covered: {}/{} ({}% coverage)  ' \
                 '\nTotal finds: {}/{} ({}% coverage)  ' \
                 '\nFalse Positives: {}  ' \
                 '\n\n{}'
    
    total_files, files_covered, total_finds, \
     total_expected, false_positives, table = build_md_table(scanner)
    # Convert cmd to a string
    cmd = ' '.join(scanner.cmd)

    # Get a % coverage value
    file_coverage = (files_covered / total_files) * 100

    find_coverage = (total_finds / total_expected) * 100

    # Sanity!
    file_coverage = round(file_coverage, 2)
    find_coverage = round(find_coverage, 2)
    out = header_fmt.format(scanner.url, cmd,
                           files_covered, total_files, file_coverage, 
                           total_finds, total_expected, find_coverage,
                           false_positives, table)
    return out

if __name__ == '__main__':
    scanners = [Gitleaks(), DetectSecrets(), TruffleHog()]
    for scanner in scanners:
        md = build_md(scanner)
        print(f'Running {type(scanner).__name__}')
        with open(Path('benchmarking') / scanner.report_filename, 'w+') as f:
            f.write(md)
        