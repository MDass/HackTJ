from bs4 import BeautifulSoup
thepage = "hi"
soup = BeautifulSoup(thepage, "html.parser")
print soup
