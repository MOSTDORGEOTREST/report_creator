# MDGT Report Creator

### Сервис для создания отчетов по опытам.

#### Стек:
* fastapi
* reportlab

## Деплой:
1. Открыть папку ~/ в терминале и выполнить:\
    `git init`\
    `git clone https://github.com/MOSTDORGEOTREST/report_creator.git`

2. Запуск через скрипт из папки проекта:\
    `bash script.sh`


## Пример запроса:

```
data = {
    "object_number": "test",
    "laboratory_number": "test",
    "test_type": "test",
    "data": {
        "test": "test"
    },
    "active": True
}


def request_qr(data):
    with requests.Session() as sess:
        sess.post("https://georeport.ru/auth/sign-in/",
                  data={
                      "username": "trial",
                      "password": "trial",
                      "grant_type": "password",
                      "scope": "",
                      "client_id": "",
                      "client_secret": ""
                  },
                  verify=False, allow_redirects=False
                  )

        response = sess.post('https://georeport.ru/reports/report_and_qr', json=data)
        if not response.ok:
            return (False, response.json()['detail'])

        qr_path = f"{data['object_number']} {data['laboratory_number']} {data['test_type']}.png"

        with open(qr_path, "wb") as file:
            file.write(response.content)
        return (True, qr_path)```

