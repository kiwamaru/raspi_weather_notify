raspi_weather_notify
======================
Raspberry PI2 model bとフルカラーLEDを使用して
今日の天気の降水確率を色で表します。

* 80%以上は赤
* 50%以上は黄
* 30%以上は青
* 20%以上はシアン
* 20%未満は消灯


使い方 
------
## 必要機器 ##

* 角型フルカラーLED 型番:OSTA71A1D-A
* 5Ω抵抗x2
* 65Ω抵抗x1
* あとはブレッドボードその他

## 接続 ##
* REDカソードは65Ωの抵抗を経由してGPIO18(ピン番号12)
* BLUEカソードは5Ωの抵抗を経由してGPIO13(ピン番号33)
* GREENカソードは5Ωの抵抗を経由してGPIO19(ピン番号35)
* アノードはGND(ピン番号9)

## 必要ライブラリのインストール ##

#### GPIOモジュールをインストール ####

`$ sudo apt-get install python-rpi.gpio`

#### pywapiをインストール ####

https://launchpad.net/python-weather-api/trunk/0.3.8/+download/pywapi-0.3.8.tar.gz
をダウンロードして展開後、

`$ python setup.py build`

`$ python setup.py install`

#### このプログラムをインストール ####

`cd /home/pi/`

`git clone https://github.com/kiwamaru/raspi_weather_notify.git`

## CRONへ登録 ##

`$ sudo crontab -e`

`*/5 * * * * sudo python /home/pi/raspi_weather_notify/weather.py`
 
パラメータの解説
----------------
get_weather_from_weather_com('xxxx') で地域コードを指定する。

### 地域コードの調べ方 ###

www.weather.comにて地域を入力すると、以下のようにURLの末尾が地域コードとなる。

`http://www.weather.com/weather/today/l/JAXX0085:1:JA`

'JAXX0085:1:JA'は東京の地域コード

関連情報
--------
### 参考サイト
* https://code.google.com/p/python-weather-api/
* http://ameblo.jp/tetsuro0907/entry-12019192299.html
* http://mamerium.com/raspberry-pi-rpi-gpio-basic/
* http://akizukidenshi.com/catalog/g/gI-01444/
* http://www.bunnyhop.jp/lab-20150114/
