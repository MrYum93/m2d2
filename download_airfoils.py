import urllib2
import urllib

def main():
	standard_url = 'http://airfoiltools.com/polar/csv?polar=xf-' #then later add the csv download file eg: ag04-il-50000

	response = urllib2.urlopen('http://airfoiltools.com/search/airfoils')
	html = response.read()
	#with open(html) as f:
	i = 0
	#for line in html.readlines():
	#	i = i + 1
	#	print(line + ' stringlen: ' + str(i))
	#print(html)
	#print("test")
	urllib.urlretrieve ('http://airfoiltools.com/search/airfoils', "airfoil_html.txt")
	with open('airfoil_html.txt', 'r') as f:
		for line in f:
			break
			#print(str(i) + ': ' + line)
			i = i + 1
			if line.startswith('<tr><td class="link"><a href="/airfoil/details?airfoil') > 0 :
				#print(len('<tr><td class="link"><a href="/airfoil/details?airfoil'))
				airfoil_name = line[55:]

				airfoil_name = airfoil_name.split("\"")
				#print(airfoil_name[0])
				#print(str(i) + ': ' + airfoil_name)
				#print(str(i) + ': ' + str(line.find('<tr><td class="link"><a href="/airfoil/details?airfoil=')))
				
				file_50_name = airfoil_name[0] + "_50.txt"
				file_100_name =  airfoil_name[0] + "_100.txt"
				csv_50 = standard_url + airfoil_name[0] + '-50000'
				csv_100 = standard_url + airfoil_name[0] + '-100000'
				#https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
				urllib.urlretrieve (csv_50, file_50_name)
				urllib.urlretrieve (csv_100, file_100_name)
				print("file created")

	airfoil_file = open('airfoil_list', 'wa+')
	with open('airfoil_web.txt', 'r') as f:
		for line in f:
			if line.startswith('<tr><td class="link"><a href="/airfoil/details?airfoil') > 0 :
				airfoil_name = line[55:]
				airfoil_name = airfoil_name.split("\"")
				airfoil_file.write(airfoil_name[0] + "\n")
		airfoil_file.close()
				


	return 0

if __name__ == '__main__':
    main()
