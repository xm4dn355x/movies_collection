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


import gettext
import wx
from math import ceil


ICON_PATH = "X:\\#Work\\Python\\wxGlade-0.9.6\\icons\\wxglade128.ico"


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1280, 720))

        # Menu Bar
        self.main_frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(1, _(u"Выход"), _(u"Выход из программы"))
        self.Bind(wx.EVT_MENU, self.on_exit, id=1)
        self.main_frame_menubar.Append(wxglade_tmp_menu, _(u"Файл"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(3, _(u"Обновить библиотеку"), _(u"Произвести поиск новых файлов на диске"))
        self.Bind(wx.EVT_MENU, self.on_update, id=3)
        wxglade_tmp_menu.Append(4, _(u"Добавить фильм"), _(u"Добавить один, или несколько фильмов в библиотеку"))
        self.Bind(wx.EVT_MENU, self.on_add_film, id=4)
        item = wxglade_tmp_menu.Append(
            wx.ID_ANY,
            _(u"Добавить актера/жанр/студию..."),
            _(u"Добавить новый критерий для сортировки и поиска по библиотеке")
        )
        self.Bind(wx.EVT_MENU, self.on_add_filter, id=item.GetId())
        self.main_frame_menubar.Append(wxglade_tmp_menu, _(u"Библиотека"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(
            6,
            _(u"Настройки программы"),
            _(u"Настроки путей поиска фильмов для библиотеки, интерфейса и т.д.")
        )
        self.Bind(wx.EVT_MENU, self.on_settings, id=6)
        self.main_frame_menubar.Append(wxglade_tmp_menu, _(u"Настройки"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(8, _(u"О программе"), _(u"Координаты автора программы"))
        self.Bind(wx.EVT_MENU, self.on_about, id=8)
        wxglade_tmp_menu.Append(9, _(u"Помощь"), _(u"Как пользоваться программой"))
        self.Bind(wx.EVT_MENU, self.on_help, id=9)
        self.main_frame_menubar.Append(wxglade_tmp_menu, _(u"Справка"))
        self.SetMenuBar(self.main_frame_menubar)
        # Menu Bar end
        self.main_frame_statusbar = self.CreateStatusBar(1)
        self.filter_selector = wx.ComboBox(self, wx.ID_ANY,
                                           choices=[_(u"Актеры"), _(u"Актрисы"), _(u"Режиссеры"), _(u"Студии")],
                                           style=wx.CB_DROPDOWN)
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY,
                                     choices=[_("choice 1"), _("choice 2"), _("choice 3"), _("choice 4"), _("choice 1"),
                                              _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"),
                                              _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"),
                                              _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"), _("choice 1"),
                                              _("choice 1")], style=wx.LB_MULTIPLE | wx.LB_NEEDED_SB | wx.LB_SORT)
        self.films_panel = wx.ScrolledWindow(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):
        self.SetTitle(_(u"Коллекция фильмов"))
        self.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "JetBrains Mono"))
        self.main_frame_statusbar.SetStatusWidths([-1])

        # statusbar fields
        main_frame_statusbar_fields = [_("main_frame_statusbar")]
        for i in range(len(main_frame_statusbar_fields)):
            self.main_frame_statusbar.SetStatusText(main_frame_statusbar_fields[i], i)
        self.filter_selector.SetMinSize((170, 25))
        self.filter_selector.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "JetBrains Mono"))
        self.filter_selector.SetSelection(1)
        self.list_box_1.SetMinSize((170, -1))
        self.films_panel.SetScrollRate(10, 10)


    def __do_layout(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        filters_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _(u"Фильтры:")), wx.VERTICAL)
        filters_sizer.Add(self.filter_selector, 0, 0, 0)
        filters_sizer.Add(self.list_box_1, 1, 0, 0)
        main_sizer.Add(filters_sizer, 0, wx.EXPAND, 0)
        self.films_panel.SetSizer(self.draw_content())
        main_sizer.Add(self.films_panel, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer)
        self.Layout()
        self.Bind(wx.EVT_SIZE, self.on_resize)


    def on_exit(self, event):  # wxGlade: MainFrame.<event_handler>
        """Close the frame, terminating the application."""
        self.Close(True)

    def on_update(self, event):  # wxGlade: MainFrame.<event_handler> # TODO: Написать функционал обновления БД
        print("Event handler 'on_update' not implemented!")
        event.Skip()

    def on_add_film(self, event):  # wxGlade: MainFrame.<event_handler> # TODO: Написать функционал добавления файла в бд
        print("Event handler 'on_add_film' not implemented!")
        event.Skip()

    def on_add_filter(self, event):  # wxGlade: MainFrame.<event_handler> # TODO: Написать функционал добавления фильтра
        print("Event handler 'on_add_filter' not implemented!")
        event.Skip()

    def on_settings(self, event):  # wxGlade: MainFrame.<event_handler> # TODO: Реализовать настройки
        print("Event handler 'on_settings' not implemented!")
        event.Skip()

    def on_about(self, event):  # wxGlade: MainFrame.<event_handler>
        """Display an About Dialog"""
        wx.MessageBox("MIT License\nCopyright (c) 2020 Michael Nikitenko\n\nhttps://github.com/xm4dn355x/",
                      "О программе", wx.OK | wx.ICON_INFORMATION)

    def on_help(self, event):  # wxGlade: MainFrame.<event_handler> # TODO: Реализовать справку
        print("Event handler 'on_help' not implemented!")
        event.Skip()

    def on_resize(self, event): # TODO: Разобраться с ресайзом
        size = self.GetSize()
        print(f"on_resize is working! size = {size}")
        print(event)
        self.Layout()

    def draw_content(self):
        # TODO: Написать коннект к БД
        db_data = [
            {'preview': ICON_PATH, 'title': 'Тест 1', 'tags': ['порно', 'весело', 'задорно']},
            {'preview': ICON_PATH, 'title': 'Тест 2', 'tags': ['порно', 'весело', 'задорно']},
            {'preview': ICON_PATH, 'title': 'Тест 3', 'tags': ['порно', 'весело', 'задорно']},
            {'preview': ICON_PATH, 'title': 'Тест 4', 'tags': ['порно', 'весело', 'задорно']},
            {'preview': ICON_PATH, 'title': 'Тест 5', 'tags': ['']},
            {'preview': ICON_PATH, 'title': 'Тест 6', 'tags': ['порно']},
            {'preview': ICON_PATH, 'title': 'Тест 7', 'tags': []},
            {'preview': ICON_PATH, 'title': 'Тест 8', 'tags': ['порно', 'весело', 'задорно']},
            {'preview': ICON_PATH, 'title': 'Тест 9', 'tags': ['порно', 'весело', 'задорно']},
        ]

        size = self.GetSize()
        cols = int((size.x - 170)/320)
        rows = len(db_data)/cols
        print(rows)
        rows = int(ceil(rows))
        grid_films_sizer = wx.GridSizer(rows, cols, 0, 0)

        for data in db_data:
            film_sizer = wx.BoxSizer(wx.VERTICAL)
            preview_path = data['preview']
            preview = wx.BitmapButton(self.films_panel, wx.ID_ANY, wx.Bitmap(preview_path, wx.BITMAP_TYPE_ANY))
            preview.SetMinSize((320, 180))
            film_sizer.Add(preview, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
            film_title = wx.StaticText(self.films_panel, wx.ID_ANY, _(data['title']), style=wx.ALIGN_CENTER)
            film_title.SetMinSize((320, 36))
            film_sizer.Add(film_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
            hor_divider = wx.StaticLine(self.films_panel, wx.ID_ANY)
            film_sizer.Add(hor_divider, 0, wx.EXPAND, 0)
            tags = ''
            if len(data['tags']) == 1:
                tags = data['tags'][0]
            else:
                for tag in data['tags']:
                    tags = tags + f'{tag}, '
            film_tags = wx.StaticText(self.films_panel, wx.ID_ANY, _(tags), style=wx.ALIGN_CENTER)
            film_tags.SetMinSize((320, 54))
            film_sizer.Add(film_tags, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
            grid_films_sizer.Add(film_sizer, 1, wx.EXPAND, 0)
        return grid_films_sizer


class McApp(wx.App):
    def OnInit(self):
        self.main_frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True


if __name__ == "__main__":
    gettext.install("movies_collection")  # replace with the appropriate catalog name

    movies_collection = McApp(0)
    movies_collection.MainLoop()
