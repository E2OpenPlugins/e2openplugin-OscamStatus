from distutils.core import setup
import setup_translate

pkg = 'Extensions.OscamStatus'
setup(name='enigma2-plugin-extensions-oscamstatus',
       version='1.3.3',
       description='shows status of your oscam server',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
       package_data={pkg: ['*.png', '*.xml', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass, # for translation
      )
