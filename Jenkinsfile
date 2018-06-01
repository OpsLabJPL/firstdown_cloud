    node('CAE-Jenkins2-DH-Agents-Linux') {
        agent { dockerfile true }
        stages {
            stage('Checkout') {
                checkout scm
            }

            stage('Test') {
                sh 'python setup.py test'
            }
        }
    }
