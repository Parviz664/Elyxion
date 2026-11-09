from pathlib import Path
import hashlib
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
manifest = ET.parse(root / 'app/src/main/AndroidManifest.xml')
android = '{http://schemas.android.com/apk/res/android}'
permissions = {p.attrib.get(android + 'name') for p in manifest.getroot().findall('uses-permission')}
for name in ('android.permission.INTERNET', 'android.permission.SYSTEM_ALERT_WINDOW', 'android.permission.FOREGROUND_SERVICE_SPECIAL_USE'):
    assert name in permissions, name
java = root / 'app/src/main/java/com/elyxion/cosmos'
files = list(java.glob('*.java'))
assert len(files) == 11
assert 'InputBus.move(x, y)' in (java / 'OverlayService.java').read_text()
assert 'InputBus.x()' in (java / 'DemoActivity.java').read_text()
assert 'web.loadUrl(URL)' in (java / 'StarveActivity.java').read_text()
assert 'web.dispatchKeyEvent(event)' in (java / 'StarveActivity.java').read_text()
assert 'AimMath.target(' in (java / 'StarveActivity.java').read_text()
assert 'setMotionEventSplittingEnabled(true)' in (java / 'StarveActivity.java').read_text()
assert (java / 'AimMath.java').is_file()
assert (root / 'qa/AimMathTest.java').is_file()
assert 'dispatchGesture' not in ''.join(p.read_text() for p in files)
assert (root / 'app/build.gradle').is_file()
assert (root / 'settings.gradle').is_file()
sums = root / 'SHA256SUMS.txt'
for ln in sums.read_text().splitlines():
    sha, rel = ln.split('  ', 1)
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == sha, rel
print('PASS: 11 Java sources, Android manifest, no third-party gesture injection,  SHA256 source manifest')
