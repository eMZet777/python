"""
pip - pip installs  packages - instalator  pakunkow

PyPi - Puthon Package index - indeks (spis) pakunkow do Pythona

"""





import requests
 
###############################################################
 
def file_to_list(_list, file_to_change):
    with open(file_to_change, "r", encoding="UTF-8") as file:
        for line in file:
            _list.append(line.replace("\n", ""))
        return _list
            
###############################################################
    
pages = []
working_pages = []
 
pages = file_to_list(pages, "pages_www.txt")
 
for slot in pages:
    try:
        page = requests.get(slot)
        if (page.status_code == 200):
            working_pages.append(slot)
    except:
        #Webside does not work
        None
 
print(pages)
print(working_pages)
