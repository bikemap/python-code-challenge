# Bikemap python code challenge

As part of your coding challenge you will extend an existing API. The goal of the challenge is to see how you're able to work with existing code.
Successful measurement is to finish two tasks and get the minimum passing score of 25 points. You can earn more points with good code quality measured by writing tests. 
_We believe that writing unit tests is the best software engineer's habit, and also it helps colleagues to understand how the code is working._ 

Expected spend time is no more than 5 hours. Obviously you can spend more if you want, but we value your time. 

## Challenge
The git repository contains a simple API to manage Todo entries. Currently, Todos does not have any categorisation, we would like to be able to add labels/tags to each todo entry.
Since, all data are stored in the app memory, that means it will disappear after each app reload. We would like you to save data in a persistence storage, so the data will survive after an app reload. 

### Your task is
1) Extend the API in a way that it will be possible to add labels/tags to `TodoEntry`.
2) Save data in database (_you can choose any database based on your preferences_).

## Scoring
Minimum passing score is **25 points**

1) **10 points** for finishing task #1
   1) **3 points** for integration tests in `test.http`
   2) **5 points** for unit tests
2) **15 points** for finishing task #2
   1) **10 points** for unit tests

## Installation
Project is fully functional, compatible with Python 3.8 or newer versions. By using [Starlette](https://www.starlette.io/) framework with [Uvicorn](https://www.uvicorn.org) combination.

### Install dependencies

```shell
pip install -r requirements.txt
```

### Run HTTP server
```shell
cd src/app
uvicorn api:app --reload
```

## Testing

### Run tests

```shell
pytest
```

### Integration tests via HTTP

Integration tests are in `tests.http`

_How to work with integration tests in [Pycharm](https://www.jetbrains.com/help/pycharm/http-client-in-product-code-editor.html)._
