import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
//import cyhub 1.0

Item {
    id: win_root
    width: 1920
    height: 1080

    Item {
        id: windowsId
        anchors.fill: parent

        MenuBar {
            id :myTopMenu
            width: parent.width
            height: 30

            Menu {
                id: filemenu
                title: qsTr("&File")
                MenuItem {
                    text: "Settings"
                    onTriggered: {
                        settings_dialog.open()
                        settings_dialog.set_settings_info()
                    }
                }
            }

            Menu {
                id: editMenu
                title: qsTr("&Edit")
                // ...
            }

            Menu {
                id: viewMenu
                title: qsTr("&View")
                // ...
            }

            Menu {
                id: helpMenu
                title: qsTr("&Help")
                // ...
            }
            
        }
    
        Rectangle {
            id : winareaId
            width: parent.width
            height: 1020
            anchors {
                top: myTopMenu.bottom
            }
            color: "#95C8D8"

            RowLayout {
                id: rowLayoutId 
                anchors.fill: parent

                ColumnLayout{
                    id: colLayoutId

                    signal clickedButton(string name)

                    Frame {



                    }

                    Frame {
                        GridLayout {

                        }
                    }

                    Frame {
                        GridLayout {

                        }
                    }

                    Frame{
                        RowLayout {

                        }
                    }
                }

                //I2G_IMG_HOLDER {}

            }

        }

        Item {
            id: statusbar_Id
            Rectangle {
                width: parent.width
                height: 30
                anchors {
                    bottom: parent.bottom
                }
                //color: "#95C8D8"
                color: "#313231"
                
            }
            
        }
    }
}