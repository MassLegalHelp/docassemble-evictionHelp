from docassemble.base.functions import value

def adjust(item, length=None):
  try:
    val = value(item)
    return str(val).ljust(length or 20)
  except:
    return " " * (length or 20)

def adjustMoney(item, length=None):
  return adjust(item, length or 10)

def exists(item):
  try:
    val = value(item)
    return len(str(val).strip()) > 0
  except:
    return False