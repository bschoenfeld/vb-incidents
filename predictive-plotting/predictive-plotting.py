import csv 
from geopy import geocoders
with open('PredictivePlotting.csv', 'rb') as f:
	with open('PredictivePlotting2.csv', 'wb') as f2:
		reader = csv.reader(f)
		writer=csv.writer(f2)
		count=0
		for row in reader:
			count+=1
			if(count>=1):
				print row[3]
				place, (lat, lng) = geocoders.googlev3.GoogleV3().geocode("{0}, virginia beach, VA".format(row[3]), exactly_one=False)[0]
				print str(lat)+', '+str(lng)
				row.append (lat)
				row.append (lng)
				writer.writerow(row)
