import Set_Browser as SB

class Create():
	def __init__(self, driver):
		self.driver = driver
		
    def open_browser(self, url):
        if url == "":
            self.url = "https://www.issta.co.il/"
        else:
            self.url = url
			self.driver.get(self.url)
			self.driver.maximize_window()
        return self.driver


Create().open_browser()