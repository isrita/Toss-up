# Toss Up

Recipe generator application that offers the user detailed instructions, step by step, accompanied by images. This service is made possible by OpenAI tools such as its image builder and text completion model.

### Manual Installation:

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure you replace the valudes with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

4. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
5. Run the migrations: `$ pipenv run upgrade`
6. Run the application: `$ pipenv run start`

### Front-End Manual Installation:

-   Make sure you are using node version 14+ and that you have already successfully installed and runned the backend.

1. Install the packages: `$ npm install`
2. Start coding! start the webpack dev server `$ npm run start`

## Usage
Run pipenv run and npm run start you need tu have a database created

## User VIEWS

### Landing-page
![image](https://github.com/isrita/Toss-up/assets/40001587/732c13bb-a823-4cbb-9407-4cd97fd2a4a1)
### home-page
![image](https://github.com/isrita/Toss-up/assets/40001587/b7771f55-ac27-4615-ae25-2c301e3db159)
### Chatbot
![image](https://github.com/isrita/Toss-up/assets/40001587/fe99af9a-a4b7-4657-9c9c-9aea436c6a6a)
### Recipe
![image](https://github.com/isrita/Toss-up/assets/40001587/ae95b9ba-033e-4628-b220-a33e6e8573d6)
### Recipe 2
![image](https://github.com/isrita/Toss-up/assets/40001587/df810342-fea4-4473-b53f-10ca5e1358cc)


### Contributors

@josewilmerDR
@Materonlove
@isrita
@estebansolanog
