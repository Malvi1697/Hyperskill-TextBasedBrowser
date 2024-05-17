import os
class Website:
    webpages_url_history = []
    def __init__(self, webpage_url, webpages_list, dir_name):
        self.dir_name = dir_name
        self.webpage_url = webpage_url
        self.webpages_list = webpages_list


    def stripped(self):
        return self.webpage_url.split(".")[0]

    def print_website(self):
        print(self.__str__())

    def make_tab(self):
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            print("File already exists")

        with open(self.dir_name + "/" + self.stripped(), "w") as url_text_file:
            url_text_file.write(self.__str__())

    def __str__(self):
        for webpage in self.webpages_list:
            if self.webpage_url in webpage:
                webpage = self.webpages_list[(self.webpages_list.index(webpage)) + 1]
                break
        return webpage
