#ifndef __GUI_MENU_BUILDER_H__
#define __GUI_MENU_BUILDER_H__

#include <wx/wx.h>

class MenuBuilder {
 public:
  virtual void SetupMenus(wxMenuBar *menu_bar) = 0;
};

#endif