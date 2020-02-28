from flask import Flask
from views.home import homeView
from views.app1 import appView1
from views.app2 import appView2


class main(homeView, appView1, appView2):
  """Views controller.
  """

  class App(object):
    """Flask App object.
    """
    app = Flask(__name__)

  def __init__(self):
    # Initialize inherited classes
    homeView.__init__(self)
    appView1.__init__(self)
    appView2.__init__(self)
    self.registerViews()

  def registerViews(self):
    """Decorate inherited views.
    """
    self.App.app.route('/')(self.mainHomeView)
    self.App.app.route('/1')(self.mainAppView1)
    self.App.app.route('/2')(self.mainAppView2)
    
  def run(self):
    self.App.app.run()


if __name__ == "__main__":
  mainApp = main()
  mainApp.run()
