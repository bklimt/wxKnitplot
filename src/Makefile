all: ../bin/cli/proto2json ../bin/cli/chart2svg ../bin/gui/knitplot

../obj/storage/chart.pb: storage/chart.proto
	protoc -I=. --cpp_out=. $< && mkdir -p ../obj/storage && touch $@

storage/chart.pb.h: ../obj/storage/chart.pb

storage/chart.pb.cc: ../obj/storage/chart.pb

../obj/model/library.o: model/library.cc model/library.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/gui/chart_panel.o: gui/chart_panel.cc gui/preview_panel.h model/chart.h model/color.h model/listener.h model/chart_parser.h model/chart_listener.h gui/library_panel.h model/point.h model/style.h gui/menu_builder.h model/shape.h model/shape_base.h model/library.h gui/chart_panel.h storage/chart.pb.h model/graphic.h
	mkdir -p ../obj/gui && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/point.o: model/point.cc model/point.h model/listener.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/line.o: model/line.cc model/color.h model/listener.h model/point.h model/line.h model/style.h model/renderer.h model/shape_base.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/chart_parser.o: model/chart_parser.cc model/chart_parser.h model/library.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/cli/proto2json.o: cli/proto2json.cc storage/chart.pb.h
	mkdir -p ../obj/cli && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../bin/cli/proto2json: ../obj/cli/proto2json.o ../obj/storage/chart.pb.o
	mkdir -p ../bin/cli && c++ -o $@ $^ -lgflags -lprotobuf

../obj/model/text.o: model/text.cc model/text.h model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/shape_base.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/circle.o: model/circle.cc model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/circle.h model/shape_base.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/cli/chart2svg.o: cli/chart2svg.cc model/svg.h model/chart.h model/color.h model/listener.h model/chart_parser.h model/chart_listener.h model/point.h model/style.h model/renderer.h model/shape.h model/shape_base.h model/library.h storage/chart.pb.h model/graphic.h
	mkdir -p ../obj/cli && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../bin/cli/chart2svg: ../obj/cli/chart2svg.o ../obj/model/polygon.o ../obj/model/chart.o ../obj/model/svg.o ../obj/model/chart_parser.o ../obj/model/circle.o ../obj/storage/chart.pb.o ../obj/model/shape.o ../obj/model/style.o ../obj/model/color.o ../obj/model/text.o ../obj/model/spline.o ../obj/model/rectangle.o ../obj/model/library.o ../obj/model/graphic.o ../obj/model/line.o ../obj/model/point.o
	mkdir -p ../bin/cli && c++ -o $@ $^ -lgflags -lprotobuf

../obj/model/graphic.o: model/graphic.cc model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/shape.h model/shape_base.h model/graphic.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/shape.o: model/shape.cc model/text.h model/color.h model/listener.h model/point.h model/style.h model/line.h model/shape.h model/spline.h model/shape_base.h model/circle.h model/polygon.h storage/chart.pb.h model/rectangle.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/color.o: model/color.cc model/color.h model/listener.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/anchor.o: model/anchor.cc model/point.h model/anchor.h model/listener.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/gui/preview_panel.o: gui/preview_panel.cc gui/preview_panel.h model/chart.h model/color.h model/listener.h model/chart_parser.h model/chart_listener.h model/point.h model/style.h model/renderer.h model/shape.h gui/wx_renderer.h model/shape_base.h model/library.h storage/chart.pb.h model/graphic.h
	mkdir -p ../obj/gui && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/gui/library_panel.o: gui/library_panel.cc gui/preview_panel.h model/chart.h model/color.h model/listener.h model/chart_parser.h model/chart_listener.h gui/library_panel.h model/point.h model/style.h model/renderer.h model/shape.h gui/wx_renderer.h model/shape_base.h model/library.h storage/chart.pb.h model/graphic.h
	mkdir -p ../obj/gui && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/polygon.o: model/polygon.cc model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/shape_base.h model/polygon.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/svg.o: model/svg.cc model/svg.h model/text.h model/color.h model/listener.h model/point.h model/style.h model/line.h model/renderer.h model/spline.h model/circle.h model/shape_base.h model/polygon.h storage/chart.pb.h model/rectangle.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/chart.o: model/chart.cc model/svg.h model/chart.h model/color.h model/listener.h model/chart_parser.h model/chart_listener.h model/point.h model/style.h model/renderer.h model/shape.h model/shape_base.h model/library.h storage/chart.pb.h model/graphic.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/gui/knitplot.o: gui/knitplot.cc gui/preview_panel.h model/chart.h gui/knitplot.h model/listener.h model/chart_parser.h model/chart_listener.h model/color.h gui/library_panel.h model/point.h model/style.h gui/menu_builder.h model/shape.h model/shape_base.h model/library.h storage/chart.pb.h gui/chart_panel.h model/graphic.h
	mkdir -p ../obj/gui && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../bin/gui/knitplot: ../obj/gui/knitplot.o ../obj/model/point.o ../obj/gui/library_panel.o ../obj/model/chart.o ../obj/model/chart_parser.o ../obj/model/svg.o ../obj/model/circle.o ../obj/storage/chart.pb.o ../obj/gui/preview_panel.o ../obj/model/shape.o ../obj/model/style.o ../obj/gui/wx_renderer.o ../obj/model/color.o ../obj/model/text.o ../obj/model/spline.o ../obj/model/rectangle.o ../obj/model/library.o ../obj/model/graphic.o ../obj/gui/chart_panel.o ../obj/model/line.o ../obj/model/polygon.o
	mkdir -p ../bin/gui && c++ -o $@ $^ -lgflags `wx-config --libs` -lprotobuf

../obj/model/style.o: model/style.cc model/color.h model/style.h model/listener.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/gui/wx_renderer.o: gui/wx_renderer.cc model/text.h model/color.h model/listener.h model/point.h model/style.h model/line.h model/renderer.h model/spline.h gui/wx_renderer.h model/circle.h model/shape_base.h model/polygon.h storage/chart.pb.h model/rectangle.h
	mkdir -p ../obj/gui && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/rectangle.o: model/rectangle.cc model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/shape_base.h storage/chart.pb.h model/rectangle.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/model/spline.o: model/spline.cc model/color.h model/listener.h model/point.h model/style.h model/renderer.h model/spline.h model/shape_base.h storage/chart.pb.h
	mkdir -p ../obj/model && c++ -I. -c -o $@ $< `wx-config --cxxflags`

../obj/storage/chart.pb.o: storage/chart.pb.cc storage/chart.pb.h
	mkdir -p ../obj/storage && c++ -I. -c -o $@ $< `wx-config --cxxflags`

