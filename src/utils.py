import os
import subprocess

url_top = "https://www.levels.fyi/comp.html"

DF_COLUMNS = ["Job", "Company", "Country", "Region", "City",
              "Date", "Level", "Tag", "Years Comp",
              "Years Xp", "Compensation", "Base",
              "Stock", "Bonus", "Nego Gain"]

FOLDER_PROJECT = os.path.join(os.path.expanduser('~') + '/scraper-levels.fyi/')
FOLDER_DB = os.path.join(FOLDER_PROJECT, "db")
FOLDER_SRC = os.path.join(FOLDER_PROJECT, "src")
FOLDER_RES = os.path.join(FOLDER_PROJECT, "res")
FOLDER_LOGS = os.path.join(FOLDER_PROJECT, "logs")
FILE_OUT = os.path.join(FOLDER_LOGS, "update_logs.txt")


def format_salary(s):
	if '$' in s:
		return float(s.split(',')[0][1:])
	if "N" in s:
		return 0
	return float(s[:-1])


def format_date(d):
	revers = d.split("/")[::-1]
	a = revers[0] if len(revers[0]) == 2 else "0" + revers[0]
	b = revers[1] if len(revers[1]) == 2 else "0" + revers[1]
	c = revers[2] if len(revers[2]) == 2 else "0" + revers[2]
	return a + "/" + c + "/" + b


def write_log_file(log_txt):
	with open(FILE_OUT, "r+") as file:
		prev_file = file.read()
		file.seek(0)
		file.write(log_txt + prev_file)
		file.close()


def lap_finished(r, prev_r, curr_r, tol=1):
	try:
		summ = sum([int(r[i] == prev_r[0][i]) for i in range(len(r))])
		return summ >= 15 - tol, curr_r + [r] + prev_r[1:]
	except IndexError:
		try:
			summ = sum([int(r[i] == curr_r[0][i]) for i in range(len(r))])
			return summ >= 15 - tol, [r] + curr_r[1:] + prev_r
		except IndexError:
			return False, 0


def send_mail_if_error(category, new_row):
	recipient = 'yourfa@protonmail.com'
	subject = f'Error for {category}'
	subprocess.Popen(['mail', '-s', subject, recipient], stdin=subprocess.PIPE).communicate(str(new_row).encode('ascii'))
	return
