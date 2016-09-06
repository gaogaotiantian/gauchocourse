#!/bin/sh
if [ -d "$1" ]; then
    cp ./apdata.json ./apSourceCodes.js ./courseData.json ./gc.js ./gradreq.json Style.css ./typege.js ui.js "$1"
    cp -r ./image "$1"
    cp ./index_pre.html "$1"/index.html
else
    echo "Directory does not exist"
fi

