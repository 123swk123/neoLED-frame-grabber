import argparse
import logging
from PyQt5 import QtCore, QtGui, QtQuick, QtWidgets, QtSerialPort
import os
import sys
import pathlib
import time
from collections import deque

class neoLED_FrameGrabber(QtCore.QObject):
    # callBackObj = None
    newFrame = QtCore.pyqtSignal('QVector<int>')

    def __init__(self, iodev, ledFrameBytes, ledColorChBytes, colorConv, verbose = False, parent = None):
        super().__init__(parent)

        self.logger = logging.getLogger('neoLED_FrameGrabber')
        logger.setLevel(logging.CRITICAL if verbose == False else logging.WARNING)

        # self.iodev = QtSerialPort.QSerialPort()
        self.iodev = iodev
        self.ledFrameBytes = ledFrameBytes
        self.ledColorChBytes = ledColorChBytes
        self.colorSpaceConv = colorConv
        self.buffOvrFlow = bytearray()
        self.buffFrame = []
        self.buffAccumulator = open('dump.bin', 'wb')

        #open the device in read only mode
        if isinstance(self.iodev, QtSerialPort.QSerialPort):
            #for serial type iodev
            # default serial port setting is 8bits, No Parity, 1 stop bits and No Flow Control
            # baud rate is 2MHz
            if self.iodev.open(QtCore.QIODevice.ReadOnly) == False:
                raise Exception(self.iodev.portName() + ' Device Not Found')

            self.iodev.setBaudRate(2000000)
            logger.warning('Opened {} @ {}'.format(self.iodev.portName(), self.iodev.baudRate()))
            self.iodev.readyRead.connect(self.processData)
        else:
            #for file type iodev
            logger.critical('Currently file mode unsupported')
            raise NotImplementedError

        # self.newFrame = QtCore.pyqtSignal(bytearray)

        # neoLED_FrameGrabber.callBackObj = self
    
    def __del__(self):
        # f = open('dump.bin', 'wb')
        # f.write(self.buffAccumulator)
        self.buffAccumulator.close()

    @QtCore.pyqtSlot()
    def processData(self):
        newBytesLen = self.iodev.bytesAvailable()

        thisBuffer = self.iodev.read(newBytesLen)
        self.buffOvrFlow += thisBuffer
        self.buffAccumulator.write(thisBuffer)

       	ovfBytesLen = len(self.buffOvrFlow)
        idxFooter = 0
        logger.warning('buff len {}, {}'.format(newBytesLen, ovfBytesLen))

        while (ovfBytesLen >= self.ledFrameBytes) and (idxFooter >= 0):

            idxFooter = self.buffOvrFlow.find(b'\x0d\x0a')
            logger.warning('Footer: {}'.format(idxFooter))

            if idxFooter > 0:
                #extract the buffer
                tmpExtractBuffer = self.buffOvrFlow[:idxFooter]

                #remove the the extracted buffer
                self.buffOvrFlow[:idxFooter+2] = []

                if idxFooter != self.ledFrameBytes:
                    # extracted buffer does not fit the frame, so discard them
                    logger.warning('discarding(B/S) data sz: {}'.format(idxFooter))
                else:
                    self.buffFrame = [self.colorSpaceConv(tmpExtractBuffer[i:i+self.ledColorChBytes]) for i in range(0, self.ledFrameBytes, self.ledColorChBytes)]
                    # logger.warning('match')
                    self.newFrame.emit(self.buffFrame)

            ovfBytesLen = len(self.buffOvrFlow)

    def getFrame(self):
        return self.buffFrame

tmpObj = None
gCntxt = None
tmeStamps = deque(maxlen=20)
tmePrev = None

@QtCore.pyqtSlot('QVector<int>')
def frameRefresh(frame):
    global gCntxt
    global tmeStamps
    global tmePrev

    tmeStamp = time.time()

    if tmePrev is not None and (tmeStamp - tmePrev) != 0:
        tmeStamps.append(1 / (tmeStamp - tmePrev))
    
    if len(tmeStamps) < tmeStamps.maxlen:
        gCntxt.setContextProperty("simRefreshRate",  "Calculating Hz...")
    else:
        RefreshRate = sum(tmeStamps)/tmeStamps.maxlen
        gCntxt.setContextProperty("simRefreshRate",  "{:0.4}Hz".format(RefreshRate))

    # print(len(frame), frame)
    frameColor = [QtGui.QColor.fromRgb(pixel) for pixel in frame]
    gCntxt.setContextProperty("simModelData",  frameColor)
    
    tmePrev = tmeStamp
    # pass

