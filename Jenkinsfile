node('CAE-Jenkins2-DH-Agents-Linux') {
    stage('Checkout') {
        checkout scm
    }

    stage('Reset docker credentials') {
        sh 'docker logout'
    }

    docker.image('https://registry.jpl.nasa.gov/mpowell/firstdown_cloud:firstdown_cloud').inside {
        stage('Gather dependencies') {
            sh 'pip install -r requirements.txt'
        }

        stage('Build') {
            sh 'python setup.py test'
        }
    }
}
