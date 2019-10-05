class HtmlWriter():

    @classmethod
    def get_path(cls, filename):
        import os
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        filepath = os.path.join(file_dir, '../Resources/' + filename)
        filepath = os.path.abspath(os.path.realpath(filepath))
        return filepath

    @staticmethod
    def write_polygon(filename, polygon):
        from bs4 import BeautifulSoup as Soup
        filepath = HtmlWriter.get_path(filename)
        file = open(filepath)
        soup = Soup(file, "html.parser")
        new_polygon = soup.new_tag('polygon')
        points = ''
        print(polygon.points)
        for pair in polygon.points:
            points = points + str(pair[0]) + ',' + str(pair[1]) + ','
        new_polygon['points'] = points
        new_polygon['Style'] = "fill: " + polygon.color
        polygons = soup.find('svg')
        polygons.append(new_polygon)
        print(soup)
        with open(filepath, "wb") as file:
            file.write(soup.prettify("utf-8"))
        file.close()

    @staticmethod
    def visualize(filename):
        import webbrowser
        filepath = HtmlWriter.get_path(filename)
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(filepath)