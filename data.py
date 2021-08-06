import csv
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "management.settings")
import django
django.setup()

from lecture.models import Lecture


CSV_PATH = 'static/file/udacity.csv'

with open(CSV_PATH, 'r', newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	s = pd.DataFrame(data_reader)

ss = []
for i in range(len(s)):
	st = (s['title'][i], s['category'][i], s['skill_covered'][i], s['content'][i])
	ss.append(st)
for i in range(len(s)):
	Lecture.objects.create(class_name=ss[i][0], subject=ss[i][1], detail_subject=ss[i][2], content=ss[i][3])
