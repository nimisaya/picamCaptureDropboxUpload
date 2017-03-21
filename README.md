# picamCaptureDropboxUpload
Capture photos using Raspberry Pi Camera and upload to dropbox. Delete local file once photos are uploaded.

### Run
_Note: These instructions are based on running on the Raspberry Pi 3 with Raspbian Jessie Lite OS_

**Capture with Pi camera**
1. Insert Pi camera
2. Enable camera in raspi-config
3. Make sure you have the following installed:
    * python (sudo apt-get install python3)
    * picamera (sudo apt-get install python3-picamera)
4. Specify photo format

**Dropbox Upload**
1. Sign up for Dropbox account at dropbox.com
2. Navigate to [Dropbox Developers](https://www.dropbox.com/developers)
3. Select 'Create your app'
4. Select the following:
    * Dropbox API
    * App folder or Full Dropbox (Depends on purpose)
    * Enter a name for your app
    * Create app
    * Generate code and copy to clipboard
5. Make sure you have the following installed:
    * python (sudo apt-get install python3)
    * pip (sudo apt-get install python3-pip)
    * dropbox for python (sudo pip install dropbox)
6. Use a text editor e.g. nano, to edit the file and fill in:
   * TOKEN - the dropbox app code you generated
   * uploadPath - folder on dropbox you want photo uploaded to (Not required)

**Run**

$ python3 picamCaptureDropboxUpload.py


### Relevant Documentation
* [Picamera Documentation](https://media.readthedocs.org/pdf/picamera/release-1.3/picamera.pdf)
* [Dropbox for Python Documentation](http://dropbox-sdk-python.readthedocs.io/en/latest/index.html)
* [backup-and-restore.py](https://github.com/dropbox/dropbox-sdk-python/blob/master/example/back-up-and-restore/backup-and-restore-example.py)


### Tested
Raspberry Pi 3 with:
* Raspberry Pi Camera v2.1
