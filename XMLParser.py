from xml.dom.minidom import parse, parseString
from datetime import timedelta, date
import os


def nDaysFromToday(n):
    dt = date.today() + timedelta(days=n)
    return dt.strftime("%Y%m%d")


def parse_update_XML(X, Y):
    if X > Y:
        print("Depart Day cannot be greater than Return Date")
    else:
        try:
            doc = parse('./Data/test_payload1.xml')
            doc.getElementsByTagName(
                "DEPART")[0].childNodes[0].nodeValue = nDaysFromToday(X)
            doc.getElementsByTagName(
                "RETURN")[0].childNodes[0].nodeValue = nDaysFromToday(Y)
            output_path = './Data/test_payload1_updated.xml'
            if os.path.exists(output_path):
                os.remove(output_path)
            with open(output_path, 'x') as fs:
                fs.write(doc.toxml())
                fs.close()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    X = 10
    Y = 11
    parse_update_XML(X, Y)