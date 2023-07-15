# Shopping Tem Data

Shopping Tem Data is the data branch of the Shopping Tem project, focusing on data-related tasks such as database migrations, data gathering, cleaning, and loading scripts. This repository contains all the necessary components for managing and processing data in the context of the Shopping Tem project.

# Introduction

Shopping Tem is a web application that enables users to search for shopping centers containing two or more stores they want to visit. Leveraging modern web technologies, the app combines a user-friendly interface with advanced backend functionality. It provides a seamless and efficient solution for users to explore and find shopping destinations that meet their needs.

# Features
The Shopping Tem Data repository offers the following features:

- **Database Migrations**: Includes scripts and configurations for managing database migrations. This ensures that the database structure is up-to-date and in sync with the latest changes in the project.

- **Data Gathering Scripts**: Provides a collection of scripts used for gathering data from various sources. These scripts facilitate tasks such as data extraction and collection from APIs, web scraping, or importing data from external files.

- **Data Cleaning Scripts**: Contains scripts responsible for cleaning and preprocessing the gathered data. These scripts perform tasks such as removing duplicates, handling missing values, standardizing formats, and transforming data.

- **Data Loading Scripts**: Includes scripts for loading the cleaned and processed data into the database. These scripts ensure that the data is properly stored and ready for analysis and use by other components of the Shopping Tem project.

# Instalation

1. Clone the repository:

```bash
git clone https://github.com/pedrodrocha/shopping-tem-data.git ./
```

2. Install the required dependencies:

```bash
poetry install
```

3. Configure the database connection 

```bash
cp .env.example .env
```
Update the `.env` file with your specific database configuration.

4. Perform the necessary database migrations:

```bash
alembic upgrade head
```
This command will apply any pending database migrations and ensure that the database structure is up to date.

$ License
The Shopping Tem Data repository is open-source and is licensed under the MIT License. You can freely use, modify, and distribute the codebase in accordance with the terms of this license.