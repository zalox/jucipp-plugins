import jucipp
from jucipp import Menu, Config

menu = Menu.get()
config = Config.get()

keybindings = config.menu.keys

def print_hello():
    print("hello, world")

keybindings["hello-action"] = "<primary>h"
config.menu.keys = keybindings

menu.add_action("hello-action", print_hello)
menu.set_keys()

# import jucipp, os, gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk, Gio
# from os import path

# def add_menu(position, label, items) :
#     plugin_menu = jucipp.get_gio_plugin_menu()
#     sub_menu = Gio.Menu.new()
#     i = 0
#     app = Gio.Application.get_default()
#     for item in items :
#       sub_menu.insert(i, item['label'], 'app.'+item['action'])
#       i = i + 1
#       python_action = Gio.SimpleAction.new(item['action'], None)
#       python_action.connect('activate', item['method'])
#       app.add_action(python_action)
#       app.add_accelerator(item['accel'], 'app.'+item['action'], None)
#     if plugin_menu.get_n_items() >= position :
#       plugin_menu.remove(position)
#     plugin_menu.insert_submenu(position, label, sub_menu)

# def init() :
#   items = [
#             {
#               'label': 'Insert snippet',
#               'action': 'insert-snippet',
#               'accel': '<Alt>space',
#               'method': insert_snippet
#             }
#   ]
#   add_menu(1, '_Snippet', items)False

# def get_ifndef() :
#   file_name = str(jucipp.editor.get_file_path())
#   package, file_name = path.split(file_name)
#   file_name, file_ext = path.splitext(file_name)
#   package = path.basename(package)
#   guard = package + '_' + file_name + '_' + file_ext[1:len(file_ext)] + '_\n'
#   res = '#ifndef ' + guard
#   res += '#define ' + guard
#   res += '#endif  // ' + guard
#   return res

# def get_snippet(word) :
#   snippets = {}

#   # iterate array
#   snippets['itar'] = '''\
# for (int i = 0; i < ${v.size()}; i++) {

# }'''
#   # iterate list
#   snippets['itli'] = '''\
# for (auto &${item:list_type}) {

# }'''

#   snippets['if'] = '''\
# if (${}) {

# }'''

#   snippets['ife'] = '''\
# if (${}) {

# } else {

# }'''

#   snippets['cout'] = '''\
# cout << ${} << "\\n";'''
#   snippets['io'] = '''\
# #include <iostream>
# using namespace std;'''
#   snippets['ifndef'] = get_ifndef()
#   try :
#     output = snippets[word]
#   except KeyError :
#     output = word
#   return output

# def get_iter_at_cursor(gtk_text_buffer) :
#   mark = gtk_text_buffer.get_insert()
#   return gtk_text_buffer.get_iter_at_mark(mark)

# def get_current_line_text(gtk_text_buffer) :
#   line_number = get_iter_at_cursor(gtk_text_buffer).get_line()
#   start_iter = gtk_text_buffer.get_iter_at_line(line_number)
#   end_iter = gtk_text_buffer.get_iter_at_line(line_number+1)
#   end_iter.backward_char()
#   return gtk_text_buffer.get_text(start_iter, end_iter, 0)

# def add_indention(text_line, output) :
#   tab_info = [" ", ""];
#   indent = 0
#   for c in text_line :
#     if c is not tab_info[0]:
#       break
#     indent = indent + 1
#   if indent <= 0 :
#    return output
#   text_indent = ''
#   for x in range(0, indent) :
#     text_indent = text_indent + tab_info[0]
#   text_lines = output.split('\n')
#   res = ''
#   for text_line in text_lines :
#     res += text_indent + text_line + '\n'
#   return res[indent:len(res)]

# # jumps the marker to ${content} and marks the content
# def jump(start_iter, text) :
#   buf = start_iter.get_buffer()
#   start_pos = start_iter.get_offset()
#   end_pos = start_iter.get_offset()
#   pos = 0
#   stack = []
#   for c in text : # takes care of matching {}
#     if c is '$' : # constraint: comments with $ are not allowed in snippets
#       start_pos = start_pos + pos
#     if c is '{' :
#       stack.append(c)
#     if c is '}':
#       if stack.count(stack) is 0 :
#         end_pos = end_pos + pos
#         break
#       stack.pop()
#     pos = pos + 1
#   if pos is len(text) :
#     return
#   begin = buf.get_iter_at_offset(start_pos);
#   end = buf.get_iter_at_offset(end_pos+1);
#   token = buf.get_text(buf.get_iter_at_offset(start_pos+2),buf.get_iter_at_offset(end_pos),True)
#   buf.delete(begin,end)
#   buf.insert(begin,token,len(token))
#   buf.place_cursor(begin)
#   buf.move_mark(buf.get_insert(),buf.get_iter_at_offset(start_pos))

# def insert_snippet(action, param) :
#   view = jucipp.editor.get_current_gtk_source_view()
#   if not view :
#     return
#   gtk_text_buffer = view.get_buffer()
#   if not gtk_text_buffer :
#     return
#   input_line = get_current_line_text(gtk_text_buffer)
#   if not input_line or input_line is '' :
#     return
#   line_offset = get_iter_at_cursor(gtk_text_buffer).get_line_index()
#   first_backwards_space = input_line.rfind(' ', 0, line_offset)
#   first_backwards_space = first_backwards_space + 1
#   snippet_key_word = input_line[first_backwards_space:line_offset]
#   snippet = get_snippet(snippet_key_word)
#   if snippet == snippet_key_word :
#     return
#   snippet = add_indention(input_line, snippet)
#   line_number = get_iter_at_cursor(gtk_text_buffer).get_line()
#   begin_iter = gtk_text_buffer.get_iter_at_line_offset(line_number,first_backwards_space)
#   end_iter = gtk_text_buffer.get_iter_at_line_offset(line_number,line_offset)
#   gtk_text_buffer.delete(begin_iter,end_iter)
#   gtk_text_buffer.insert_at_cursor(snippet, len(snippet)-1)
#   end_iter = get_iter_at_cursor(gtk_text_buffer)
#   end_iter.backward_chars(len(snippet)-1)
#   jump(end_iter, snippet)


# init()

