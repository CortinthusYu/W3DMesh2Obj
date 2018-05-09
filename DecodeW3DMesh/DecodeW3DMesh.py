from xml.dom.minidom import parse
import xml.dom.minidom
import os,sys
items = os.listdir(".")
FileList = []
for names in items:
  if names.endswith(".w3x"):
    FileList.append(names)
print(FileList)


for names in FileList:
    DOMTree=parse(sys.path[0]+'\\'+names)
    root=DOMTree.documentElement
    vertexs=root.getElementsByTagName('Vertices')[0].getElementsByTagName('V')
    Normals=root.getElementsByTagName('Normals')[0].getElementsByTagName('N')
    Faces=root.getElementsByTagName('Triangles')[0].getElementsByTagName('T')
    try:
        TexCoords1=root.getElementsByTagName('TexCoords')[0].getElementsByTagName('T')
        #TexCoords2=root.getElementsByTagName('TexCoords')[1].getElementsByTagName('T')
    finally:
        print('Going Wrong')

    file=open("{0}\{1}".format(sys.path[0],names+'.obj'),'w+')
    print('opening'+"{0}\{1}".format(sys.path[0],names+'.obj'))
    for v in vertexs:
       if v._attrs!=None:
        file.write('v {0} {1} {2}\n'.format(v.getAttribute('X'),v.getAttribute('Y'),v.getAttribute('Z')))

    for n in Normals:
        if v._attrs!=None:
         file.write('vn {0} {1} {2}\n'.format(n.getAttribute('X'),n.getAttribute('Y'),n.getAttribute('Z')))

    for tc in TexCoords1:
     if v._attrs!=None:
      file.write('vt {0} {1} {2}\n'.format(tc.getAttribute('X'),tc.getAttribute('Y'),tc.getAttribute('Z')))

#   for tc in TexCoords2:
#     if v._attrs!=None:
#         file.write('vt {0} {1} {2}\n'.format(v.getAttribute('X'),v.getAttribute('Y'),v.getAttribute('Z')))

    for f in Faces:
     file.write('f {0}/{0}/{0} {1}/{0}/{1} {2}/{0}/{2}\n'.format(
                                   int(f.childNodes[1].childNodes[0].data)+1,
                                   int(f.childNodes[3].childNodes[0].data)+1,
                                  int(f.childNodes[5].childNodes[0].data)+1,
                                  f.childNodes[7].getAttribute('X'),
                                  f.childNodes[7].getAttribute('Y'),
                                  f.childNodes[7].getAttribute('Z')))
    file.close()
