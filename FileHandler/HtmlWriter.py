class HtmlWriter():

    @classmethod
    def get_path(cls, filename):
        import os
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        filepath = os.path.join(file_dir, '../Resources/' + filename)
        filepath = os.path.abspath(os.path.realpath(filepath))
        return filepath


    @staticmethod
    def write_polygon(filename, string):
        from bs4 import BeautifulSoup as Soup
        filepath = HtmlWriter.get_path(filename)
        file = open(filepath)
        soup = Soup(file, "html.parser")
        polygons = soup.find('svg')
        convertString = Soup(string, 'html.parser')
        polygons.append(convertString)
        with open(filepath, "wb") as file:
            file.write(soup.prettify("utf-8"))
        file.close()

    @staticmethod
    def writeGen(filename, string, gen_number):
        from bs4 import BeautifulSoup as Soup
        filepath = HtmlWriter.get_path(filename)
        file = open(filepath)
        soup = Soup(file, "html.parser")
        polygons = soup.find('svg')
        new_gen = soup.new_tag('gen'+str(gen_number))
        polygons.append(new_gen)
        convert_string = Soup(string, 'html.parser')
        new_gen.append(convert_string)
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
        new_svg['viewbox'] = "0 0 1920 1080"
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

