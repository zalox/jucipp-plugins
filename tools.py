import jucipp, gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

favorite = os.environ['HOME'] + "/projects"
plugin = os.environ['HOME'] + "/.juci/plugins"
favorite_file = plugin + "tools.py" # change to favorite_file

def add_menu(position, label, items) :
  plugin_menu = jucipp.get_gio_plugin_menu()
  if not plugin_menu :
    jucipp.terminal.println('plugin_menu menu does not exist')
    return
  sub_menu = Gio.Menu.new()
  i = 0
  app = Gio.Application.get_default()
  for item in items :
    sub_menu.insert(i, item['label'], 'app.'+item['action'])
    i = i + 1
    python_action = Gio.SimpleAction.new(item['action'], None)
    python_action.connect('activate', item['method'])
    app.add_action(python_action)
    app.add_accelerator(item['accel'], 'app.'+item['action'], None)
    
  if plugin_menu.get_n_items() >= position :
    plugin_menu.remove(position)
    
  plugin_menu.insert_submenu(position, label, sub_menu)
  
def init() :
  items = [
            {
              'label': 'Open plugin folder',
              'action': 'open-plugin-folder',
              'accel': '<primary>p',
              'method': open_plugin_folder
            },
            {
              'label': 'Open favorite folder',
              'action': 'open-favorite-folder',
              'accel': '<primary>j',
              'method': open_favorite_folder
            },
            # TODO use unused keybindings
            {
              'label': 'Open favorite file',
              'action': 'open-favorite-file',
              'accel': '<primary><shift>j',
              'method': open_favorite_file
            }
  ]
  add_menu(0, '_Tools', items)
  
def open_favorite_folder(action, param) :
  jucipp.directories.open(favorite)
  
def open_favorite_file(action, param) :
  jucipp.directories.open(favorite_file)
 
def open_plugin_folder(action, param) :
  jucipp.directories.open(plugin)
  
init()
