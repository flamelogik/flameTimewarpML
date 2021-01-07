#!/usr/bin/python
'''
Andriy's bunlde packer
'''

import os
import sys
import base64

pligin_dirname = os.path.dirname(os.path.abspath(__file__))
plugin_file_name = os.path.basename(pligin_dirname) + '.py'
python_source = os.path.join(pligin_dirname, plugin_file_name)
bundle_folder = os.path.basename(pligin_dirname) + '.bundle'
bundle_code = 'flameTimewarpML.py'

if not os.path.isdir(bundle_folder):
    print('no folder named %s' % bundle_folder)
    sys.exit()

if '--full' in sys.argv:
    
    print ('creating %s' % bundle_folder + '.tar.bz2\n---')
    cmd = 'tar cvf ' + bundle_folder + '.tar ' + bundle_folder
    os.system(cmd)
    cmd = 'pbzip2 -v ' + bundle_folder + '.tar'
    os.system(cmd)
    cmd = 'mv ' + bundle_folder + '.tar.bz2 flameTimewarpML.package/flameTimewarpMLenv.bundle'
    os.system(cmd)

'''
f = open(bundle_folder + '.tar.bz2', 'rb')
bunle_data = f.read()
f.close()
'''

f = open('/usr/bin/pbzip2', 'rb')
bunle_data = f.read()
f.close()

encoded_bundle_data = base64.b64encode(bunle_data)

f = open(bundle_code, 'r')
bundle_code = f.read()
f.close()

bundled_code =bundle_code.replace('REPLACEME', encoded_bundle_data)

with open('flameTimewarpML.package/flameTimewarpML.py', 'w') as tempfile:
    with open(python_source, 'r') as src:
        tempfile.write(src.read())
        tempfile.write(bundled_code)


# cmd = 'mv tmp.py /opt/Autodesk/shared/python/' + plugin_file_name
# os.system(cmd)

# print ('---\nremoving %s' % bundle_folder + '.tar.bz2')
# os.remove(bundle_folder + '.tar.bz2')