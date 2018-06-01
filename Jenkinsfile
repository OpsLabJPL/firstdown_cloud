    node('CAE-Jenkins2-DH-Agents-Linux') {
        stages {
            stage('Checkout') {
                checkout scm
            }

            stage('Test') {
                agent { dockerfile true }
                steps {
                    sh 'python setup.py test'
                }
            }
        }
    }
