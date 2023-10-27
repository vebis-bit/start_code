import customtkinter
import lager_frontend

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("RadioButtonFrame test")

        self.radio_button_frame_1 = lager_frontend.RadioButtonFrame(self, header_name="RadioButtonFrame 1")
        self.radio_button_frame_1.grid(row=0, column=0, padx=20, pady=20)

        self.frame_1_button = customtkinter.CTkButton(self, text="Print value of frame 1", command=self.print_value_frame_1)
        self.frame_1_button.grid(row=1, column=0, padx=20, pady=10)

    def print_value_frame_1(self):
        print(f"Frame 1 value: {self.radio_button_frame_1.get_value()}")


if __name__ == "__main__":
    app = App()
    app.mainloop()