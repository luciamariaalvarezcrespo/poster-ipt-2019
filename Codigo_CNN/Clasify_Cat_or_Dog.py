#Poster IPT_ACM_2019
#Autoras: Icia Carro Barallobre && Lucia Alvarez Crespo

############ Librerias #######
from gi.repository import Gtk
import os
import sys
import predict


class Clasify_Cat_or_Dog():
    
    box = None
    window = None
    box_img_topredict = None
    image = None
    
    def __init__(self):
		
        self.window = Gtk.Window()
        self.window.set_title("CNN")
        self.window.set_default_size(100, 75)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect('destroy', self.destroy)

        self.box = Gtk.Box()
        
        self.box.set_spacing(10)
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.window.add(self.box)

        #GIF:
        image = Gtk.Image()
        image.set_from_file("giphy.gif")
        self.box.add(image)

        #Bottom to choose image:
        button = Gtk.Button("Pls, Could you show me a photo (jpeg/jpg) of a cat or a dog?")
        button.connect("clicked", self.on_open_clicked)
        self.box.add(button)

        
        self.window.show_all()

    def on_open_clicked(self, button):
		
        if (not (self.box_img_topredict == None) and (not(self.image == None))):
          self.box.remove(self.box_img_topredict)
          
        self.box_img_topredict = Gtk.Box()       
         
        dialog = Gtk.FileChooserDialog("Open Image", button.get_toplevel(), Gtk.FileChooserAction.OPEN)
        dialog.add_button(Gtk.STOCK_CANCEL, 0)
        dialog.add_button(Gtk.STOCK_OPEN, 1)
        dialog.set_default_response(1)

        filefilter = Gtk.FileFilter()
        filefilter.add_pixbuf_formats()

        dialog.set_filter(filefilter)

        if ((dialog.run() == 1) and 
        ((dialog.get_filename().endswith(".jpeg") or (dialog.get_filename().endswith(".jpg")))== True)):
          
          self.image = Gtk.Image()
          self.image.set_from_file(dialog.get_filename())
          
          self.box_img_topredict.add(self.image)
          self.box_img_topredict.set_size_request(150,150)            
          
          #CNN:
          result = predict.predict(dialog.get_filename())
          if  result == 0:
            button.set_label("I see a CAT, Could you show me a photo (jpeg/jpg) of a cat or a dog? ")
          elif result == 1:
            button.set_label("I see a DOG, Could you show me a photo (jpeg/jpg) of a cat or a dog?")
                

          self.box.add(self.box_img_topredict)
          self.window.show_all()  
        else: 
          button.set_label("It isn't a photo(jpeg/jpg), Could you show me a photo of a cat or a dog?")
        dialog.destroy()

    def destroy(self, window):
        Gtk.main_quit()


def main():
    app = Clasify_Cat_or_Dog()
    Gtk.main()

if __name__ == '__main__':
    main()

