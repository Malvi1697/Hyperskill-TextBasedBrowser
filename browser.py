import sys
from website import Website

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''




webpage_url = None
webpages_list = ["nytimes.com", nytimes_com, "bloomberg.com", bloomberg_com]

# args = sys.argv
# dir_name = args[1]
dir_name = "tb_tabs"

while True:
    check = False
    webpage_url = input()

    if webpage_url == "back":
        try:
            site.webpages_url_history.pop()
            webpage_url = site.webpages_url_history[-1]
            site = Website(webpage_url, webpages_list, dir_name)
            site.print_website()
            site.make_tab()
        except Exception:
            pass

    elif webpage_url == "exit":
        break

    else:
        for webpage in webpages_list:
            if webpage_url in webpage:
                check = True
        if check:
            site = Website(webpage_url, webpages_list, dir_name)
            site.print_website()
            site.make_tab()
            site.webpages_url_history.append(site.stripped())
        else:
            print("Invalid URL")
