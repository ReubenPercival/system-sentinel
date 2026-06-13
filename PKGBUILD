pkgname=system-sentinel
pkgver=1.1
pkgrel=1
pkgdesc="Advanced system maintenance"
arch=('any')
license=('MIT')
# Указываем, что файл start.py лежит рядом и его надо включить в сборку
source=('start.py')
sha256sums=('SKIP')

package() {
  # Создаем папку для скрипта
  install -d "${pkgdir}/usr/lib/system-sentinel"
  # Копируем туда твой чистый код
  install -m644 start.py "${pkgdir}/usr/lib/system-sentinel/start.py"

  # Создаем "запускатор" в /usr/bin/
  install -d "${pkgdir}/usr/bin"
  
  # Создаем файл-команду, которая вызовет python для твоего скрипта
  echo '#!/bin/sh' > "${pkgdir}/usr/bin/system-sentinel"
  echo 'python3 /usr/lib/system-sentinel/start.py "$@"' >> "${pkgdir}/usr/bin/system-sentinel"
  
  # Делаем его исполняемым
  chmod +x "${pkgdir}/usr/bin/system-sentinel"
}
