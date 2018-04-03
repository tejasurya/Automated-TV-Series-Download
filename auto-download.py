from selenium import webdriver 

#from selenium.webdriver.common.keys import keys

for j in range(7,8):
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	#set the path link to be stored
	path='E:\Simpsons\s'+str(j)
	#path='E:\Stranger Things\s1'
	profile.set_preference("browser.download.dir", path)
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

	browser=webdriver.Firefox(firefox_profile=profile)
	#set the download link
	#link='http://dl6.downloadoo.ir/TV.Show/S/Stranger%20Things/S01/'
	if j<=10:
		link='http://dl6.downloadoo.ir/TV.Show/T/The%20Simpsons/S0'+str(j)+'/'
	elif j>10:
		link='http://dl6.downloadoo.ir/TV.Show/T/The%20Simpsons/S'+str(j)+'/'
	browser.get(link)
	text=''
	limit=[0,0,23,25,23,23,26,25,26,26]
	for i in range(10,limit[j]):
		'''
		if i<=5:

			text='Stranger.Things.S01E0'+str(i)+'.720p-[Nightsdl.com].mkv'
		elif i>5:
			text='Stranger.Things.S01E0'+str(i)+'.720p-[Downloadoo.org].mkv'
			'''
		if i<10:
			#text is the ahref link to be clicked for downloading 
			text='The.Simpsons.[Nightsdl.Com].S0'+str(j)+'E0'+str(i)+'.mkv'
		elif i>=10:
			text='The.Simpsons.[Nightsdl.Com].S0'+str(j)+'E'+str(i)+'.mkv'
		download= browser.find_element_by_link_text(text)
		browser.implicitly_wait(10)
		download.click()
 