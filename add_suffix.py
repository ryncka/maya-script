import maya.cmds as rt

def process():
  selected = rt.ls(selection=True)
  if not selected:
    rt.warning("no objects selected")
    return

  dialog_selected = rt.promptDialog(
    title='add suffix',
    message='enter the suffix to be added',
    button=['ok', 'cancel'],
    defaultButton='ok',
    cancelButton='cancel',
    dismissString='cancel'
  )

  if dialog_selected == 'ok':
    suffix = rt.promptDialog(query=True, text=True)
    for object in selected:
      name = object + suffix
      rt.rename(object, name)
  else:
    rt.warning("operation canceled")

process()