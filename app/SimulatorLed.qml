import QtQuick 2.12

Item {
    property Component compLED: _compLED
    property var sizeLED

    Component {
        id:_compLED
        Item {
            Rectangle {
                border.width:1
                width:sizeLED-border.width; height:sizeLED-border.width; radius: (sizeLED-border.width)/5;
                border.color:"#dc982c"
                color: Qt.lighter(modelData, 1.5)

                Text {
                    text: (index+1)
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    font.pointSize: 7.5
                    color: 'white'
                }
            }
        }
    }
}



/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
