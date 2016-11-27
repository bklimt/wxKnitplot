#!/usr/bin/python3

import os
import os.path
import pprint
import subprocess
import sys

fullpath_map = {}
module_map = {}
protos = []

# Figure out where the relevant libs are.
#wx_copts = subprocess.check_output('wx-config --cxxflags'.split()).split()
#wx_libs = subprocess.check_output('wx-config --libs'.split()).split()

def read_includes(fullpath):
  f = open(fullpath)
  lines = f.read().split('\n')
  f.close()
  includes = [line for line in lines if line.startswith('#include "')]
  includes = [include[len('#include "'):-1] for include in includes]
  return includes

def has_main(fullpath):
  f = open(fullpath)
  lines = f.read().split('\n')
  f.close()
  mains = [line for line in lines if line.startswith('int main(')]
  if len(mains):
    return True
  return False

def has_wx_app(fullpath):
  f = open(fullpath)
  lines = f.read().split('\n')
  f.close()
  mains = [line for line in lines if line.startswith('IMPLEMENT_APP(')]
  if len(mains):
    return True
  return False

def find_library_for_header(fullpath):
  base = os.path.splitext(fullpath)[0]
  library = base + '.cc'
  if os.path.exists(library):
    return library
  return None

class Source:
  def __init__(self, path, name, ext, fullpath):
    self.path = path
    self.name = name
    self.ext = ext
    self.fullpath = fullpath
    self.module_name = os.path.join(path, name + ext)
  def __repr__(self):
    return str(self)
  def __str__(self):
    return self.fullpath

class Node:
  def __init__(self, source):
    self.source = source
    self.includes = read_includes(source.fullpath)
  def is_proto(self):
    return self.source.name.endswith('.pb')
  def pb_name(self):
    return os.path.join('../obj', self.source.path, self.source.name)
  def __str__(self):
    return self.__repr__()

class Header(Node):
  def __init__(self, source):
    Node.__init__(self, source)
    self.library = find_library_for_header(source.fullpath)
  def __repr__(self):
    return 'Header(%s, %s, %s)' % (self.source, self.library, self.includes)

class Library(Node):
  def __init__(self, source):
    Node.__init__(self, source)
    self.has_main = has_main(source.fullpath)
    self.has_wx_app = has_wx_app(source.fullpath)
  def bin_name(self):
    return os.path.join('../bin', self.source.path, self.source.name)
  def lib_name(self):
    return os.path.join('../obj', self.source.path, self.source.name + '.o')
  def __repr__(self):
    return 'Library(%s, %s)' % (self.source, self.includes) 

def get_transitive_includes(node, seen, results, indent=0):
  if node.source.fullpath in seen:
    raise Exception("cycle in includes: %s in %s" % (node.source.fullpath, seen))
  seen.append(node.source.fullpath)
  for include in node.includes:
    child = module_map[include]
    results.add(child)
    get_transitive_includes(child, seen, results, indent + 1)
  seen.pop()

def get_included_deps(node):
  deps = set()
  for include in node.transitive_includes:
    dep = include.library
    if dep:
      deps.add(fullpath_map[dep])
  if node in deps:
    deps.remove(node)
  return list(deps)

def get_transitive_deps(node, seen, results):
  if node.source.fullpath in seen:
    return
  seen.append(node.source.fullpath)
  for dep in node.deps:
    results.add(dep)
    get_transitive_deps(dep, seen, results)
  seen.pop()

def main(args):
  root = './'

  # Process all the directories.
  for dirpath, dirnames, filenames in os.walk(root):
    module = dirpath[len(root):]
    if len(module) and module[0] == '/':
      module = module[1:]
    for filename in filenames:
      name, ext = os.path.splitext(filename)
      source = Source(module, name, ext, os.path.join(dirpath, filename))
      if source.ext == '.cc':
        lib = Library(source)
        fullpath_map[source.fullpath] = lib
        module_map[os.path.join(module, filename)] = lib
      elif source.ext == '.h':
        hdr = Header(source)
        fullpath_map[source.fullpath] = hdr
        module_map[os.path.join(module, filename)] = hdr
      elif source.ext == '.proto':
        protos.append(source)

  # Populate the deps and transitive includes.
  for name in module_map:
    node = module_map[name]
    includes = set()
    get_transitive_includes(node, [], includes)
    node.transitive_includes = list(includes)
    if node.source.ext == '.cc':
      node.deps = get_included_deps(node)

  # Populate the transitive deps.
  for name in module_map:
    node = module_map[name]
    if node.source.ext != '.cc':
      continue
    deps = set()
    get_transitive_deps(node, [], deps)
    if node in deps:
      deps.remove(node)
    node.transitive_deps = list(deps)

  # Print the all rule.
  binaries = [
    module_map[name].bin_name()
    for name in module_map
    if module_map[name].source.ext == '.cc' and (
      module_map[name].has_main or module_map[name].has_wx_app)
  ]
  print('all: ' + ' '.join(binaries))
  print('')

  # Print rules for all protos.
  for proto in protos:
    print("""%s: %s
\tprotoc -I=. --cpp_out=. $< && mkdir -p %s && touch $@
""" % (
      os.path.join('../obj/', proto.path, proto.name + '.pb'),
      proto.module_name,
      os.path.join('../obj', proto.path)
))

  # Print any .pb rules.
  for name in module_map:
    node = module_map[name]
    if not node.is_proto():
      continue
    print("""%s: %s
""" % (
        node.source.module_name,
        node.pb_name(),
      ))

  # Print the .o rules.
  for name in module_map:
    node = module_map[name]
    if node.source.ext != '.cc':
      continue
    print("""%s: %s %s
\tmkdir -p %s && c++ -I. -c -o $@ $< `wx-config --cxxflags`
""" % (
        node.lib_name(),
        node.source.module_name,
        ' '.join([inc.source.module_name for inc in node.transitive_includes]),
        os.path.dirname(node.lib_name()),
      ))
    # Print the binary rule, if appropriate.
    if node.has_main:
      proto_libs = ''
      if len([dep for dep in node.transitive_deps if dep.source.name.endswith('.pb')]):
        proto_libs = ' -lprotobuf'
      print("""%s: %s %s
\tmkdir -p %s && c++ -o $@ $^ -lgflags%s
""" % (
          node.bin_name(),
          node.lib_name(),
          ' '.join([dep.lib_name() for dep in node.transitive_deps]),
          os.path.dirname(node.bin_name()),
          proto_libs
        ))
    # Print the wx binary rule, if appropriate.
    if node.has_wx_app:
      proto_libs = ''
      if len([dep for dep in node.transitive_deps if dep.source.name.endswith('.pb')]):
        proto_libs = ' -lprotobuf'
      print("""%s: %s %s
\tmkdir -p %s && c++ -o $@ $^ -lgflags `wx-config --libs`%s
""" % (
          node.bin_name(),
          node.lib_name(),
          ' '.join([dep.lib_name() for dep in node.transitive_deps]),
          os.path.dirname(node.bin_name()),
          proto_libs
        ))
      

  # Print the results.
  for name in module_map:
    node = module_map[name]
    #print(name)
    #if node.source.ext == '.cc':
    #  print(node.deps)
    #print('')

if __name__ == '__main__':
  main(sys.argv)
