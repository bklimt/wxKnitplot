
#ifndef __MODEL_RENDERER_H__
#define __MODEL_RENDERER_H__

namespace chart_model {

class Circle;
class Line;
class Polygon;
class Rectangle;
class Spline;
class Style;
class Text;

class Renderer {
 public:
  virtual ~Renderer() {}

  virtual void Start(int width, int height) = 0;
  virtual void DrawLine(const Line &line, const Style &style) = 0;
  virtual void DrawRectangle(const Rectangle &rect, const Style &style) = 0;
  virtual void DrawCircle(const Circle &circle, const Style &style) = 0;
  virtual void DrawPolygon(const Polygon &polygon, const Style &style) = 0;
  virtual void DrawSpline(const Spline &spline, const Style &style) = 0;
  virtual void DrawText(const Text &text, const Style &style) = 0;
  virtual void End() = 0;
};

}  // namespace chart_model

#endif

