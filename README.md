raspi_weather_notify
======================
Raspberry PI�ƃt���J���[LED���g�p����
�����̓V�C�̍~���m����F�ŕ\���܂��B
 
�g����
------
### �K�v�@�� ###
 �t���J���[LED �^��:OSTA71A1D-A

RED�J�\�[�h��65���̒�R���o�R����GPIO18(�s���ԍ�12)
BLUE�J�\�[�h��5���̒�R���o�R����GPIO13(�s���ԍ�33)
GREEN�J�\�[�h��5���̒�R���o�R����GPIO19(�s���ԍ�35)
�A�m�[�h��GND(�s���ԍ�9)

### �K�v���C�u�����̃C���X�g�[�� ###
$ sudo apt-get install python-rpi.gpio
https://launchpad.net/python-weather-api/trunk/0.3.8/+download/pywapi-0.3.8.tar.gz
���_�E�����[�h���ēW�J��A
$ python setup.py build
$ python setup.py install

### CRON�֓o�^ ###
$ sudo crontab -e
*/5 * * * * sudo python /home/pi/python_code/raspi_weather_notify/weather.py
 
�p�����[�^�̉��
----------------
get_weather_from_weather_com('xxxx') �Œn��R�[�h���w�肷��B

### �n��R�[�h�̒��ו� ###
www.weather.com�ɂĒn�����͂���ƁA�ȉ��̂悤��URL�̖������n��R�[�h�ƂȂ�B
http://www.weather.com/weather/today/l/JAXX0085:1:JA
'JAXX0085:1:JA'�͓����̒n��R�[�h

�֘A���
--------
### �Q�l�T�C�g
https://code.google.com/p/python-weather-api/
http://ameblo.jp/tetsuro0907/entry-12019192299.html
http://mamerium.com/raspberry-pi-rpi-gpio-basic/
http://akizukidenshi.com/catalog/g/gI-01444/
http://www.bunnyhop.jp/lab-20150114/
