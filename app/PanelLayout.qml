import QtQuick 2.12
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.12

Item {
    id: itmRoot

    width: rectOuter.width + rectOuter.x + 8
    height: rectOuter.height + rectOuter.y + 8

    // create an object instance of model view Component
    SimulatorLed {
        id: simLED
        sizeLED: pnlLEDSize + 1
    }

    Rectangle {
        id: rectOuter
        x: 8
        y: 8
        width: colLayout.width
        height: colLayout.height
        color: "gray"

        ColumnLayout {
            id: colLayout
            anchors.left: parent.left
            anchors.top: parent.top

            Loader {
                id: loaderLayout
                property SimulatorLed simLED: simLED
                source: pnlLayoutSrc
            }

            // Rectangle {width: pnlWidth * simLED.sizeLED; height: pnlHeight * simLED.sizeLED}

            Text {
                id: txtRefresh
                text: simRefreshRate
                font.pointSize: Math.min(24, (12/4) * pnlLEDSize)
                font.bold: true
                color: "orange"
            }
        }
    }
}
