from tkinter import Tk, Frame
from ttkthemes import ThemedStyle
from container import Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Caja registradora Versión 1.00")
        #self.state("zoomed")
        self.resizable(False, False)
        self.configure(bg="#C6D9E3")
        self.geometry("800x400+120+20")

        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }
        
        self.load_frames()

        self.show_frame(Container)

        self.set_theme()

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def set_theme(self):
        style = ThemedStyle(self)
        style.set_theme("breeze")

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()