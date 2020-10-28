# -*- coding: utf-8 -*-
from flask import Flask
from views.home import HomeView
from views.app1 import AppView1
from views.app2 import AppView2


class Main(HomeView, AppView1, AppView2):
    """Views controller.
    """

    class App(object):
        """Flask App object.
        """
        app = Flask(__name__)

    def __init__(self):
        # Initialize inherited classes
        HomeView.__init__(self)
        AppView1.__init__(self)
        AppView2.__init__(self)
        self.register_views()

    def register_views(self):
        """Decorate inherited views.
        """
        self.App.app.route('/', methods=["GET", "POST"])(self.main_home_view)
        self.App.app.route('/1', methods=["GET", "POST"])(self.main_app_view_1)
        self.App.app.route('/2', methods=["GET", "POST"])(self.main_app_view_2)
    
    def run(self):
        self.App.app.run()


if __name__ == "__main__":
    mainApp = Main()
    mainApp.run()
