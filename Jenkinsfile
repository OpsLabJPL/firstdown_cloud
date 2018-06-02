node('CAE-Jenkins2-DH-Agents-Linux') {
    stage('Checkout') {
        checkout scm
    }

    stage('Reset docker credentials') {
        sh 'docker logout'
    }

    docker.image('registry.jpl.nasa.gov/mpowell/firstdown_cloud:latest').inside {
        stage('Gather dependencies') {
            sh 'pip install -r requirements.txt'
        }

        stage('Build') {
            sh 'export USER=mpowell; export AWS_DEFAULT_REGION=us-gov-west-1; python setup.py test'
        }
    }
}
