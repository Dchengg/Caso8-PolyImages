class HtmlWriter():

    @classmethod
    def get_path(cls, filename):
        import os
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        filepath = os.path.join(file_dir, '../Resources/' + filename)
        filepath = os.path.abspath(os.path.realpath(filepath))
        return filepath

    @staticmethod
    def write_polygon(filename):
        from bs4 import BeautifulSoup as Soup
        filepath = HtmlWriter.get_path(filename)
        file = open(filepath)
        soup = Soup(file, "html.parser")
        new_poligon = soup.new_tag('polygon')
        new_poligon['points'] = "20,50,600,250,310,90"
        new_poligon['Style'] = "fill: #FADFCA"
        polygons = soup.find('svg')
        polygons.append(new_poligon)
        print(soup)
        with open(filename, "wb") as file:
            file.write(soup.prettify("utf-8"))
        file.close()

    @staticmethod
    def visualize(filename):
        import webbrowser
        filepath = HtmlWriter.get_path(filename)
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(filepath)