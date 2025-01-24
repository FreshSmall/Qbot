import wx
import wx.html2 as web


class WebPanel(wx.Panel):
    def __init__(self, parent, id=-1):
        super(WebPanel, self).__init__(parent, id)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)
        self.browser = web.WebView.New(self)
        vbox.Add(self.browser, proportion=-1, flag=wx.EXPAND | wx.ALL, border=10)

    def show_url(self, url):
        self.browser.LoadURL(url)

    def show_file(self, filename):
        with open(filename, "r") as f:
            html_cont = f.read()
            self.browser.SetPage(html_cont, "")
            self.browser.Show()


if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, title="WebPanel")
    web = WebPanel(frame)
    web.show_url("https://danjuanapp.com/djmodule/value-center")
    frame.Show()
    app.MainLoop()
