import docassemble.base.util

def adjust(item, length=None):
  if item != None:
    return str(item or "").ljust(length or 20)
  return " " * length 

def adjustMoney(item, length=None):
  return adjust(item, length or 10)