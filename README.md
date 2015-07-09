# iData Visa Application Tracker
This script checks visa application status using idata.com.tr services in Turkey (for Germany and Italy) and notifies OSX Notification Center.


## Installation
The following command will run the script which will be checking the visa application status every 300 seconds.

**Run**
`python main.py`

**Configuration**
in `config.py`

    country_code="<COUNTRY_CODE: de|it>"
    application_id="<APPLICATION_ID>"
    passport_id="<PASSPORT_NUMBER>"
