pipeline {
    agent {
        docker { image 'shay/home_assignment:version1' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
