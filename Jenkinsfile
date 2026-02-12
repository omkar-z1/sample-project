pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/omkar-z1/sample-project.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'venv/bin/python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/python manage.py test'
            }
        }
    }
}
