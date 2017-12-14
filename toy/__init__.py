# -*- coding: utf-8 -*-

from .widget import ANCHOR_NUMBER, ANCHOR_NUMBERS
from .widget import Number, RandomInt, Summer, Multiplier, SubprocessSummer, DataFieldExample, DialogExample, Clicker

# Define legit links
ANCHORS = [
    (False, ANCHOR_NUMBER, ANCHOR_NUMBER),
    (False, ANCHOR_NUMBER, ANCHOR_NUMBERS),
    (False, ANCHOR_NUMBERS, ANCHOR_NUMBERS),
]

# Define groups of widgets
WIDGETS = [
    "Input",
    ("#80c0ff", Number, "icon/Number.png"),
    ("#80c0ff", RandomInt, "icon/RandomNumber.png"),
    "Task",
    ("#c080ff", Summer, "icon/Summer.png"),
    ("#c080ff", Multiplier, "icon/Multiplier.png"),
    ("#c080ff", SubprocessSummer, "icon/SubprocessSummer.png"),
    "Examples",
    ("#c0ff80", DataFieldExample, "icon/DataFieldExample.png"),
    ("#80ffc0", DialogExample, "icon/DialogExample.png"),
    "Test",
    ("#ff8080", Clicker, "icon/Clicker.png"),
]
