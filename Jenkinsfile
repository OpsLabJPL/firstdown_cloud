node('CAE-Jenkins2-DH-Agents-Linux') {
    stage('Checkout') {
        checkout scm
    }

    stage('Reset docker credentials') {
        sh 'docker logout'
    }

    docker.image('cae-artifactory.jpl.nasa.gov:16003/gov/nasa/jpl/cae/jenkins/buildenv/cae-centos7-pyenv27-build-container-git-lfs').inside {
        stage('Gather dependencies') {
            sh 'pip install -r requirements.txt'
        }

        stage('Build') {
            sh 'python setup.py test'
        }
    }
}
