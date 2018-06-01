node('CAE-Jenkins2-DH-Agents-Linux') {
    stage('Checkout') {
        checkout scm
    }

    stage('Reset docker credentials') {
        sh 'docker logout'
    }

    docker.image('python:2.7-alpine').inside {
        stage('Gather dependencies') {
            sh 'sudo python setup.py install --user'
        }

        stage('Test') {
            sh 'python setup.py test'
        }
    }
}
