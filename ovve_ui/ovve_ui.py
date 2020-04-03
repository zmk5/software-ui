import argparse
import datetime
import os
import sys
from copy import deepcopy
from random import randint
from typing import Union, Optional, Tuple

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtSerialPort, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QAbstractButton, QApplication, QHBoxLayout,
                             QLabel, QPushButton, QStackedWidget, QVBoxLayout,
                             QWidget)

from display.button import FancyDisplayButton, SimpleDisplayButton
from display.change import Change
from display.rectangle import DisplayRect
from display.ui_settings import (DisplayRectSettings,
                                 FancyButtonSettings,
                                 SimpleButtonSettings,
                                 TextSetting,
                                 UISettings)
from display.widgets import (initializeHomeScreenWidget,
                             initializeModeWidget,
                             initializeRespitoryRateWidget,
                             initializeMinuteVolumeWidget,
                             initializeIERatioWidget)
from utils.params import Params
from utils.settings import Settings


class MainWindow(QWidget):
    def __init__(self, debug: bool = True) -> None:
        super().__init__()
        self.settings = Settings()
        self.local_settings = Settings()  # local settings are changed with UI
        self.params = Params()

        if debug:
            self.settings.set_test_settings()
            self.local_settings.set_test_settings()
            self.params.set_test_params()

        # you can pass new settings for different object classes here
        self.ui_settings = UISettings()
        # Example 1 (changes color of Fancy numbers to red)
        # self.ui_settings.set_fancy_button_settings(FancyButtonSettings(valueColor=Qt.red))
        # Example 2 (changes color of Simple numbers to red)
        # self.ui_settings.set_simple_button_settings(SimpleButtonSettings(valueColor=Qt.red))

        # Example 3 (sets display rect label font to Comic Sans MS)
        # self.ui_settings.set_display_rect_settings(DisplayRectSettings(labelSetting = TextSetting("Comic Sans MS", 20, True)))

        self.ptr = 0

        self.setFixedSize(800, 480)  # hardcoded (non-adjustable) screensize
        self.stack = QStackedWidget(self)

        self.page = {
            "1": QWidget(),
            "2": QWidget(),
            "3": QWidget(),
            "4": QWidget(),
            "5": QWidget(),
        }

        self.initalizeAndAddStackWidgets()
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

    def makeFancyDisplayButton(
            self, label: str, value: Union[int, float], unit: str,
            size: Optional[Tuple[int, int]] = None) -> FancyDisplayButton:
        """ Creates Fancy Display Button """
        return FancyDisplayButton(
            label,
            value,
            unit,
            parent=None,
            size=size,
            button_settings=self.ui_settings.fancy_button_settings)

    def makeSimpleDisplayButton(
            self, label: str,
            size: Optional[Tuple[int, int]] = None) -> SimpleDisplayButton:
        """ Creates Simple Display Button """
        return SimpleDisplayButton(
            label,
            parent=None,
            size=size,
            button_settings=self.ui_settings.simple_button_settings)

    def makeDisplayRect(
            self, label: str, value: Union[int, float], unit: str,
            size: Optional[Tuple[int, int]] = None) -> DisplayRect:
        """ Creates the Display Rectangle """
        return DisplayRect(
            label,
            value,
            unit,
            parent=None,
            size=size,
            rect_settings=self.ui_settings.display_rect_settings)

    def initalizeAndAddStackWidgets(self) -> None:
        initializeHomeScreenWidget(self)
        initializeModeWidget(self)
        initializeRespitoryRateWidget(self)
        initializeMinuteVolumeWidget(self)
        initializeIERatioWidget(self)
        for i in self.page:
            self.stack.addWidget(self.page[i])

    def display(self, i: int) -> None:
        self.stack.setCurrentIndex(i)

    def update_main_page_ui(self) -> None:
        self.updateMainDisplays()
        self.updateGraphs()

    def updateMainDisplays(self) -> None:
        self.mode_button_main.updateValue(self.settings.get_mode_display())
        self.resp_rate_button_main.updateValue(self.settings.resp_rate)
        self.minute_vol_button_main.updateValue(self.settings.minute_volume)
        self.ie_button_main.updateValue(self.settings.get_ie_display())
        self.peep_display_main.updateValue(self.params.peep)
        self.tv_insp_display_main.updateValue(self.params.tv_insp)
        self.tv_exp_display_main.updateValue(self.params.tv_exp)
        self.ppeak_display_main.updateValue(self.params.ppeak)
        self.pplat_display_main.updateValue(self.params.pplat)

    def updatePageDisplays(self) -> None:
        self.mode_page_rect.updateValue(self.settings.get_mode_display())
        self.resp_rate_page_rect.updateValue(self.settings.resp_rate)
        self.minute_vol_page_rect.updateValue(self.settings.minute_volume)
        self.ie_page_rect.updateValue(self.settings.get_ie_display())

    # TODO: Polish up and process data properly
    def updateGraphs(self) -> None:
        self.tv_insp_data[:-1] = self.tv_insp_data[1:]
        self.tv_insp_data[-1] = self.params.tv_insp
        self.flow_graph_line.setData(self.tv_insp_data)
        self.ptr += 1
        self.flow_graph_line.setPos(self.ptr, 0)
        QtGui.QApplication.processEvents()

    def open_serial(self) -> None:
        if not self.serial.isOpen():
            self.serial.open(QtCore.QIODevice.ReadWrite)

    def close_serial(self) -> None:
        if self.serial.isOpen():
            self.serial.close()

    def start_serial(self, serialport: str) -> None:
        #TODO: error checking, retry
        self.serial = QtSerialPort.QSerialPort(
            serialport,
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive,
        )
        self.open_serial()

    @QtCore.pyqtSlot()
    def receive(self) -> None:
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip("\r\n")
            try:
                self.parseInputAndUpdate(text)
            except:
                pass

    # TODO: Map add all other input data to proper settings

    def parseInputAndUpdate(self, text: str) -> None:
        self.params.tv_insp = int(text)
        # print(text)
        self.update_main_page_ui()

    # TODO: Finish all of these for each var
    def changeMode(self, new_val: bool) -> None:
        self.local_settings.ac_mode = new_val
        self.mode_page_rect.updateValue(self.local_settings.get_mode_display())

    # TODO: Figure out how to handle increment properly
    # (right now it's not in the settings)
    def incrementRespRate(self) -> None:
        self.local_settings.resp_rate += self.settings.resp_rate_increment
        self.resp_rate_page_rect.updateValue(self.local_settings.resp_rate)

    def decrementRespRate(self) -> None:
        self.local_settings.resp_rate -= self.settings.resp_rate_increment
        self.resp_rate_page_rect.updateValue(self.local_settings.resp_rate)

    def incrementMinuteVol(self) -> None:
        self.local_settings.minute_volume += self.settings.minute_volume_increment
        self.minute_vol_page_rect.updateValue(
            self.local_settings.minute_volume)

    def decrementMinuteVol(self) -> None:
        self.local_settings.minute_volume -= self.settings.minute_volume_increment
        self.minute_vol_page_rect.updateValue(
            self.local_settings.minute_volume)

    def changeIERatio(self, new_val: int) -> None:
        self.local_settings.ie_ratio_id = new_val
        self.ie_page_rect.updateValue(self.local_settings.get_ie_display())

    # TODO: Finish all of these for each var
    def commitMode(self):
        self.logChange(
            Change(
                datetime.datetime.now(),
                "Mode",
                self.settings.get_mode_display(),
                self.local_settings.get_mode_display(),
            ))
        self.settings.ac_mode = self.local_settings.ac_mode
        self.mode_button_main.updateValue(self.settings.get_mode_display())
        self.stack.setCurrentIndex(0)

    def commitRespRate(self) -> None:
        self.logChange(
            Change(
                datetime.datetime.now(),
                "Resp. Rate",
                self.settings.resp_rate,
                self.local_settings.resp_rate,
            ))
        self.settings.resp_rate = self.local_settings.resp_rate
        self.resp_rate_button_main.updateValue(self.settings.resp_rate)
        self.stack.setCurrentIndex(0)

    def commitMinuteVol(self) -> None:
        self.logChange(
            Change(
                datetime.datetime.now(),
                "Minute Vol",
                self.settings.minute_volume,
                self.local_settings.minute_volume,
            ))
        self.settings.minute_volume = self.local_settings.minute_volume
        self.minute_vol_button_main.updateValue(self.settings.minute_volume)
        self.stack.setCurrentIndex(0)

    def commitIERatio(self) -> None:
        self.logChange(
            Change(
                datetime.datetime.now(),
                "I/E Ratio",
                self.settings.get_ie_display(),
                self.local_settings.get_ie_display(),
            ))
        self.settings.ie_ratio_id = self.local_settings.ie_ratio_id
        self.ie_button_main.updateValue(self.settings.get_ie_display())
        self.stack.setCurrentIndex(0)

    def cancelChange(self) -> None:
        self.local_settings = deepcopy(self.settings)
        self.updateMainDisplays()
        self.stack.setCurrentIndex(0)
        self.updatePageDisplays()

    def passChanges(self, param, new_val) -> None:
        pass
        # TODO: pass settings to the Arduino

    def logChange(self, change: Change) -> None:
        if change.old_val != change.new_val:
            print(change.display())
        # TODO: Actually log the change in some data structure


def main(port, argv) -> None:
    app = QApplication(argv)
    window = MainWindow()

    window.start_serial(port)
    window.show()
    app.exec_()
    window.close_serial()
    sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Start the OVVE user interface')
    parser.add_argument('-p',
                        '--port',
                        help='Serial port for communication with Arduino')
    args = parser.parse_args()

    main(args.port, sys.argv)