import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

categories = []
canada = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "CAN":
			canada.append([int(row[0]), row[5], row[6], row[7]]) # multidemensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

print('total medal for Canada:', len(canada))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')


gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada: 
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('canada won', len(gold_1924), 'gold medals in 1924')
print('canada won', len(gold_1972), 'gold medals in 1972')
print('canada won', len(gold_2014), 'gold medals in 2014')

totalMedals = len(gold_1924) + len(gold_1972) + len(gold_2014)

print('processed', line_count, 'rows of data')

gold_1924_percentage = int(len(gold_1924) / totalMedals * 100)
gold_1972_percentage = int(len(gold_1972) / totalMedals * 100)
gold_2014_percentage = int(len(gold_2014) / totalMedals * 100)

#bar chart

Years = ('1924', '1948', '1972', '2002', '2014')
y_pos = np.arange(len(Years))
performance = [len(gold_1924), len(gold_1948), len(gold_1972), len(gold_2002), len(gold_2014)]

plt.bar(y_pos, performance, align='center', alpha=0.5, color='purple')
plt.xticks(y_pos, Years)
plt.xlabel('Years')
plt.ylabel('Gold Medals')
plt.title('GOLD MEDALS FOR CANADA')

plt.show()