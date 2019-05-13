try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except:
    raise Exception('selenium package missing. Install with: pip install selenium')
from time import sleep
import os
import json


def start_test(d):
    try:
        path = os.path.abspath("form.html")
        d.get("file://" + path)

        with open('automatedTestCases.json') as json_file:
            data = json.load(json_file)
            for p in data['testCases']:
                d.find_element_by_id('fname').send_keys(p['first_name'])
                sleep(0.5)
                d.find_element_by_id('lname').send_keys(p['last_name'])
                sleep(0.5)
                d.find_element_by_id('sid').send_keys(p['student_ID'])
                sleep(0.5)
                d.find_element_by_id('semail').send_keys(p['student_mail'])
                sleep(0.5)
                d.find_elements_by_css_selector("input[type='radio'][value='" + p['gender'] + "']")[0].click()
                sleep(0.5)
                select = Select(d.find_element_by_id('department'))
                select.select_by_visible_text(p['department'])
                sleep(0.5)
                if 'reasonToJoin' in p:
                    d.find_element_by_id('whyjoin').send_keys(p['reasonToJoin'])
                sleep(1)
                d.find_element_by_tag_name('form').submit()
                print '[+] Form submitted'
    except:
        print "error"
    finally:
        d.quit()
        print '[=] BROWSER TEST FINISHED [=]'


def main():
    print '[==] TESTS STARTED [==]'
    print '--------------------------------------------------------------------'
    try:
        print '[=] FireFox BROWSER STARTED [=]'
        d = webdriver.Firefox()  # open browser
        sleep(2)
        start_test(d)
        sleep(3)
        print '[=] Chrome BROWSER STARTED [=]'
        d = webdriver.Chrome()  # open browser
        sleep(2)
        start_test(d)

    except Exception, ex:
        print '[!] Error occured: {}'.format(ex)
        print '[==] ERROR [==]'
    finally:
        print '--------------------------------------------------------------------'
        print '[==] TESTS FINISHED [==]'


if __name__ == "__main__":
    main()
