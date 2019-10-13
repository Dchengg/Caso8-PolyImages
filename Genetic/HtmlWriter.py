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
        for point in polygon.points:
            points = points + str(point.x) + ',' + str(point.y) + ','
        new_polygon['points'] = points
        new_polygon['Style'] = "fill: " + '#%02x%02x%02x' % (polygon.color[0], polygon.color[1], polygon.color[2])
        polygons = soup.find('svg')
        polygons.append(new_polygon)
        with open(filepath, "wb") as file:
            file.write(soup.prettify("utf-8"))
        file.close()

    @staticmethod
    def reset_html(filename):
        from bs4 import BeautifulSoup as Soup
        filepath = HtmlWriter.get_path(filename)
        file = open(filepath)
        soup = Soup(file, "html.parser")
        soup.svg.decompose()
        new_svg = soup.new_tag('svg')
        new_svg['class'] = "polyImage"
        new_svg['data-name'] = "Layer 1"
        new_svg['viewbox'] = "0 0 1024 1024"
        html= soup.find('html')
        html.append(new_svg)
        with open(filepath, "wb") as file:
            file.write(soup.prettify("utf-8"))
        file.close()

    @staticmethod
    def visualize(filename):
        import webbrowser
        filepath = HtmlWriter.get_path(filename)
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.open(filepath)

