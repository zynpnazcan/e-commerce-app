pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('GitHub Access Token')
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/zynpnazcan/e-commerce-app.git', credentialsId: 'GitHub Access Token'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }
    }
}