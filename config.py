from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 26730579
    API_HASH = "6db7bd61323d70257705afbc2fba8a82"
    # the name to display in your alive message
    ALIVE_NAME = "Smoker"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = ""
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1BJWap1sBuwe2Xb4WjdosC-b5w5icMyRK28q6DmpuaoXjbk5ZMVncuXQyeQwDjuMBUEeUXMd0BPNkiJv3ho_7wnn9pGyXnK8UljpAHHeMaHV20G1FUthj6jy6I34pdkwBIkW9Fr0mSnD-GO7pcxB8nHzP5pLGfQspsQRbr0cbY-4KYflM_QRlOiaEpo3ksz-seDsG-s0fae1WtCuL7YUEwdq2nEmPIJkpQrvFvgpF36m8JqR_etpSufbL0NTRDW8Zqqhp9j2hkZ-ydfrzQchGFx7Hfno7Ul0TZrZ7zp5Bn-f4RzgocZqOmDWouV2x8uMwEAir88cvxXnu7miS5n6bkR8Ytrhul3U="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = ""
    # command han5991600564:AAG8uKEBhBDnKJmcJsoxLJgXn3iruYOnrkcdler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    VCMODE = False
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
