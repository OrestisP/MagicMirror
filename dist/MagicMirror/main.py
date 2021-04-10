import time
import webbrowser
from filesharer import FileSharer

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder


Builder.load_file('frontend.kv') # the method to connect to the python file to the kivy file


# we will have two screens:

class CameraScreen(Screen):
    def start(self):
        """starts camera widget and changes the Button text"""
        self.ids.camera.play = True  # self.ids gives access to the Widget of the current class!
        self.ids.power_btn.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture # this sets the texture back
                                                                ## to its initial. default state!
        self.ids.camera.opacity = 1

    def stop(self):
        """stops camera widget and changes the Button text"""
        self.ids.camera.play = False
        self.ids.power_btn.text = 'Start Camera'
        self.ids.camera.texture = None  # because by default the texture == the last frame!
        self.ids.camera.opacity = 0

    def capture(self):
        """creates a filename with the current time
         and captures and saves an image under the filename"""
        timestamp = time.strftime('%d-%m-%Y_%H.%M.%S') # = string from time ("%d-%m-%Y-%H:%M:%S")
        self.filepath = f"images/{timestamp}.png" # instead of just filepath, i name it self.filepath.
        # this way i make it an attribute of this class, so that i can inherit it later!
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen' # set the current screen to the next screen,
                                             # so that we switch screens! we access it by the "name"
        self.manager.current_screen.ids.my_image.source = self.filepath
        ## ATTENTION! the above manager.current_screen.ids. gives access to the Widget of the
        ## current screen that user now uses, independently of the widget's class.


class ImageScreen(Screen):
    exception = "Create a link first!" # its a class variable
    def create_link(self):
        """we want to access the image filepath of the previous class.
         We access it with the id of the class:"""
        image_path = App.get_running_app().root.ids.camera_screen.filepath  # camera_screen is the id of the previous class
# this gives the current instance of the CameraScreen class! And we grab the value of "filepath"
# ATTENTION! the filepath becomes an attribute of its class, only if we name it "self.filepath"!!!
        filesharer = FileSharer(filepath=image_path) #first creat an instance, then call the mehtod share:
        self.link = filesharer.share()
        self.ids.label.text = self.link

    def copy_link(self):
        """copy link to the clipboard available for pasting"""
        try: # without try,if the user presses copy without first generating the link, the app will crash
            Clipboard.copy(self.link) # we are not creating an Object instance, we dont have to instantiate that Clipboard Class
                         # because this method is a Classmethod of Clipboard and not an Object method!!!
        except:
            self.ids.label.text = self.exception

    def open_link(self):
        """open link with default browser"""
        try:
            webbrowser.open(self.link)
        except:
            self.ids.label.text = self.exception



# boilerplate classes

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        self.title = 'Mirror mirror on the wall, who is the prettiest of them all?'
        self.icon = 'images/mirror.png'   # has to be located int he directory of main.py
        return RootWidget()



MainApp().run()