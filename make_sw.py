# Writes sw.js with a content-hash version so every deploy refreshes the offline copy.
import hashlib, os, json
root = os.path.dirname(os.path.abspath(__file__))
files = ['./', 'index.html', 'info.js', 'corpara.webmanifest'] + ['icons/' + f for f in sorted(os.listdir(root + '/icons')) if f.endswith('.png')] + ['data/' + f for f in sorted(os.listdir(root + '/data')) if f.endswith(('.txt', '.json'))]
h = hashlib.md5()
for f in files[1:]: h.update(open(os.path.join(root, f), 'rb').read())
V = 'corpara-' + h.hexdigest()[:10]
cdn = ['https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js', 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js', 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/environments/RoomEnvironment.js', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap']
sw = open(root + '/sw.template.js').read().replace('__VERSION__', V).replace('__FILES__', json.dumps(files)).replace('__CDN__', json.dumps(cdn))
open(root + '/sw.js', 'w').write(sw); print(V, len(files), 'files')
