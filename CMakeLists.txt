cmake_minimum_required(VERSION 3.0.0)
project(wxKnitplot VERSION 0.1.0)

find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
link_libraries(${Protobuf_LIBRARIES})

find_package(wxWidgets REQUIRED)
include_directories(${wxWidgets_INCLUDE_DIRS})
link_libraries(${wxWidgets_LIBRARIES})
include(${wxWidgets_USE_FILE})

find_package(gflags REQUIRED)
include_directories(${gflags_INCLUDE_DIRS})
link_libraries(${gflags_LIBRARIES})

PROTOBUF_GENERATE_CPP(PROTO_SRC PROTO_HEADER src/storage/chart.proto)

include_directories(src)
set(SOURCES
    ${PROTO_SRC}
    ${PROTO_HEADER}
    src/gui/library_panel.h
    src/gui/chart_panel.h
    src/gui/preview_panel.h
    src/gui/library_panel.cc
    src/gui/knitplot.h
    src/gui/wx_renderer.h
    src/gui/chart_panel.cc
    src/gui/wx_renderer.cc
    src/gui/preview_panel.cc
    src/gui/menu_builder.h
    src/model/library.h
    src/model/spline.cc
    src/model/style.h
    src/model/spline.h
    src/model/chart_parser.cc
    src/model/chart_parser.h
    src/model/line.h
    src/model/color.cc
    src/model/chart.cc
    src/model/polygon.cc
    src/model/shape_base.h
    src/model/graphic.h
    src/model/point.cc
    src/model/listener.h
    src/model/line.cc
    src/model/shape.h
    src/model/chart.h
    src/model/rectangle.cc
    src/model/svg.h
    src/model/circle.cc
    src/model/library.cc
    src/model/style.cc
    src/model/point.h
    src/model/graphic.cc
    src/model/text.cc
    src/model/color.h
    src/model/renderer.h
    src/model/circle.h
    src/model/polygon.h
    src/model/rectangle.h
    src/model/shape.cc
    src/model/svg.cc
    src/model/chart_listener.h
    src/model/text.h
)

add_executable(knitplot src/gui/knitplot.cc ${SOURCES})
add_executable(proto2json src/cli/proto2json.cc ${SOURCES})
add_executable(chart2svg src/cli/chart2svg.cc ${SOURCES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
