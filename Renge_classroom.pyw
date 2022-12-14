#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main program for automated testing

import tkinter as tk
import modules.classroom as classroom

VERSION = 'V0.1'

# Start GUI & set icon
root = tk.Tk()
# TODO: Create and use an icon later
# img = tk.Image("photo", file="./etc/logo.png")
# root.tk.call('wm', 'iconphoto', root._w, img)


# Important to keep object saved locally to preserve variables
c = classroom.Classroom(root, VERSION)


root.mainloop()
