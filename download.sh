#!/bin/sh
set -eu
fetch="curl --location --fail --silent --show-error -o"
master="https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master"
set -x
$fetch gl.xml  "$master/xml/gl.xml"
$fetch glx.xml "$master/xml/glx.xml"
$fetch wgl.xml "$master/xml/wgl.xml"
