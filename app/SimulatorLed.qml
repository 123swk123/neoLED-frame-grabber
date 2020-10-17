import QtQuick 2.12

Item {
    property Component compLED: _compLED
    property var sizeLED

    Component {
        id:_compLED
        Item {
            Rectangle {
                id: _compRect
                // removing border improves render speed, due to less number of render features
                // border.width:sizeLED/24
                // width:sizeLED-border.width; height:sizeLED-border.width; radius: (sizeLED-border.width)/5;
                // border.color:"gray"//"#dc982c"
                width:sizeLED; height:sizeLED; radius: sizeLED/6;
                color: modelData//Qt.lighter(modelData, 1.5)

                Loader {
                    id: loaderText
                }
                Component.onCompleted: {
                    if(sizeLED > 24+border.width)
                        loaderText.sourceComponent = _compText
                }

                Component {
                    id: _compText
                    Text {
                        text: (index+1)
                        parent: _compRect
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.verticalCenter: parent.verticalCenter
                        font.pointSize: 7.5
                        color: '#303030'
                    }
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
