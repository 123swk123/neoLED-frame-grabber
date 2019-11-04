import QtQuick 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12

PathView {
    id: viewLayout

    width: pnlWidth * simLED.sizeLED
    height: pnlHeight * simLED.sizeLED

    model: simModelData
    delegate: simLED.compLED

    Component.onCompleted: {
        var strTemp = ''
        var x = simLED.sizeLED * (pnlHeight-1)
        for(var y=0;y<pnlWidth;y++) {
            strTemp += 'PathLine{y:'+x+'; x:(simLED.sizeLED * '+ y +')} PathLine{y:'+x+'; x:(simLED.sizeLED * '+ (y+1) +')} '
            x = (x === 0) ? simLED.sizeLED * (pnlHeight-1) : 0
        }

        var obj = Qt.createQmlObject('import QtQuick 2.12;Path { startX:0; startY:0;'+strTemp+'}', viewLayout)
        viewLayout.path = obj;
    }
}