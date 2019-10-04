from logic.HtmlWriter import HtmlWriter


def main():
    HtmlWriter.write_polygon("PolyImage.html")
    HtmlWriter.visualize("PolyImage.html")

if __name__ == "__main__":
    main()
