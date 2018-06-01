pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            checkout scm
        }

        stage('Reset docker credentials') {
            sh 'docker logout'
        }

        docker.image('python:2.7-alpine').inside {
            stage('Test') {
                sh 'python setup.py test'
            }
        }
    }
}
