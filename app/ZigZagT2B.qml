import QtQuick 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12

GridView {
    id: viewLayout

    width: pnlWidth * simLED.sizeLED
    height: pnlHeight * simLED.sizeLED
    
    cellWidth: simLED.sizeLED
    cellHeight: simLED.sizeLED

    flow: GridView.FlowTopToBottom
    verticalLayoutDirection: GridView.TopToBottom
    layoutDirection: Qt.LeftToRight

    model: simModelData
    delegate: simLED.compLED
}