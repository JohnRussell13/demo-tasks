import requests
import re
import os
import time

for i in range(0,50,1):

    x = requests.get('https://take.quiz-maker.com/poll4331296xb920AdDc-136')
    # print(x.text)

    y = re.search("\"qp_d4331296\" value=\"", x.text)
    z = re.search("\"><input type=hidden name=\"qp_fp4331296\" value=\"", x.text)
    # print(y.end())

    print(x.text)

    f = x.text[y.end():z.start()]
    # print(f)

    # str = "curl 'https://take.quiz-maker.com/results4331296xb920AdDc-136' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://take.quiz-maker.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://take.quiz-maker.com/poll4331296xb920AdDc-136' -H 'Cookie: Tracking%5FSID=; ASPSESSIONIDQWSQDCSQ=ODAJHBEAEGBEOECFODOLLKBB; QP%5F4331296=Y; Tracking%5FCID=E693919C57724906b9624e21B' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' --data-raw 'qp_ipt4331296=185.169.233.191%2C172.70.130.233&qp_d4331296="+ f +"&qp_fp4331296=80723571&qp_v4331296=9&qp_b4331296=Vote'"
    str = "curl 'https://take.quiz-maker.com/results4331296xb920AdDc-136' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://take.quiz-maker.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://take.quiz-maker.com/poll4331296xb920AdDc-136' -H 'Cookie: Tracking%5FSID=; ASPSESSIONIDQWSQDCSQ=ODAJHBEAEGBEOECFODOLLKBB' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' --data-raw 'qp_ipt4331296=185.169.233.191%2C172.70.130.233&qp_d4331296="+ f +"&qp_fp4331296=80723571&qp_v4331296=9&qp_b4331296=Vote'"

    # print(str)
    
    # time.sleep(5)
    # os.system("nordvpn connect rs")
    # time.sleep(5)
    os.system(str)

    #curl 'https://take.quiz-maker.com/results4331296xb920AdDc-136' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://take.quiz-maker.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://take.quiz-maker.com/poll4331296xb920AdDc-136' -H 'Cookie: Tracking%5FSID=; ASPSESSIONIDQWSQDCSQ=ODAJHBEAEGBEOECFODOLLKBB; QP%5F4331296=Y; Tracking%5FCID=E693919C57724906b9624e21B' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' --data-raw 'qp_ipt4331296=185.169.233.191%2C172.70.130.233&qp_d4331296=44691.3439795057-44691.3479754274&qp_fp4331296=80723571&qp_v4331296=9&qp_b4331296=Vote'
    #curl 'https://take.quiz-maker.com/results4331296xb920AdDc-136' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://take.quiz-maker.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://take.quiz-maker.com/poll4331296xb920AdDc-136' -H 'Cookie: Tracking%5FSID=; ASPSESSIONIDQWSQDCSQ=ODAJHBEAEGBEOECFODOLLKBB; QP%5F4331296=Y; Tracking%5FCID=E693919C57724906b9624e21B' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' --data-raw 'qp_ipt4331296=185.169.233.191%2C172.70.130.233&qp_d4331296=44691.3440543545-44691.3443290707&qp_fp4331296=80723571&qp_v4331296=9&qp_b4331296=Vote'
    
    #curl 'https://take.quiz-maker.com/results4331296xb920AdDc-136' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://take.quiz-maker.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://take.quiz-maker.com/poll4331296xb920AdDc-136' -H 'Cookie: Tracking%5FSID=; ASPSESSIONIDQUSTDDSQ=MPBHANABJGJONBNMFOELNMJN' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers' --data-raw 'qp_ipt4331296=141.98.103.221%2C172.70.131.130&qp_d4331296=44691.7845379229-44691.7847963736&qp_fp4331296=80723571&qp_v4331296=9&qp_b4331296=Vote'