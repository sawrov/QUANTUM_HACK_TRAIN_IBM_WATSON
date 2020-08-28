#make csv to train

import csv
huha="this"
with open('train_diseases.csv', mode='w') as csv_file:
	csv_writer=csv.writer(csv_file,delimiter=",")
	with open('filtered_final_list.txt') as diseases:
		for disease in diseases:
			csv_writer.writerow(['object_of_interest',disease])