if __name__ == "__main__":
    argparser = argparse.ArgumentParser('Virtual neoLED Viewer', description='records or preview the neoLEDs with a defined layout')
    argparser.add_argument('--led', metavar='<WS2811 | WS2812B | SK6812RGBW>', type=str, required=True, help='LED type')
    argparser.add_argument('--ledsize', metavar='<int>', type=int, required=False, default=32, help='LED size in  pixels')
    argparser.add_argument('--layout', metavar='<SnakeL2R | SnakeT2B | ZigZagL2R | ZigZagT2B>', type=str, required=True, help='Pannel Layout type')
    argparser.add_argument('--width', metavar='<int>', type=int, required=True, help='Pannel Layout width')
    argparser.add_argument('--height', metavar='<int>', type=int, required=True, help='Pannel Layout height')
    # argparser.add_argument('--refresh', metavar='<LED Panel Refresh Rate in Hz>', type=int, required=True, help='Define refresh rate higher than actual panel refresh rate for smooth live view')
    argparser.add_argument('--port', metavar='<serial port>', type=str, required=False, help='live view HW serial port')
    argparser.add_argument('--file', metavar='<recorded file>', type=str, required=False, help='use the offline recorded')
    argparser.add_argument('--verbose', action = 'store_true', help='generate many logs')
    argparser.add_argument('--version', action='version', version='%(prog)s v0.1')

    args = argparser.parse_args()

    logger = logging.getLogger('neoLEDViewer')
    logger.setLevel(logging.CRITICAL if args.verbose == False else logging.WARNING)

    if args.led == 'WS2811':
        ledColorChBytes = 3
        led2RGB=lambda ledBuff: (0)<<24|ledBuff[0]<<16|ledBuff[1]<<8|ledBuff[2]
    elif args.led == 'WS2812B':
        ledColorChBytes = 3
        led2RGB=lambda ledBuff: (0)<<24|ledBuff[1]<<16|ledBuff[0]<<8|ledBuff[2]
    elif args.led == 'SK6812RGBW':
        ledColorChBytes = 4
        led2RGB=lambda ledBuff: (0)<<24|ledBuff[1]<<16|ledBuff[0]<<8|ledBuff[2]
    else:
        logger.critical('Invalid LED type, use --help to see the supported LED types')
        sys.exit(-1)

    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName(argparser.prog)
    view = QtQuick.QQuickView()

    if args.port:
        iodev = QtSerialPort.QSerialPort(args.port)
    elif args.file:
        iodev = QtCore.QFile(args.file)

    tmpObj = neoLED_FrameGrabber(iodev, args.width * args.height * ledColorChBytes, ledColorChBytes, led2RGB, args.verbose)
    # tmpObj = neoLED_FrameGrabber(QtCore.QFile(args.file), args.width * args.height * 4, args.verbose)
    logger.warning('Started...neoLEDViewer')

    gCntxt=view.rootContext()

    gCntxt.setContextProperty("simModelData",  [QtGui.QColor.fromRgb(0)]*(args.width * args.height))
    gCntxt.setContextProperty("simRefreshRate",  "0Hz")
    gCntxt.setContextProperty('pnlWidth', args.width)
    gCntxt.setContextProperty('pnlHeight',  args.height)
    gCntxt.setContextProperty('pnlLEDSize', args.ledsize)

    if args.layout == 'SnakeL2R':
        gCntxt.setContextProperty('pnlLayoutSrc',  'SnakeL2R.qml')
    elif args.layout == 'SnakeT2B':
        gCntxt.setContextProperty('pnlLayoutSrc',  'SnakeT2B.qml')
    elif args.layout == 'ZigZagL2R':
        gCntxt.setContextProperty('pnlLayoutSrc',  'ZigZagL2R.qml')
    elif args.layout == 'ZigZagT2B':
        gCntxt.setContextProperty('pnlLayoutSrc',  'ZigZagT2B.qml')
    else:
        logger.critical('Invalid layout style, use --help to see the supported layout')
        sys.exit(-1)

    view.setResizeMode(QtQuick.QQuickView.SizeRootObjectToView)

    view.setSource(QtCore.QUrl(pathlib.Path(os.path.abspath('PanelLayout.qml')).as_uri()))

    gRootObjs = view.rootObject()

    view.show()

    tmpObj.newFrame.connect(frameRefresh)

    sys.exit(app.exec_())

