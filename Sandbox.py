# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Script for researching and experiments                                                                            #
#                                                                                                                   #
# Скрипт для ресёрча и экспериментов                                                                                #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


# TODO: Разобраться как устроен wxPython и попробовать нарисовать адаптивное окно.


# First things, first. Import the wxPython package.
import wx


# Next, create an application object.
app = wx.App()


# Then a frame.
frm = wx.Frame(None, title="Hello World")


# Show it.
frm.Show()


if __name__ == '__main__':
    # Start the event loop.
    app.MainLoop()