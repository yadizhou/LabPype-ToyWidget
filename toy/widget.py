# -*- coding: utf-8 -*-

import wx
import os
import subprocess
from random import randint
from time import sleep

from labpype.widget import Widget, ANCHOR_REGULAR
from labpype.widget.field import *

# Import the dialogs for our widgets
from . import dialog as Di

# Get the path of the application
MAIN_PATH = os.path.dirname(os.path.realpath(__file__))
Here = lambda f="": os.path.join(MAIN_PATH, f)


# Define some anchor types here
class ANCHOR_NUMBER(ANCHOR_REGULAR):
    pass


class ANCHOR_NUMBERS(ANCHOR_REGULAR):
    pass


# Now we define some widgets
class Number(Widget):
    NAME = "Number"
    DIALOG = "V"
    INTERNAL = FloatField(key="NUMBER", label="")
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        if self["OUT"] is not None:
            return str(self["OUT"])

    def Task(self):
        return self["NUMBER"]


class RandomInt(Widget):
    NAME = "Random Integer"
    DIALOG = "V"
    INTERNAL = IntegerField(key="MIN", label="Min"), IntegerField(key="MAX", label="Max")
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        if self["OUT"] is not None:
            return str(self["OUT"])

    def Task(self):
        return randint(self["MIN"], self["MAX"])


class Summer(Widget):
    NAME = "Summer"
    DIALOG = Di.Number
    THREAD = True
    INCOMING = ANCHOR_NUMBERS, "NUMBERS", True, "LTB", "Number"
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        if self.IsState("Done"):
            return "+".join(str(i) for i in self["NUMBERS"]) + "=" + str(self["OUT"])

    def Task(self):
        p = 0
        for i in self["NUMBERS"]:
            # sleep(0.5)
            self.Checkpoint()
            p += i
        return p


# -------------------------------------------------------- #
class Multiplier(Widget):
    NAME = "Multiplier"
    DIALOG = Di.Number
    THREAD = True
    INCOMING = ANCHOR_NUMBERS, "NUMBERS", True, "LTB", "Number"
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        if self.IsState("Done"):
            return "*".join(str(i) for i in self["NUMBERS"]) + "=" + str(self["OUT"])

    def Task(self):
        p = 1
        n = len(self["NUMBERS"])
        for index, i in enumerate(self["NUMBERS"]):
            # sleep(1)
            self.Checkpoint("%s/%s" % (index + 1, n))
            p *= i
        return p


class SubprocessSummer(Widget):
    NAME = "Subprocess Summer"
    DIALOG = {"ORIENTATION": "V", "SIZE": (120, -1)}
    THREAD = True
    INCOMING = ANCHOR_NUMBERS, "NUMBERS", True, "LTB", "Number"
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        if self.IsState("Done"):
            return str(self["OUT"])

    def Task(self):
        t = self.GetThread()
        p = subprocess.Popen(["python", Here("dummyprocess.py"), *(str(i) for i in self["NUMBERS"])], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while p.poll() is None:
            sleep(1)
            if t.stop:
                p.kill()
                t.Checkpoint()
        if p.returncode == 0:
            return float(p.stdout.read().strip())


# -------------------------------------------------------- #
class Provider(Widget):
    NAME = "Provider"
    DIALOG = "V"
    SINGLETON = True

    def Name(self):
        return str(self["OUT"])

    def Task(self):
        return randint(0, 9)


class Receiver(Widget):
    NAME = "Receiver"
    DIALOG = "V"
    PROVIDER = Provider, "X10"
    OUTGOING = ANCHOR_NUMBER

    def Name(self):
        return str(self["OUT"])

    def Task(self):
        return randint(0, 9) + self["X10"] * 10


# -------------------------------------------------------- #
class DataFieldExample(Widget):
    NAME = "DataField Example"
    DIALOG = "V"  # Automatically generate dialog using vertical layout
    INTERNAL = \
        BooleanField("BOOLEAN", "BooleanField", "No", "Yes"), \
        LineField("LINE", "LineField"), \
        TextField("TEXT", "TextField"), \
        IntegerField("INTEGER", "IntegerField"), \
        FloatField("FLOAT", "FloatField"), \
        ChoiceField("CHOICE1", "ChoiceField", choices=list("ABC"), widget="C"), \
        ChoiceField("CHOICE2", "ChoiceField", choices=list("ABC"), widget="L"), \
        ChoiceField("CHOICE3", "ChoiceField", choices=list("ABC"), widget="B"), \
        FileField("FILE", "FileField", )


class DialogExample(Widget):
    NAME = "Dialog Example"
    DIALOG = Di.MyDialog
    INTERNAL = "BT", "BB", "LC", "TC", "LB", "PV", "PF"


# -------------------------------------------------------- #
class Clicker(Widget):
    NAME = "Clicker"
    THREAD = True
    DIALOG = "V"

    def Task(self):
        while 1:
            sleep(0.01)
            n = randint(0, len(self.Canvas.Widget) - 1)
            w = self.Canvas.Widget[n]
            if w.__class__ != self.__class__:
                x = randint(0, 1)
                with self.Canvas.Lock:
                    wx.CallAfter(w.OnAlter)
                    if x:
                        wx.CallAfter(w.OnBegin)
            self.Checkpoint()
