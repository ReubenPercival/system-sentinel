pkgname=system-sentinel
pkgver=1.3
pkgrel=1
pkgdesc="Advanced system maintenance"
arch=('any')
license=('GPLv3')

source=('start.py')
sha256sums=('SKIP')

package() {

  install -d "${pkgdir}/usr/lib/system-sentinel"

  install -m644 start.py "${pkgdir}/usr/lib/system-sentinel/start.py"


  install -d "${pkgdir}/usr/bin"
  
  
  echo '#!/bin/sh' > "${pkgdir}/usr/bin/system-sentinel"
  echo 'python3 /usr/lib/system-sentinel/start.py "$@"' >> "${pkgdir}/usr/bin/system-sentinel"
  
 
  chmod +x "${pkgdir}/usr/bin/system-sentinel"
}
