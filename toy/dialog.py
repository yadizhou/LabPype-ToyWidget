# -*- coding: utf-8 -*-

from labpype.widget import Dialog


class Number(Dialog):
    def Initialize(self, Sizer):
        self["OUT"] = self.AddLineCtrl(Sizer, "The result is:", "")

    def GetData(self):
        if self.Widget["OUT"] is not None:
            self["OUT"].SetValue(str(self.Widget["OUT"]))
        else:
            self["OUT"].SetValue("")


class MyDialog(Dialog):
    def Initialize(self, Sizer):
        self.AddSectionHead(Sizer, tag="SectionHead", shape="C")
        self["BN"] = self.AddButton(Sizer, label="Button", tag="Click me")
        self["BT"] = self.AddButtonToggle(Sizer, label="ButtonToggle",
                                          tags=("No", "Yes"))
        self["BB"] = self.AddButtonBundle(Sizer, label="ButtonBundle",
                                          choices=list("012345"), rows=2)
        self.AddStaticText(Sizer, label="StaticText",
                           value="Dialog Example")
        self["LC"] = self.AddLineCtrl(Sizer, label="LineCtrl")
        self["TC"] = self.AddTextCtrl(Sizer, label="TextCtrl")
        self["LB"] = self.AddListBox(Sizer, label="ListBox",
                                     choices=list("012345"), selected=3)
        self["PV"] = self.AddPickerValue(Sizer, label="PickerValue",
                                         choices=list("012345"), selected=2)
        self.AddSeparator(Sizer)
        self["PF"] = self.AddPickerFile(Sizer, label="PickerFile")

    def SetData(self):
        self.Widget["BT"] = self["BT"].IsToggled()
        self.Widget["BB"] = self["BB"].GetSelection()
        self.Widget["LC"] = self["LC"].GetValue()
        self.Widget["TC"] = self["TC"].GetValue()
        self.Widget["LB"] = self["LB"].GetStringSelection()
        self.Widget["PV"] = self["PV"].GetSelection()
        self.Widget["PF"] = self["PF"].GetValue()

    def GetData(self):
        if self.Widget["BT"] is not None:
            self["BT"].SetToggle(self.Widget["BT"])
        if self.Widget["BB"] is not None:
            self["BB"].SetSelection(self.Widget["BB"])
        if self.Widget["LC"] is not None:
            self["LC"].SetValue(self.Widget["LC"])
        if self.Widget["TC"] is not None:
            self["TC"].SetValue(self.Widget["TC"])
        if self.Widget["LB"] is not None:
            self["LB"].SetStringSelection(self.Widget["LB"])
        if self.Widget["PV"] is not None:
            self["PV"].SetSelection(self.Widget["PV"])
        if self.Widget["PF"] is not None:
            self["PF"].SetValue(self.Widget["PF"])
