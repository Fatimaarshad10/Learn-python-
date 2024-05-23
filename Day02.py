import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Canvas Example")

    # Create a canvas widget
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    for i in range(0, 10):
        canvas.create_oval(i*20, i*20, i*20+20, i*20+20 , fill='black')

    # Display the canvas
    root.mainloop()

if __name__ == "__main__":
    main()