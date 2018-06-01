pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Reset docker credentials') {
            steps {
                sh 'docker logout'
            }
        }

        docker.image('python:2.7-alpine').inside {
            stage('Test') {
                steps {
                    sh 'python setup.py test'
                }
            }
        }
    }
}
