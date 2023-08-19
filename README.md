# Gmailer
Send bulk email in gmail with python. Tested on python 3.6.8.

# Run programme
Run `python -m main`

# Package as executable
Run `pyinstaller -n "Gmailer" -w main.py`

# Qt Designer
1. Download at https://build-system.fman.io/qt-designer-download
1. Edit any `.ui` files
1. Convert `.ui` files to `.py` files with the command `pyside2-uic <input file>.ui -o <output file>.py`

# Password for the email
Since 2022, Google has restricted sign ins from SMTP. To continue to send emails using this application,
you need to set up app passwords and use the generated password when sending emails. See
https://support.google.com/mail/answer/185833?hl=en on how to set app password.
