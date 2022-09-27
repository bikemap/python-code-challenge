# App structure

## 📁 apischema
Application logic for working with json api (encoding, validation, schema).

## 📁 persistence
Application logic for data persistence. Where `repository` is representing contract with outer layers to persist data. `mapper` is representing implementation for specific adapter (like: Sqlite, Elastic search, 3rd party API, etc...).  

## 📁 tests
Unit tests. Directory structure is mimicking app folder structure.

## 🐍 api.py
Bootstrap file for API based on [Starlette](https://www.starlette.io/) framework.

## 🐍 entities.py
Business entities.

## 🐍 usecases.py
Business logic application.
