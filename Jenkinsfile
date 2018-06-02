node('CAE-Jenkins2-DH-Agents-Linux') {
    stage('Checkout') {
        checkout scm
    }

    stage('Reset docker credentials') {
        sh 'docker logout'
    }

    docker.image('registry.jpl.nasa.gov/mpowell/firstdown_cloud:fce293df').inside {
        stage('Test') {
            sh 'export USER=mpowell; export AWS_DEFAULT_REGION=us-gov-west-1; python setup.py test'
        }
    }
}
