#!/usr/bin/python3

import pytest
import pygibank

window = pygibank.startup(testing=True)

def test_window_title():
    window.set_title("new title")
